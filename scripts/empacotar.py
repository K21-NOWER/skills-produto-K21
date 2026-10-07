#!/usr/bin/env python3
"""Gera os arquivos .zip de distribuição na pasta dist/.

Arquivos gerados:
  dist/<skill>.zip          uma skill por arquivo
                            (Claude.ai e Claude Desktop: Customize > Skills > Upload a skill)
  dist/produto-k21.zip      todas as skills reunidas em uma só (pacote único), para subir uma vez
  dist/produto-plugin.zip   o plugin completo
                            (Claude.ai e Claude Desktop: Customize > Plugins > Add > Upload plugin)

O pacote único é montado a partir das skills de plugins/produto/skills, que são a fonte
única da verdade, mais o roteador pacote-unico/SKILL.md. Nada é copiado à mão: ao mudar uma skill,
basta rodar este script de novo.

Antes de gerar qualquer arquivo, o script confere frontmatter, nomes, tamanho das descrições,
caminhos citados e a regra de "um único SKILL.md" no pacote único. Se algo falhar, nada é gerado.

Uso, a partir da raiz do repositório:
    python3 scripts/empacotar.py
"""

import json
import re
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PLUGIN = RAIZ / "plugins" / "produto"
SKILLS = PLUGIN / "skills"
ROTEADOR = RAIZ / "pacote-unico" / "SKILL.md"
MARKETPLACE = RAIZ / ".claude-plugin" / "marketplace.json"
DIST = RAIZ / "dist"
NOME_PACOTE = "produto-k21"
IGNORAR_PADROES = shutil.ignore_patterns(".DS_Store", "__pycache__", "*.pyc")


def deve_ignorar(caminho):
    return caminho.name == ".DS_Store" or "__pycache__" in caminho.parts or caminho.suffix == ".pyc"


def arquivos_de(pasta):
    return [c for c in sorted(pasta.rglob("*")) if c.is_file() and not deve_ignorar(c)]


def compactar(pasta_base, destino, prefixo=""):
    """Compacta tudo de pasta_base em destino. O prefixo, se houver, vira a pasta de topo do zip."""
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as zf:
        for caminho in arquivos_de(pasta_base):
            relativo = caminho.relative_to(pasta_base)
            arcname = Path(prefixo) / relativo if prefixo else relativo
            zf.write(caminho, arcname.as_posix())


def separar_frontmatter(texto):
    m = re.match(r"\A---\n(.*?)\n---\n", texto, re.S)
    if not m:
        raise ValueError("SKILL.md sem frontmatter")
    campos = {}
    for linha in m.group(1).splitlines():
        chave, _, valor = linha.partition(": ")
        campos[chave.strip()] = valor.strip()
    return campos, texto[m.end():]


def verificar_skill(pasta, nome_esperado=None):
    texto = (pasta / "SKILL.md").read_text(encoding="utf-8")
    campos, _ = separar_frontmatter(texto)
    erros = []
    nome = campos.get("name", "")
    if nome != (nome_esperado or pasta.name):
        erros.append(f"{pasta.name}: o name '{nome}' é diferente do nome da pasta")
    if not re.fullmatch(r"[a-z0-9-]{1,64}", nome):
        erros.append(f"{pasta.name}: name inválido '{nome}'")
    descricao = campos.get("description", "")
    if not descricao or len(descricao) > 1024:
        erros.append(f"{pasta.name}: description vazia ou com mais de 1024 caracteres ({len(descricao)})")
    if len(texto.splitlines()) > 500:
        erros.append(f"{pasta.name}: SKILL.md com mais de 500 linhas")
    return erros


def verificar_caminhos(rotulo, texto, base):
    """Todo caminho de references, scripts ou modos citado entre crases precisa existir em base."""
    erros = []
    for caminho in sorted(set(re.findall(r"`((?:references|scripts|modos)/[\w./-]+)`", texto))):
        if not (base / caminho).exists():
            erros.append(f"{rotulo}: caminho citado não existe: {caminho}")
    return erros


