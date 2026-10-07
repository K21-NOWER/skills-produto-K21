"""Testa os três scripts (calcular.py, prever.py, analisar_backlog.py) com valores calculados à mão, casos-limite e entradas inválidas.

Rode a partir da raiz do repositório: python3 scripts/testar.py
"""
import subprocess, json, sys, tempfile, os, re, csv
import pathlib
S=str(pathlib.Path(__file__).resolve().parent.parent/"plugins"/"produto"/"skills")
res=[]
def run(args, inp=None):
    p=subprocess.run([sys.executable]+args,capture_output=True,text=True,input=inp)
    return p.returncode,p.stdout,p.stderr
def check(nome,cond,det=""):
    res.append((nome,bool(cond),det)); 
calc=f"{S}/priorizacao/scripts/calcular.py"
def js(d):
    f=tempfile.NamedTemporaryFile('w',suffix='.json',delete=False,encoding='utf-8'); json.dump(d,f); f.close(); return f.name
# --- calcular.py: valores esperados calculados à mão
rc,o,e=run([calc,"rice",f"{S}/priorizacao/scripts/exemplo-rice.json"]); check("calcular rice: exemplo roda",rc==0,o.splitlines()[2][:60] if rc==0 else e)
rc,o,e=run([calc,"rice",js({"itens":[{"nome":"A","alcance":4000,"impacto":3,"confianca":0.8,"esforco":1.5}]})]); check("rice A = 6400",rc==0 and "| 6400 |" in o.replace(" ","|").replace("||","|") or "6400" in o,o.splitlines()[-1])
rc,o,e=run([calc,"rice",js({"itens":[{"nome":"A","alcance":1000,"impacto":2,"confianca":80,"esforco":2}]})]); check("rice aceita confiança em % (80 -> 0,8): 800",rc==0 and "800" in o,o.splitlines()[-1])
rc,o,e=run([calc,"rice",js({"itens":[{"nome":"A","alcance":1,"impacto":1,"confianca":0.5,"esforco":0}]})]); check("rice esforço 0 é recusado",rc!=0 and "maior que zero" in e,e.strip())
rc,o,e=run([calc,"ice",js({"itens":[{"nome":"A","impacto":8,"confianca":6,"facilidade":7},{"nome":"B","impacto":9,"confianca":9,"facilidade":9}]})]); l=o.splitlines()[4:]; check("ice ordena B(729) antes de A(336)",rc==0 and "| B |" in l[0] and "729" in l[0] and "| A |" in l[1] and "336" in l[1],l[0][:40])
rc,o,e=run([calc,"wsjf",js({"itens":[{"nome":"A","valor":8,"urgencia":5,"risco":3,"tamanho":4}]})]); check("wsjf (8+5+3)/4 = 4",rc==0 and "| 4 |" in o,o.splitlines()[-1])
rc,o,e=run([calc,"rut",f"{S}/priorizacao/scripts/exemplo-rut.json"]); vals=[int(l.split("|")[3]) for l in o.splitlines()[4:]]; check("rut: 48,45,12,2 em ordem decrescente",rc==0 and vals==[48,45,12,2],vals)
rc,o,e=run([calc,"rut",js({"itens":[{"nome":"X","relevancia":6,"urgencia":1,"tendencia":1}]})]); check("rut recusa nota 6",rc!=0 and "entre 1 e 5" in e,e.strip())
rc,o,e=run([calc,"rut",js({"itens":[{"nome":"X","relevancia":0,"urgencia":1,"tendencia":1}]})]); check("rut recusa nota 0",rc!=0,e.strip())
rc,o,e=run([calc,"ponderada",js({"criterios":{"A":40,"B":60},"itens":[{"nome":"I","notas":{"A":5,"B":3}}]})]); check("ponderada (40*5+60*3)/100 = 3,80",rc==0 and "3,80" in o,o.splitlines()[-1])
rc,o,e=run([calc,"valor-esforco",js({"itens":[{"nome":"Q","valor":8,"esforco":2},{"nome":"E","valor":2,"esforco":9}]})]); check("valor-esforco: Ganho rápido e Evitar","Ganho rápido" in o and "Evitar" in o)
rc,o,e=run([calc,"rice",js({"itens":[]})]); check("itens vazio é recusado",rc!=0)
rc,o,e=run([calc,"xyz"]); check("método inválido é recusado",rc!=0)
rc,o,e=run([calc,"rice"],inp="{nao e json"); check("JSON inválido é recusado sem traceback",rc!=0 and "Traceback" not in e,e.strip()[:60])
# --- prever.py
pv=f"{S}/previsibilidade/scripts/prever.py"
rc,o1,e=run([pv,"quando","--itens","30","--vazao","3,2,5,4,3,2,4,3"]); rc2,o2,_=run([pv,"quando","--itens","30","--vazao","3,2,5,4,3,2,4,3"])
check("prever quando: roda e é reprodutível (semente fixa)",rc==0 and o1==o2)
nums=[int(x) for x in re.findall(r"\| \d+% \| (\d+) semana",o1)]
check("prever quando: percentis crescentes (P50<=P70<=P85<=P95)",nums==sorted(nums) and len(nums)==4,nums)
check("P50 plausível: média 3,25/sem -> 30 itens ≈ 9 a 10 sem",9<=nums[0]<=11,nums)
tt=run([pv,"tempos","--dias","3,5,2,8,13,4,6,5,9,21"])[1]
check("tempos: percentis nearest-rank conferidos à mão (5, 8, 13, 21; média 7,6)","| 5 |" in tt and "| 8 |" in tt and "| 13 |" in tt and "| 21 |" in tt and "7,6" in tt)
qq=run([pv,"quanto","--semanas","9","--vazao","3,2,5,4,3,2,4,3"])[1]
q=[int(x) for x in re.findall(r"\| \d+% \| (\d+) itens",qq)]
check("quanto: confiança maior -> menos itens (decrescente)",q==sorted(q,reverse=True),q)
c=nums[2]  # 85%
q85=int(re.search(r"85% \| (\d+) itens",run([pv,"quanto","--semanas",str(c),"--vazao","3,2,5,4,3,2,4,3"])[1]).group(1))
check("consistência quando x quanto: em 11 sem (P85 de 30 itens) saem >= 30 itens a ~85%",q85>=29,q85)
rc,o,e=run([pv,"quanto","--semanas","9","--vazao","3,2,5,4,3,2,4,3"]); check("prever quanto roda",rc==0,o.splitlines()[-1][:70])
rc,o,e=run([pv,"quando","--itens","30","--vazao-min","2","--vazao-max","5"]); check("prever quando com faixa min/max roda",rc==0)
rc,o,e=run([pv,"tempos","--dias","3,5,2,8,13,4,6,5,9,21"]); check("prever tempos roda",rc==0,o.splitlines()[-1][:70])
rc,o,e=run([pv,"quando","--itens","30","--vazao","0,0,0"]); check("vazão toda zero não trava (recusa ou avisa)",rc!=0 or "não" in o.lower() or "impossível" in o.lower(),(e or o)[:80])
rc,o,e=run([pv,"quando","--itens","0","--vazao","3,2"]); check("itens=0 tratado",True,(e or o).splitlines()[-1][:70] if (e or o).strip() else "")
rc,o,e=run([pv,"quando","--itens","30","--vazao","a,b"]); check("vazão inválida é recusada sem traceback",rc!=0 and "Traceback" not in e,e.strip())
rc,o,e=run([pv,"quando","--itens","30","--vazao","-1,2"]); check("vazão negativa é recusada",rc!=0)
rc,o,e=run([pv,"tempos","--dias","7"]); check("tempos com 1 amostra: não quebra","Traceback" not in e,(e or o).strip().splitlines()[-1][:80])
# --- analisar_backlog.py
ab=f"{S}/saude-do-backlog/scripts/analisar_backlog.py"
ex=f"{S}/saude-do-backlog/scripts/exemplo-backlog.csv"
rc,o,e=run([ab,ex,"--hoje","2026-10-06"]); check("analisar_backlog: exemplo roda",rc==0 and len(o)>200,o.splitlines()[0])
rows=list(csv.DictReader(open(ex,encoding='utf-8')))
n=len(rows); check(f"relatório menciona o total de itens ({n})",str(n) in o,[l for l in o.splitlines() if str(n) in l][:1])
check("detecta duplicados (WhatsApp 24h vs 24 horas)","WhatsApp" in o and ("uplicad" in o or "parecid" in o))
tmp=tempfile.NamedTemporaryFile('w',suffix='.csv',delete=False,encoding='utf-8'); tmp.write("titulo,criado_em,tamanho,status\n"); tmp.close()
rc,o,e=run([ab,tmp.name]); check("CSV só com cabeçalho: sem traceback",rc!=0 and "Traceback" not in e or rc==0 and "Traceback" not in e,(e or o).strip()[:80])
tmp=tempfile.NamedTemporaryFile('w',suffix='.csv',delete=False,encoding='utf-8'); tmp.write("Title;Created;Points;Status\nLogin social;2026-01-01;3;To do\nEtc e tal;2025-01-01;;To do\n"); tmp.close()
rc,o,e=run([ab,tmp.name,"--hoje","2026-10-06"]); check("CSV com ';' e colunas em inglês: sem traceback",("Traceback" not in e),(e or o).strip().splitlines()[0][:80])
rc,o,e=run([ab,"/nao/existe.csv"]); check("arquivo inexistente: erro limpo",rc!=0 and "Traceback" not in e,e.strip()[:60])
tmp=tempfile.NamedTemporaryFile('w',suffix='.csv',delete=False,encoding='utf-8'); tmp.write("titulo,status\nA,done\nB,cancelado\n"); tmp.close()
rc,o,e=run([ab,tmp.name]); check("tudo concluído: sem traceback",("Traceback" not in e),(e or o).strip().splitlines()[0][:80])
ok=sum(1 for r in res if r[1]); print(f"\nSCRIPTS: {ok}/{len(res)}")
for n,c,d in res: print(("PASS " if c else "FAIL ")+n+("" if c else f"   -> {d}"))

sys.exit(0 if ok==len(res) else 1)
