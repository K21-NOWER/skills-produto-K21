#!/usr/bin/env python3
"""Calcula notas de priorização e imprime uma tabela em Markdown, da maior nota para a menor.

Métodos: rice, ice, wsjf, rut, ponderada, valor-esforco.

Uso:
    python3 calcular.py rice itens.json
    cat itens.json | python3 calcular.py rice

Formato do JSON de entrada (todas as chaves em português, sem acento):

  rice           {"itens": [{"nome": "...", "alcance": 4000, "impacto": 3,
                             "confianca": 0.8, "esforco": 1.5}]}
                 nota = alcance x impacto x confianca / esforco
                 confianca aceita 0.8 ou 80 (valores acima de 1 são tratados como %)

  ice            {"itens": [{"nome": "...", "impacto": 8, "confianca": 6, "facilidade": 7}]}
                 notas de 1 a 10; nota = impacto x confianca x facilidade

  wsjf           {"itens": [{"nome": "...", "valor": 8, "urgencia": 5, "risco": 3, "tamanho": 5}]}
                 custo do atraso = valor + urgencia + risco; nota = custo do atraso / tamanho

  rut            {"itens": [{"nome": "...", "relevancia": 4, "urgencia": 4, "tendencia": 3}]}
                 notas de 1 a 5; Business Value = relevancia x urgencia x tendencia (Matriz RUT, K21)

  ponderada      {"criterios": {"Alinhamento": 40, "Receita": 30, "Facilidade": 30},
                  "itens": [{"nome": "...", "notas": {"Alinhamento": 5, "Receita": 3, "Facilidade": 2}}]}
                 nota = soma(peso x nota) / soma(pesos). Esforço entra como "Facilidade" (nota alta = fácil).

  valor-esforco  {"corte": 5, "itens": [{"nome": "...", "valor": 8, "esforco": 3}]}
                 notas de 1 a 10; ordena por valor / esforço e classifica em quadrantes
                 (corte padrão: 5; acima do corte é "alto").

Só usa a biblioteca padrão do Python.
"""

import json
import sys

METODOS = ("rice", "ice", "wsjf", "rut", "ponderada", "valor-esforco")


def erro(mensagem):
    print(f"Erro: {mensagem}", file=sys.stderr)
    sys.exit(1)


def formatar(valor):
    """Inteiro sem casas; senão, até 2 casas decimais."""
    if isinstance(valor, str):
        return valor
    if abs(valor - round(valor)) < 1e-9:
        return str(int(round(valor)))
    return f"{valor:.2f}".replace(".", ",")


def numero(item, campo, positivo=False):
    nome = item.get("nome", "(sem nome)")
    if campo not in item:
        erro(f'o item "{nome}" não tem o campo "{campo}"')
    valor = item[campo]
    if isinstance(valor, bool) or not isinstance(valor, (int, float)):
        erro(f'o campo "{campo}" do item "{nome}" precisa ser um número')
    if positivo and valor <= 0:
        erro(f'o campo "{campo}" do item "{nome}" precisa ser maior que zero')
    if valor < 0:
        erro(f'o campo "{campo}" do item "{nome}" não pode ser negativo')
    return valor


def nome_do(item):
    if "nome" not in item or not str(item["nome"]).strip():
        erro("todo item precisa de um campo \"nome\"")
    return str(item["nome"])


def tabela(cabecalho, linhas):
    saida = ["| " + " | ".join(cabecalho) + " |", "|" + "|".join("---" for _ in cabecalho) + "|"]
    for linha in linhas:
        saida.append("| " + " | ".join(formatar(c) for c in linha) + " |")
    return "\n".join(saida)


def rice(dados):
    linhas = []
    for item in dados["itens"]:
        alcance = numero(item, "alcance")
        impacto = numero(item, "impacto")
        confianca = numero(item, "confianca")
        esforco = numero(item, "esforco", positivo=True)
        if confianca > 1:
            confianca = confianca / 100
        if confianca > 1:
            erro(f'a confiança do item "{nome_do(item)}" passou de 100%')
        nota = alcance * impacto * confianca / esforco
        linhas.append((nome_do(item), nota, alcance, impacto, f"{formatar(confianca * 100)}%", esforco))
    linhas.sort(key=lambda l: l[1], reverse=True)
    corpo = [(i + 1, *l) for i, l in enumerate(linhas)]
    return "RICE = (Alcance x Impacto x Confiança) / Esforço", tabela(
        ["#", "Item", "Nota RICE", "Alcance", "Impacto", "Confiança", "Esforço"], corpo
    )


def ice(dados):
    linhas = []
    for item in dados["itens"]:
        impacto = numero(item, "impacto")
        confianca = numero(item, "confianca")
        facilidade = numero(item, "facilidade")
        nota = impacto * confianca * facilidade
        media = (impacto + confianca + facilidade) / 3
        linhas.append((nome_do(item), nota, media, impacto, confianca, facilidade))
    linhas.sort(key=lambda l: l[1], reverse=True)
    corpo = [(i + 1, *l) for i, l in enumerate(linhas)]
    return "ICE = Impacto x Confiança x Facilidade (notas de 1 a 10)", tabela(
        ["#", "Item", "Nota ICE", "Média", "Impacto", "Confiança", "Facilidade"], corpo
    )


