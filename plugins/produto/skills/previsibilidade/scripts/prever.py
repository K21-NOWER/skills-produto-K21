#!/usr/bin/env python3
"""Previsão probabilística de entrega (simulação de Monte Carlo) e percentis de tempos de ciclo.

Respostas são sempre intervalos de probabilidade baseados no histórico informado, nunca datas exatas.

Uso:
  Quando termina um backlog de N itens, dado o histórico de itens entregues por semana:
    python3 prever.py quando --itens 50 --vazao 3,2,5,4,3,2,4,3 [--inicio 2026-10-12]

  Quantos itens saem em S semanas:
    python3 prever.py quando --itens 50 --vazao-min 2 --vazao-max 5     (sem histórico detalhado)
    python3 prever.py quanto --semanas 8 --vazao 3,2,5,4,3,2,4,3

  Percentis dos tempos de entrega (lead time ou cycle time) de itens já concluídos, em dias:
    python3 prever.py tempos --dias 3,5,2,8,13,4,6,5,9,21

Opções comuns: --simulacoes 10000 (padrão) e --semente 42 (resultado reproduzível).
Com --vazao a simulação sorteia semanas do próprio histórico (com reposição). Com --vazao-min e
--vazao-max sorteia um inteiro entre os dois valores, com a mesma chance para todos.
Só usa a biblioteca padrão do Python.
"""

import argparse
import random
import sys
from datetime import date, datetime, timedelta

PERCENTIS_PRAZO = (50, 70, 85, 95)
LIMITE_SEMANAS = 520


def erro(msg):
    print(f"Erro: {msg}", file=sys.stderr)
    sys.exit(1)


def lista(texto, nome, inteiros=False):
    try:
        valores = [float(x) for x in texto.replace(";", ",").split(",") if x.strip() != ""]
    except ValueError:
        erro(f"{nome} precisa ser uma lista de números separados por vírgula")
    if not valores:
        erro(f"{nome} não pode ser vazio")
    if any(v < 0 for v in valores):
        erro(f"{nome} não pode ter números negativos")
    return [int(v) for v in valores] if inteiros else valores


def percentil(ordenados, p):
    k = max(0, min(len(ordenados) - 1, int(round(p / 100 * (len(ordenados) - 1)))))
    return ordenados[k]


def sorteador(args):
    if args.vazao:
        historico = lista(args.vazao, "--vazao", inteiros=True)
        if sum(historico) == 0:
            erro("o histórico de vazão só tem zeros; não há como prever")
        return (lambda rnd: rnd.choice(historico)), historico
    if args.vazao_min is not None and args.vazao_max is not None:
        if args.vazao_min < 0 or args.vazao_max < args.vazao_min or args.vazao_max == 0:
            erro("--vazao-min e --vazao-max precisam ser inteiros, com 0 <= min <= max e max > 0")
        return (lambda rnd: rnd.randint(args.vazao_min, args.vazao_max)), None
    erro("informe --vazao (histórico) ou --vazao-min e --vazao-max")


def data_inicial(texto):
    if not texto:
        return date.today()
    try:
        return datetime.strptime(texto, "%Y-%m-%d").date()
    except ValueError:
        erro("--inicio precisa estar no formato AAAA-MM-DD")


def avisos_amostra(historico):
    avisos = []
    if historico is None:
        avisos.append("Sem histórico detalhado: a simulação usa só o mínimo e o máximo. Trate o resultado como indicação grosseira.")
    elif len(historico) < 8:
        avisos.append(f"Amostra pequena ({len(historico)} semanas): o intervalo real é mais largo do que o mostrado.")
    return avisos


