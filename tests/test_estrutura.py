"""Confere a estrutura das skills: frontmatter, referências citadas, rubricas (pesos e faixas), referências cruzadas e exemplos.

Rode a partir da raiz do repositório: python3 scripts/testar.py
"""
import re,pathlib,json,sys
S=pathlib.Path(__file__).resolve().parent.parent/"plugins"/"produto"/"skills"
skills=sorted(p.name for p in S.iterdir() if p.is_dir())
fails=[]; notes=[]; FORMATO={}
def F(sk,msg): fails.append(f"{sk}: {msg}")
for sk in skills:
    d=S/sk; t=(d/"SKILL.md").read_text(encoding="utf-8")
    # 1 arquivos de references órfãos
    for f in sorted((d/"references").glob("*.md")):
        if f"references/{f.name}" not in t: F(sk,f"references/{f.name} não é citado no SKILL.md")
        txt=f.read_text(encoding="utf-8")
        if len(txt.splitlines())>300 and "Conteúdo" not in txt[:600]: F(sk,f"{f.name} tem >300 linhas e não tem sumário")
    for f in sorted((d/"scripts").glob("*")) if (d/"scripts").exists() else []:
        if f.suffix in (".py",) and f"scripts/{f.name}" not in t: F(sk,f"scripts/{f.name} não é citado")
    # 2 referências cruzadas a outras skills
    for ref in set(re.findall(r"skill `([a-z0-9-]+)`",t)):
        if ref not in skills: F(sk,f"cita skill inexistente `{ref}`")
    # 3 rubrica x tabela de critérios
    rub=d/"references"/"rubrica.md"
    mt=re.search(r"\|\s*#\s*\|([^\n]*[Pp]eso[^\n]*)\n\|[-| ]+\n((?:\|[^\n]*\n?)+)",t)
    if mt and rub.exists():
        crit=[]
        hdr=mt.group(1).split("|")
        iw=[i for i,c in enumerate(hdr) if c.strip().lower().startswith("peso")][0]+1
        for r in mt.group(2).strip().splitlines():
            c=[x.strip() for x in r.strip("|").split("|")]
            crit.append((c[1],int(re.search(r"\d+",c[iw]).group())))
        rt=rub.read_text(encoding="utf-8")
        secs=re.findall(r"^## (\d+)\.\s+(.+?)\s*\((?:peso\s*)?(\d+)\)\s*$",rt,re.M)
        if secs:  # formato longo (4 faixas por seção)
            if len(secs)!=len(crit): F(sk,f"rubrica tem {len(secs)} critérios, SKILL.md tem {len(crit)}")
            else:
                for (n,nome,peso),(cn,cp) in zip(secs,crit):
                    if int(peso)!=cp: F(sk,f"peso do critério {n} difere: rubrica {peso} x SKILL {cp} ({cn})")
            for b in re.split(r"^## \d+\.",rt,flags=re.M)[1:]:
                nome=b.splitlines()[0].strip()
                faixas=re.findall(r"^\|\s*(\d+)-(\d+)\s*\|",b,re.M)
                if sk=="user-story" and nome.startswith("Tamanho"):
                    if len(faixas)!=5: F(sk,"Tamanho deveria ter 5 faixas"); 
                    continue
                if len(faixas)!=4: F(sk,f"critério '{nome[:30]}' tem {len(faixas)} faixas (esperado 4)"); continue
                fs=sorted((int(a),int(b2)) for a,b2 in faixas)
                if fs[0][0]!=0 or fs[-1][1]!=100 or any(fs[i][1]+1!=fs[i+1][0] for i in range(3)): F(sk,f"critério '{nome[:30]}': faixas com lacuna: {fs}")
            formato="longo"
        else:  # formato matriz
            linhas=re.findall(r"^\|\s*\*\*(\d+)\.\s*(.+?)\s*\((\d+)\)\*\*([^\n]*)$",rt,re.M)
            if len(linhas)!=len(crit): F(sk,f"matriz tem {len(linhas)} critérios, SKILL.md tem {len(crit)}")
            else:
                for (n,nome,peso,resto),(cn,cp) in zip(linhas,crit):
                    if int(peso)!=cp: F(sk,f"peso do critério {n} difere: rubrica {peso} x SKILL {cp} ({cn})")
                    cels=[c.strip() for c in resto.strip().strip("|").split("|")]
                    bandas=cels[-4:]
                    if len(cels) not in (4,5) or any(not c for c in bandas): F(sk,f"critério {n} sem as 4 faixas preenchidas")
            if not re.search(r"\|[^\n]*90-100[^\n]*70-89[^\n]*40-69[^\n]*0-39",rt): F(sk,"matriz sem cabeçalho 90-100/70-89/40-69/0-39")
            formato="matriz"
        FORMATO[sk]=formato
        # sumário da rubrica lista todos
    elif not rub.exists() and sk not in ("priorizacao","papel-de-produto"): F(sk,"sem rubrica.md")
    # 4 regras de teto mencionadas se há nota geral
    if mt and "teto" not in t.lower() and "não passa de" not in t.lower(): F(sk,"avalia com nota mas não declara regra de teto")
    # 5 seção de formato de saída
    if not re.search(r"formato de saída|Formato de saída|O que entregar",t): F(sk,"sem seção de formato de saída")
    # 6 sem placeholders esquecidos
    for m in re.finditer(r"TODO|XXX|lorem|\[\.\.\.\]\s*$",t): notes.append(f"{sk}: possível placeholder '{m.group()}'")
# 7 exemplos: teto de bloqueio respeitado
for sk in skills:
    ex=next(iter(sorted((S/sk/"references").glob("exemplo*.md"))),None)
    if not ex:
        if sk=="visao-do-produto" and "Exemplo completo" in (S/sk/"references"/"modelos.md").read_text(encoding="utf-8"): continue
        F(sk,"sem exemplo"); continue
    txt=ex.read_text(encoding="utf-8")
    notas=[int(m.group(1)) for m in re.finditer(r"^\|[^|\n]*\((?:peso\s*)?\d+\)\s*\|\s*(\d+)\s*\|",txt,re.M)]
    g=re.search(r"(?:Nota geral|Robustez|Termômetro|Qualidade da hipótese)[:\s*]*\**\s*(\d+)/100",txt)
    if notas and g and min(notas)<40 and int(g.group(1))>69: F(sk,f"exemplo viola teto: nota {g.group(1)} com critério {min(notas)}")

# 8 voz do autor: sem travessão longo ou curto nem hífen duplo nos textos
RAIZ=S.parent.parent.parent
for f in sorted(RAIZ.rglob("*")):
    if not f.is_file() or f.suffix not in (".md",".json",".py",".csv",".yml") or f.name=="test_estrutura.py" or any(x in f.parts for x in ("dist",".git")): continue
    for n,l in enumerate(f.read_text(encoding="utf-8").splitlines(),1):
        if "\u2014" in l or "\u2013" in l or " -- " in l: F(f.relative_to(RAIZ).as_posix(),f"linha {n}: travessão ou hífen duplo")
print(f"ESTRUTURA: {len(skills)} skills verificadas; rubricas: "+", ".join(f"{k}={v}" for k,v in sorted(FORMATO.items())))
print("FALHAS:" if fails else "Nenhuma falha.")
for f in fails: print(" -",f)
for n in notes: print(" nota:",n)

sys.exit(1 if fails else 0)