def wsjf(dados):
    linhas = []
    for item in dados["itens"]:
        valor = numero(item, "valor")
        urgencia = numero(item, "urgencia")
        risco = numero(item, "risco")
        tamanho = numero(item, "tamanho", positivo=True)
        custo = valor + urgencia + risco
        nota = custo / tamanho
        linhas.append((nome_do(item), nota, custo, valor, urgencia, risco, tamanho))
    linhas.sort(key=lambda l: l[1], reverse=True)
    corpo = [(i + 1, *l) for i, l in enumerate(linhas)]
    return "WSJF = Custo do Atraso / Tamanho; Custo do Atraso = Valor + Urgência + Risco ou Oportunidade", tabela(
        ["#", "Item", "WSJF", "Custo do atraso", "Valor", "Urgência", "Risco/Oport.", "Tamanho"], corpo
    )


def rut(dados):
    linhas = []
    for item in dados["itens"]:
        r = numero(item, "relevancia")
        u = numero(item, "urgencia")
        tend = numero(item, "tendencia")
        for nome, valor in (("relevancia", r), ("urgencia", u), ("tendencia", tend)):
            if valor < 1 or valor > 5:
                erro(f'o campo "{nome}" do item "{nome_do(item)}" precisa estar entre 1 e 5')
        linhas.append((nome_do(item), r * u * tend, r, u, tend))
    linhas.sort(key=lambda l: l[1], reverse=True)
    corpo = [(i + 1, *l) for i, l in enumerate(linhas)]
    return "Business Value (RUT) = Relevância x Urgência x Tendência (notas de 1 a 5)", tabela(
        ["#", "Item", "Business Value", "Relevância", "Urgência", "Tendência"], corpo
    )


def ponderada(dados):
    criterios = dados.get("criterios")
    if not isinstance(criterios, dict) or not criterios:
        erro('a matriz ponderada precisa do campo "criterios" com {"nome": peso}')
    soma_pesos = 0
    for nome, peso in criterios.items():
        if isinstance(peso, bool) or not isinstance(peso, (int, float)) or peso < 0:
            erro(f'o peso do critério "{nome}" precisa ser um número maior ou igual a zero')
        soma_pesos += peso
    if soma_pesos <= 0:
        erro("a soma dos pesos precisa ser maior que zero")
    linhas = []
    for item in dados["itens"]:
        notas = item.get("notas")
        if not isinstance(notas, dict):
            erro(f'o item "{nome_do(item)}" precisa do campo "notas"')
        total = 0
        parciais = []
        for nome, peso in criterios.items():
            if nome not in notas:
                erro(f'o item "{nome_do(item)}" não tem nota para o critério "{nome}"')
            nota = notas[nome]
            if isinstance(nota, bool) or not isinstance(nota, (int, float)):
                erro(f'a nota de "{nome}" do item "{nome_do(item)}" precisa ser um número')
            total += peso * nota
            parciais.append(nota)
        linhas.append((nome_do(item), total / soma_pesos, *parciais))
    linhas.sort(key=lambda l: l[1], reverse=True)
    corpo = [(i + 1, *l) for i, l in enumerate(linhas)]
    cabecalho = ["#", "Item", "Nota ponderada"] + [f"{n} ({formatar(p)})" for n, p in criterios.items()]
    return "Nota ponderada = soma(peso x nota) / soma dos pesos", tabela(cabecalho, corpo)


def valor_esforco(dados):
    corte = dados.get("corte", 5)
    linhas = []
    for item in dados["itens"]:
        valor = numero(item, "valor")
        esforco = numero(item, "esforco", positivo=True)
        if valor > corte and esforco <= corte:
            quadrante = "Ganho rápido"
        elif valor > corte:
            quadrante = "Aposta grande"
        elif esforco <= corte:
            quadrante = "Preenchimento"
        else:
            quadrante = "Evitar"
        linhas.append((nome_do(item), valor / esforco, valor, esforco, quadrante))
    linhas.sort(key=lambda l: l[1], reverse=True)
    corpo = [(i + 1, *l) for i, l in enumerate(linhas)]
    return f"Valor / Esforço (notas de 1 a 10; corte entre alto e baixo: {formatar(corte)})", tabela(
        ["#", "Item", "Valor / Esforço", "Valor", "Esforço", "Quadrante"], corpo
    )


FUNCOES = {
    "rice": rice,
    "ice": ice,
    "wsjf": wsjf,
    "rut": rut,
    "ponderada": ponderada,
    "valor-esforco": valor_esforco,
}


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in METODOS:
        erro("uso: calcular.py {" + ",".join(METODOS) + "} [arquivo.json]")
    metodo = sys.argv[1]
    try:
        if len(sys.argv) > 2:
            with open(sys.argv[2], encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
        else:
            dados = json.load(sys.stdin)
    except FileNotFoundError:
        erro(f"arquivo não encontrado: {sys.argv[2]}")
    except json.JSONDecodeError as e:
        erro(f"o JSON de entrada é inválido ({e})")
    if not isinstance(dados, dict) or not isinstance(dados.get("itens"), list) or not dados["itens"]:
        erro('o JSON precisa ter o campo "itens" com pelo menos um item')
    formula, saida = FUNCOES[metodo](dados)
    print(f"**{formula}**\n")
    print(saida)


if __name__ == "__main__":
    main()