def cmd_quando(args):
    if args.itens is None or args.itens <= 0:
        erro("--itens precisa ser maior que zero")
    sorteia, historico = sorteador(args)
    rnd = random.Random(args.semente)
    inicio = data_inicial(args.inicio)
    semanas_por_rodada = []
    for _ in range(args.simulacoes):
        restante, semanas = args.itens, 0
        while restante > 0 and semanas < LIMITE_SEMANAS:
            restante -= sorteia(rnd)
            semanas += 1
        semanas_por_rodada.append(semanas)
    ordenados = sorted(semanas_por_rodada)
    print(f"**Quando termina?** {args.itens} itens, {args.simulacoes} simulações, semente {args.semente}\n")
    print("| Probabilidade | Termina em até | Data (a partir de {})".format(inicio.strftime("%d/%m/%Y")) + " |")
    print("|---|---|---|")
    for p in PERCENTIS_PRAZO:
        s = percentil(ordenados, p)
        fim = inicio + timedelta(days=7 * s)
        print(f"| {p}% | {s} semana(s) | {fim.strftime('%d/%m/%Y')} |")
    print(f"\nLeitura: com 85% de probabilidade, os {args.itens} itens terminam em até {percentil(ordenados, 85)} semanas, e há 15% de chance de passar disso.")
    for aviso in avisos_amostra(historico):
        print(f"\nAtenção: {aviso}")
    print("\nPremissas: escopo estável e ritmo de entrega parecido com o histórico. Se algo disso mudar, simule de novo.")


def cmd_quanto(args):
    if args.semanas is None or args.semanas <= 0:
        erro("--semanas precisa ser maior que zero")
    sorteia, historico = sorteador(args)
    rnd = random.Random(args.semente)
    totais = []
    for _ in range(args.simulacoes):
        totais.append(sum(sorteia(rnd) for _ in range(args.semanas)))
    ordenados = sorted(totais)
    print(f"**Quantos itens em {args.semanas} semana(s)?** {args.simulacoes} simulações, semente {args.semente}\n")
    print("| Confiança | Entrega pelo menos |")
    print("|---|---|")
    for confianca in PERCENTIS_PRAZO:
        itens = percentil(ordenados, 100 - confianca)
        print(f"| {confianca}% | {itens} itens |")
    print(f"\nLeitura: com 85% de confiança, saem pelo menos {percentil(ordenados, 15)} itens em {args.semanas} semanas; a mediana é {percentil(ordenados, 50)}.")
    for aviso in avisos_amostra(historico):
        print(f"\nAtenção: {aviso}")


def cmd_tempos(args):
    dias = lista(args.dias, "--dias")
    if len(dias) < 5:
        print("Atenção: menos de 5 itens concluídos; os percentis dizem pouco.\n")
    ordenados = sorted(dias)
    print(f"**Tempos de entrega de {len(dias)} itens concluídos (dias)**\n")
    print("| Medida | Dias |")
    print("|---|---|")
    for p in PERCENTIS_PRAZO:
        print(f"| Percentil {p} | {percentil(ordenados, p):g} |")
    print(f"| Média | {sum(dias) / len(dias):.1f} |")
    print(f"| Mínimo / máximo | {min(dias):g} / {max(dias):g} |")
    print(f"\nExpectativa de nível de serviço (SLE) sugerida: 85% dos itens em até {percentil(ordenados, 85):g} dias.")
    print("Observação: use a mesma definição de início e fim para todos os itens (por exemplo, do compromisso à entrega).")


def main():
    ap = argparse.ArgumentParser(description="Previsão probabilística de entrega")
    sub = ap.add_subparsers(dest="comando", required=True)

    def comuns(p):
        p.add_argument("--vazao", help="itens entregues por semana, separados por vírgula (histórico)")
        p.add_argument("--vazao-min", type=int, help="mínimo de itens por semana (sem histórico detalhado)")
        p.add_argument("--vazao-max", type=int, help="máximo de itens por semana (sem histórico detalhado)")
        p.add_argument("--simulacoes", type=int, default=10000)
        p.add_argument("--semente", type=int, default=42)

    q = sub.add_parser("quando", help="em quantas semanas termina um backlog")
    comuns(q)
    q.add_argument("--itens", type=int)
    q.add_argument("--inicio", help="AAAA-MM-DD (padrão: hoje)")
    q.set_defaults(func=cmd_quando)

    n = sub.add_parser("quanto", help="quantos itens saem em um número de semanas")
    comuns(n)
    n.add_argument("--semanas", type=int)
    n.set_defaults(func=cmd_quanto)

    t = sub.add_parser("tempos", help="percentis de tempos de entrega, em dias")
    t.add_argument("--dias", required=True)
    t.set_defaults(func=cmd_tempos)

    args = ap.parse_args()
    if getattr(args, "simulacoes", 1) <= 0:
        erro("--simulacoes precisa ser maior que zero")
    args.func(args)


if __name__ == "__main__":
    main()
