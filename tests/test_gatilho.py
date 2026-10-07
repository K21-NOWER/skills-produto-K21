"""Teste aproximado de acionamento: compara pedidos de alunos com as descrições das skills (proxy lexical, não substitui testar no Claude).

Rode a partir da raiz do repositório: python3 scripts/testar.py
"""
import re,math,pathlib,unicodedata,collections,sys
S=pathlib.Path(__file__).resolve().parent.parent/"plugins"/"produto"/"skills"
def norm(x): return ''.join(c for c in unicodedata.normalize('NFD',x.lower()) if unicodedata.category(c)!='Mn')
STOP=set("de a o e do da em para com um uma os as que por no na se ao dos das mais ou sem como seu sua entre sobre mesmo nao nem ja mas quando use sempre usuario pedir falar skill".split())
def toks(x): 
    ws=re.findall(r"[a-z0-9]+",norm(x)); return [w[:6] for w in ws if w not in STOP and len(w)>2]
desc={}
for d in sorted(S.iterdir()):
    t=(d/"SKILL.md").read_text(encoding="utf-8"); desc[d.name]=re.search(r"description: (.+)",t).group(1)
docs={k:toks(v+" "+k.replace('-',' ')) for k,v in desc.items()}
df=collections.Counter(w for ws in docs.values() for w in set(ws)); N=len(docs)
def score(prompt,k):
    q=collections.Counter(toks(prompt)); d=collections.Counter(docs[k]); n=len(docs[k])**0.5
    return sum(q[w]*(1+math.log(d[w]))*math.log(1+N/df[w]) for w in q if w in d)/n
P={ # 3 pedidos naturais por skill, no jeito que aluno escreve
"user-story":["Avalia essa história: Como usuário, quero gerenciar meus pedidos, para ter mais controle","Preciso escrever os critérios de aceitação dessa funcionalidade de cadastro","Essa story está grande demais? Precisa fatiar?"],
"visao-do-produto":["Escreve a visão do meu app de delivery para pequenos restaurantes","Monta o vision board e o posicionamento do produto","Dá uma nota para a visão do nosso produto"],
"priorizacao":["Tenho 8 ideias e só 6 pessoas-mês, me ajuda a decidir o que fazer primeiro com RICE","Qual método uso para ordenar essas iniciativas? Quero comparar RICE e ICE","Aplica a Matriz RUT nesta lista de itens"],
"hipoteses":["Acho que lembrete por WhatsApp reduz faltas. Como testo isso?","Monta um Test Card para essa hipótese","Quero um experimento barato para validar essa ideia antes de construir"],
"metricas-de-produto":["Quais métricas devo acompanhar no meu app de assinatura?","Qual é a minha North Star Metric?","Como calculo churn e retenção?"],
"udd-fatiamento":["Quero lançar um marketplace. Como começo pequeno e deixar o uso guiar o que construir?","Qual é o epicentro do meu produto e como fatio o MVP?","Explica o Padrão 1-2-N e UDD"],
"okr":["Escreve meus OKRs do trimestre","Meus key results são todos tarefas, o que está errado?","Como faço um check-in de OKR que funcione?"],
"saude-do-backlog":["Meu backlog tem 300 itens e ninguém mexe, como limpo?","Chegou uma demanda nova de um stakeholder, descarto ou coloco na prateleira?","Analisa esse CSV do backlog e diz se está saudável"],
"previsibilidade":["Temos 40 itens no backlog, quando fica pronto?","Quantos itens conseguimos entregar até 15 de dezembro? Entregamos 3, 4 e 2 por semana","O que é cycle time e como calculo o percentil 85?"],
"papel-de-produto":["Sou PO há 6 meses e não sei se estou fazendo certo, me ajuda a me avaliar","Qual a diferença entre PO, PM e gerente de projetos?","Quero um plano de evolução de carreira para GPM"],
"discovery-com-clientes":["Preciso montar um roteiro de entrevista com clientes que cancelaram","Fiz 5 entrevistas, me ajuda a sintetizar as notas","Monta um mapa de empatia e uma persona a partir dessas conversas"],
"estrategia-e-roadmap":["Meu roadmap é uma lista de funcionalidades com datas, como melhoro?","Preencher o Tanque de Decantação do meu produto","Monta a estratégia de produto do próximo ano"],
"apresentacao-de-produto":["Monta a Sprint Review da semana para os stakeholders","Preciso de um elevator pitch do produto","Como apresento resultados de métricas sem enrolar?"],
"riscos-e-vieses":["Faz um pré-mortem do lançamento do mês que vem","Acho que estou com viés de confirmação nessa decisão, me ajuda","Quais riscos tem nessa iniciativa e qual a probabilidade e impacto?"],
}
tot=0;ok=0;erros=[]
for esperado,ps in P.items():
    for p in ps:
        sc=sorted(((score(p,k),k) for k in docs),reverse=True)
        tot+=1
        if sc[0][1]==esperado: ok+=1
        else: erros.append((esperado,p[:60],sc[0][1],sc[1][1] if sc[1][1]!=esperado else '(2º)'))
print(f"GATILHO (proxy lexical, 42 pedidos): top-1 correto = {ok}/{tot}")
for e in erros: print(" errou:",e)

sys.exit(0 if ok>=tot-2 else 1)
