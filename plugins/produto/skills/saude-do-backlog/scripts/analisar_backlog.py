#!/usr/bin/env python3
"""Resume a saúde de um backlog exportado em CSV e imprime um relatório em Markdown.

Uso:
    python3 analisar_backlog.py backlog.csv
    python3 analisar_backlog.py backlog.csv --hoje 2026-10-06 --topo 10

O CSV precisa de uma linha de cabeçalho. As colunas são reconhecidas por nome, sem diferenciar
maiúsculas, minúsculas e acentos (as que não existirem são ignoradas):

  titulo      titulo, title, nome, summary, resumo
  criado em   criado, criado_em, data_criacao, created, created_at
  tamanho     tamanho, estimativa, pontos, size, story_points
  status      status, estado, situacao
  ordem       prioridade, ordem, rank (número; se faltar, vale a ordem das linhas, do topo para baixo)

Itens com status feito, concluido, done, closed, cancelado ou descartado ficam de fora.
Só usa a biblioteca padrão do Python.
"""

import argparse
import csv
import io
import re
import statistics
import sys
import unicodedata
from datetime import date, datetime
from difflib import SequenceMatcher

NOMES = {
    "titulo": ("titulo", "title", "nome", "summary", "resumo"),
    "criado": ("criado", "criado_em", "data_criacao", "created", "created_at"),
    "tamanho": ("tamanho", "estimativa", "pontos", "size", "story_points"),
    "status": ("status", "estado", "situacao"),
    "ordem": ("prioridade", "ordem", "rank"),
}
FECHADOS = {"feito", "concluido", "done", "closed", "cancelado", "descartado", "resolvido"}
PALAVRAS_EPICO = ("gerenciar", "administrar", "sistema de", "modulo de", "completo", "etc", "end-to-end")
TAMANHOS_GRANDES = {"g", "gg", "xl", "xxl", "grande", "13", "20", "21", "40", "100"}


def erro(msg):
    print(f"Erro: {msg}", file=sys.stderr)
    sys.exit(1)


def normalizar(texto):
    texto = unicodedata.normalize("NFKD", str(texto)).encode("ascii", "ignore").decode()
    return re.sub(r"\s+", " ", texto).strip().lower()


