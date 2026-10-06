---
name: okr
description: Avalia, escreve e acompanha OKRs (Objectives and Key Results) com nota de 0 a 100 por critério (objetivo, KRs de resultado e não tarefa, formato de X para Y, equilíbrio, indicadores antecedentes, conexão com a estratégia e o propósito do cliente com Fit for Purpose, foco, ambição e governança), diagnostica as 10 disfunções mais comuns, separa OKR de BAU e KPI e prepara check-ins que funcionam. Use sempre que o usuário falar de OKR, objetivo e resultado-chave, KR, check-in de OKR, "meus KRs são tarefas?", OKR x KPI, OKR e bônus, desdobrar OKR estratégico em tático, ou colar objetivos e metas de um ciclo para revisar, mesmo sem citar a sigla.
---

# OKR: avaliar, escrever e acompanhar

OKR conecta a estratégia da organização ao trabalho dos times, e é sobretudo uma ferramenta de **mudança cultural**: sai a cultura de entrega de tarefas, visão individual e baixo comprometimento com o resultado, entra o foco em resultado, o senso de dono e a colaboração. Como toda ferramenta, é meio, não fim. Quando OKR falha, quase sempre o problema não está na ferramenta, e sim nas disfunções que ela expõe.

Esta skill avalia OKRs, escreve OKRs bons a partir do problema e da estratégia, e ajuda a conduzir o acompanhamento. Os modos usam a mesma régua.

## Escolha o modo

- **Avaliar**: o usuário traz objetivos e KRs de um ciclo. Pedidos como "dá uma nota", "meus KRs estão bons?".
- **Criar**: traz estratégia, problema ou área e quer OKRs. Pedidos como "monta os OKRs do trimestre", "desdobra esse objetivo em KRs".
- **Check-in**: quer conduzir ou preparar um check-in. Veja `references/checkin-e-disfuncoes.md`.
- **Diagnosticar**: quer saber por que o OKR da empresa não está funcionando. Use as 10 disfunções.
- **Avaliar e melhorar** (o mais comum): traz OKRs fracos e quer a versão boa.

Responda no idioma do usuário (padrão: português do Brasil), com tom de mentor.

## Conceitos que sustentam a rubrica

- **Objetivo** é qualitativo, descreve um problema ou uma oportunidade, e funciona como "um inimigo em comum". Não implica solução predefinida.
- **Resultado-chave (KR)** é quantitativo, acionável, com frequência de medição adequada ao ciclo. O formato clássico é **Aumentar, Diminuir ou Alcançar de X para Y**.
- **KR não é tarefa.** "Entregar o projeto tal antes da data tal" é tarefa. Pergunte: "ok, e que métrica melhora porque entregamos este projeto?" Geralmente essa é o KR. Projeto como KR leva a entregar uma solução que pode não gerar impacto, e troca o senso de dono pelo senso de compliance ("eu fiz a minha parte").
- **Prefira indicadores antecedentes (leading).** OKR aponta para o futuro desejado; indicador que só olha o passado impede corrigir a rota dentro do ciclo.
- **Equilíbrio.** Um KR só distorce: um OKR de vendas sem KR de satisfação empurra leads ruins e serviços que o cliente não precisa. KRs demais (15 para um objetivo) matam o foco. Equilibre eficácia com eficiência e com saúde do negócio (churn, turnover, fraude).
- **Fit for Purpose (F4P).** Conecte a estratégia ao **propósito do cliente**: mapeie por que o cliente procura o produto e escolha objetivos nos propósitos que a concorrência não atende bem, em vez de copiar o que ela faz bem. Os critérios de adequação (as métricas pelas quais o cliente escolhe você) viram KRs.
- **OKR não é BAU.** Business as usual (operação do dia a dia) se acompanha com KPIs de saúde, olhando o desempenho passado. OKR é para inovação, mudança, expansão ou melhoria em áreas-chave. Nem tudo precisa estar nos OKRs, e nem toda área precisa se ver em todos os objetivos: OKR é, acima de tudo, um instrumento de priorização.
- **Níveis e ciclos.** Estratégico: até 1 ano, responsabilidade do C-level. Tático: até 3 meses, responsabilidade compartilhada.
- **OKR não é meta nem bônus.** Meta ligada a bônus gera motivação extrínseca, competição e comportamento tóxico; OKR busca motivação intrínseca, pensamento sistêmico e colaboração.