def converter_para_modo(nome, texto):
    """Transforma o SKILL.md de uma skill no MODO.md do pacote único."""
    _, corpo = separar_frontmatter(texto)
    corpo = corpo.lstrip("\n")
    corpo = corpo.replace("${CLAUDE_SKILL_DIR}/scripts/", f"${{CLAUDE_SKILL_DIR}}/modos/{nome}/scripts/")
    corpo = re.sub(r"`(references|scripts)/", rf"`modos/{nome}/\1/", corpo)
    return corpo


def montar_pacote_unico(pasta_temporaria):
    raiz = pasta_temporaria / NOME_PACOTE
    raiz.mkdir(parents=True)
    shutil.copy(ROTEADOR, raiz / "SKILL.md")
    for pasta in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        modo = raiz / "modos" / pasta.name
        modo.mkdir(parents=True)
        texto = (pasta / "SKILL.md").read_text(encoding="utf-8")
        (modo / "MODO.md").write_text(converter_para_modo(pasta.name, texto), encoding="utf-8")
        for sub in ("references", "scripts"):
            if (pasta / sub).is_dir():
                shutil.copytree(pasta / sub, modo / sub, ignore=IGNORAR_PADROES)
    return raiz


def verificar_pacote_unico(raiz):
    erros = verificar_skill(raiz, NOME_PACOTE)
    total = len(list(raiz.rglob("SKILL.md")))
    if total != 1:
        erros.append(f"o pacote único deve ter exatamente um SKILL.md, mas tem {total}")
    roteador = (raiz / "SKILL.md").read_text(encoding="utf-8")
    erros += verificar_caminhos("roteador", roteador, raiz)
    for modo in sorted((raiz / "modos").iterdir()):
        if f"`modos/{modo.name}/MODO.md`" not in roteador:
            erros.append(f"o roteador não lista o modo {modo.name}")
    for modo in sorted((raiz / "modos").iterdir()):
        texto = (modo / "MODO.md").read_text(encoding="utf-8")
        erros += verificar_caminhos(f"modo {modo.name}", texto, raiz)
        soltos = re.findall(r"`(?:references|scripts)/[^`]*`", texto)
        if soltos:
            erros.append(f"modo {modo.name}: caminhos sem o prefixo modos/: {soltos}")
    return erros


def verificar_plugin():
    erros = []
    try:
        plugin = json.loads((PLUGIN / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
        marketplace = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        return [f"JSON inválido ou ausente: {e}"]
    nomes = [p.get("name") for p in marketplace.get("plugins", [])]
    if plugin.get("name") not in nomes:
        erros.append(f"o plugin '{plugin.get('name')}' não está listado no marketplace ({nomes})")
    for entrada in marketplace.get("plugins", []):
        origem = entrada.get("source")
        if isinstance(origem, str) and not (RAIZ / origem).exists():
            erros.append(f"source do marketplace não existe: {origem}")
    for obrigatorio in ("README.md", "LICENSE"):
        if not (PLUGIN / obrigatorio).exists():
            erros.append(f"falta {obrigatorio} na pasta do plugin")
    return erros


def main():
    erros = verificar_plugin()
    pastas = sorted(p for p in SKILLS.iterdir() if p.is_dir())
    for pasta in pastas:
        erros += verificar_skill(pasta)
        erros += verificar_caminhos(pasta.name, (pasta / "SKILL.md").read_text(encoding="utf-8"), pasta)

    with tempfile.TemporaryDirectory() as tmp:
        raiz = montar_pacote_unico(Path(tmp))
        erros += verificar_pacote_unico(raiz)
        if erros:
            print("Nada foi gerado. Corrija os problemas abaixo:", file=sys.stderr)
            for erro in erros:
                print(f"  - {erro}", file=sys.stderr)
            sys.exit(1)

        shutil.rmtree(DIST, ignore_errors=True)
        DIST.mkdir()
        for pasta in pastas:
            compactar(pasta, DIST / f"{pasta.name}.zip", prefixo=pasta.name)
        compactar(raiz, DIST / f"{NOME_PACOTE}.zip", prefixo=NOME_PACOTE)
        compactar(PLUGIN, DIST / "produto-plugin.zip")

    for arquivo in sorted(DIST.glob("*.zip")):
        print(f"Gerado: dist/{arquivo.name} ({arquivo.stat().st_size / 1024:.0f} KB)")


if __name__ == "__main__":
    main()