def ler_data(texto):
    texto = str(texto).strip()
    for formato in ("%Y-%m-%d", "%d/%m/%Y", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S", "%d/%m/%Y %H:%M"):
        try:
            return datetime.strptime(texto[:19] if "T" in texto or " " in texto else texto, formato).date()
        except ValueError:
            continue
    return None


def carregar(caminho):
    try:
        with open(caminho, encoding="utf-8-sig", newline="") as f:
            texto = f.read()
        try:
            dialeto = csv.Sniffer().sniff(texto[:4096], delimiters=",;\t")
        except csv.Error:
            dialeto = csv.excel
        leitor = csv.DictReader(io.StringIO(texto), dialect=dialeto)
        linhas = list(leitor)
        cabecalho = leitor.fieldnames or []
    except FileNotFoundError:
        erro(f"arquivo não encontrado: {caminho}")
    mapa = {}
    for campo, opcoes in NOMES.items():
        for coluna in cabecalho:
            if normalizar(coluna).replace(" ", "_") in opcoes:
                mapa[campo] = coluna
                break
    if "titulo" not in mapa:
        erro('não achei a coluna de título (use um destes nomes: titulo, title, nome, summary)')
    return linhas, mapa


def percentil(valores, p):
    valores = sorted(valores)
    k = max(0, min(len(valores) - 1, int(round(p / 100 * (len(valores) - 1)))))
    return valores[k]


def main():
    ap = argparse.ArgumentParser(description="Resumo da saúde de um backlog em CSV")
    ap.add_argument("arquivo")
    ap.add_argument("--hoje", help="data de referência (AAAA-MM-DD); padrão: hoje")
    ap.add_argument("--topo", type=int, default=10, help="quantos itens do topo olhar (padrão 10)")
    args = ap.parse_args()
    hoje = ler_data(args.hoje) if args.hoje else date.today()
    if hoje is None:
        erro("data inválida em --hoje; use AAAA-MM-DD")

    linhas, mapa = carregar(args.arquivo)
    abertos = []
    for linha in linhas:
        if "status" in mapa and normalizar(linha.get(mapa["status"], "")) in FECHADOS:
            continue
        if not str(linha.get(mapa["titulo"], "")).strip():
            continue
        abertos.append(linha)
    if not abertos:
        erro("nenhum item aberto encontrado")
    if "ordem" in mapa:
        def chave(l):
            try:
                return float(str(l.get(mapa["ordem"], "")).replace(",", "."))
            except ValueError:
                return float("inf")
        abertos.sort(key=chave)

    titulos = [str(l[mapa["titulo"]]).strip() for l in abertos]
    out = [f"# Saúde do backlog ({len(abertos)} itens abertos, referência {hoje.isoformat()})\n"]

    # Idade
    if "criado" in mapa:
        idades = []
        for l in abertos:
            d = ler_data(l.get(mapa["criado"], ""))
            if d:
                idades.append((hoje - d).days)
        if idades:
            velhos90 = sum(1 for i in idades if i > 90)
            velhos180 = sum(1 for i in idades if i > 180)
            out.append("## Idade dos itens")
            out.append(f"- Mediana: {int(statistics.median(idades))} dias; percentil 85: {percentil(idades, 85)} dias; máxima: {max(idades)} dias")
            out.append(f"- Com mais de 90 dias: {velhos90} ({100 * velhos90 // len(idades)}%); com mais de 180 dias: {velhos180} ({100 * velhos180 // len(idades)}%)\n")
        else:
            out.append("## Idade dos itens\n- Não consegui ler as datas de criação (use AAAA-MM-DD ou DD/MM/AAAA).\n")
    else:
        out.append("## Idade dos itens\n- Sem coluna de data de criação.\n")

    # Tamanho
    if "tamanho" in mapa:
        tamanhos = [normalizar(l.get(mapa["tamanho"], "")) for l in abertos]
        sem = sum(1 for t in tamanhos if not t)
        grandes = [i for i, t in enumerate(tamanhos) if t in TAMANHOS_GRANDES]
        out.append("## Tamanho")
        out.append(f"- Sem tamanho ou estimativa: {sem} ({100 * sem // len(abertos)}%)")
        out.append(f"- Provavelmente grandes demais (tamanho G, GG, 13 ou mais): {len(grandes)} ({100 * len(grandes) // len(abertos)}%)")
        topo = min(args.topo, len(abertos))
        topo_grandes = [titulos[i] for i in grandes if i < topo]
        topo_sem = sum(1 for t in tamanhos[:topo] if not t)
        out.append(f"- No topo ({topo} primeiros): {len(topo_grandes)} grandes e {topo_sem} sem tamanho. O topo deveria ser pequeno e estimado.")
        for t in topo_grandes[:5]:
            out.append(f"  - grande no topo: {t}")
        out.append("")
    else:
        out.append("## Tamanho\n- Sem coluna de tamanho ou estimativa.\n")

    # Palavras de épico
    suspeitos = [t for t in titulos if any(re.search(r"\b" + re.escape(p) + r"\b", normalizar(t)) for p in PALAVRAS_EPICO)]
    out.append("## Itens com cara de épico")
    out.append(f"- Títulos com palavras amplas (gerenciar, administrar, sistema de, completo, etc.): {len(suspeitos)} ({100 * len(suspeitos) // len(abertos)}%)")
    for t in suspeitos[:5]:
        out.append(f"  - {t}")
    out.append("")

    # Duplicados
    pares = []
    limite = min(len(titulos), 1500)
    norm = [normalizar(t) for t in titulos[:limite]]
    for i in range(len(norm)):
        for j in range(i + 1, len(norm)):
            if SequenceMatcher(None, norm[i], norm[j]).ratio() >= 0.8:
                pares.append((titulos[i], titulos[j]))
    out.append("## Possíveis duplicados (títulos muito parecidos)")
    out.append(f"- {len(pares)} par(es)" + (f" (analisei só os {limite} primeiros itens)" if len(titulos) > limite else ""))
    for a, b in pares[:8]:
        out.append(f"  - \"{a}\" e \"{b}\"")
    out.append("")

    # Volume
    out.append("## Volume")
    out.append(f"- {len(abertos)} itens abertos. Referência prática: o horizonte de trabalho cabe em poucas sprints; o resto é opção, não compromisso.")
    out.append("\nObservação: os números são sinais para a conversa. Itens antigos podem ser importantes, e títulos parecidos podem não ser duplicados.")
    print("\n".join(out))


if __name__ == "__main__":
    main()