## Modo avaliar

1. Leia `references/rubrica.md`.
2. Pontue os 9 critérios de 0 a 100, citando trechos dos OKRs.
3. Nota geral = soma de (nota x peso) dividida por 100. **Teto de bloqueio:** se qualquer critério ficar abaixo de 40, a nota geral não passa de 69.
4. Faixas: 85 a 100 Pronto para o ciclo; 70 a 84 Quase lá; 50 a 69 Precisa de refinamento; 0 a 49 Reescrever.

| # | Critério | Peso |
|---|---|---|
| 1 | Objetivo (qualitativo, problema ou oportunidade) | 14 |
| 2 | KRs de resultado, não tarefa | 20 |
| 3 | Formato mensurável (de X para Y, baseline e alvo) | 10 |
| 4 | Equilíbrio entre KRs | 12 |
| 5 | Indicadores antecedentes e frequência | 8 |
| 6 | Conexão com estratégia e propósito do cliente | 12 |
| 7 | Foco e quantidade (e separação do BAU) | 10 |
| 8 | Ambição e aprendizado | 6 |
| 9 | Governança (nível, ciclo, líder, check-in) | 8 |

Calibre com rigor: OKRs escritos pela primeira vez costumam ficar entre 30 e 65. Reserve 90 ou mais para OKRs que você levaria ao ciclo sem mudar.

### Formato de saída

```
## Avaliação dos OKRs: [área ou ciclo]

**Nota geral: NN/100** (faixa)

### 1. Notas por critério
| Critério (peso) | Nota | Por quê (evidência) | Como melhorar |
|---|---|---|---|

### 2. O que mais pesa
### 3. OKRs melhorados
**Objetivo:** ...
| KR | Tipo (resultado, equilíbrio, antecedente) | De X para Y | Baseline | Alvo |
|---|---|---|---|---|
### 4. Disfunções percebidas
(das 10, só as que aparecem)
### 5. Perguntas e suposições
```

Se o usuário pedir só a nota, entregue as seções 1 e 2. Onde faltar dado, escreva a suposição entre colchetes; não invente números.

## Modo criar

1. **Entenda a estratégia e o cliente.** Qual problema ou oportunidade, para quem, e que propósito do cliente (F4P) queremos atender melhor. Declare suposições em vez de interrogar.
2. **Escreva 1 a 3 objetivos** qualitativos, no nível certo (estratégico ou tático). Se a meta parecer ousada demais, fatie ("nenhuma doença simples ficará sem tratamento").
3. **Para cada objetivo, derive os KRs:** o que de fato mudaria se o objetivo fosse atingido? Prefira antecedentes, escreva de X para Y e inclua 1 ou 2 KRs de equilíbrio (eficiência, saúde do negócio).
4. **Retire os "tarefeiros":** para cada KR que seja entrega, pergunte que métrica melhora com ela e use essa métrica.
5. **Separe o que é BAU** (vai para KPI) e o que não precisa estar nos OKRs.
6. **Defina governança:** líder de cada OKR, champion (facilitador), cadência de check-in e como o painel fica visível.
7. **Autoavalie** e reescreva o que ficar abaixo de 80.

## Princípios

- OKR muda cultura, e o check-in é onde a mudança acontece: manter a regularidade vale tanto quanto escrever os OKRs.
- KR descreve sucesso. Se descreve entrega, o time entrega e o resultado não vem.
- Poucos objetivos, KRs equilibrados, nada de OKR para tudo.

Para as métricas dos KRs, use `metricas-de-produto`. Para transformar um KR em experimento, use `hipoteses`. Para a estratégia por trás do objetivo, use `estrategia-e-roadmap`. Para ver uma avaliação completa, leia `references/exemplo.md`.
