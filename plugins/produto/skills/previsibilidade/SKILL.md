---
name: previsibilidade
description: Responde "quando fica pronto?" e "quanto cabe até a data?" com previsão probabilística, usando simulação de Monte Carlo (script incluso) sobre o histórico de entregas do time, calcula percentis de lead time e cycle time para definir expectativas de nível de serviço, ensina a ler fluxo (Lei de Little, CFD) e avalia promessas de prazo com nota de 0 a 100. Explica estimativa de esforço (os 5 Ps), T-Shirt e Planning Poker e por que não converter pontos em dias. Use sempre que o usuário perguntar "quando fica pronto?", prazo de entrega, previsão, forecasting, Monte Carlo, vazão, throughput, lead time, cycle time, CFD, estimativa, Planning Poker, story points, "o chefe quer uma data", ou quiser revisar um prazo prometido, mesmo sem citar esses termos.
---

# Previsibilidade: responder "quando fica pronto?" sem mentir

"Quando fica pronto?" é uma pergunta válida e vamos ouvi-la sempre. Esta skill ensina a respondê-la do jeito honesto: com um **intervalo de probabilidade** construído sobre o histórico real do time, e não com uma data inventada. Também ajuda a trocar a pergunta por outras mais úteis.

## As regras do jogo (K21)

1. **Toda estimativa é uma estimativa, não uma assertiva.** Sempre há margem de erro.
2. **Toda previsão é, no máximo, uma distribuição de probabilidades baseada nos dados históricos disponíveis.** Sem histórico, a previsão é incipiente.
3. **As perguntas que dá para responder dependem dos dados que existem.** Sem dados sobre a performance do time, nem Monte Carlo nem inteligência artificial conseguem responder sobre ela.
4. **A resposta nunca é exata** ("termina em 25/08 com custo de R$ 132.456,67"). É sempre um intervalo probabilístico: "com 85% de probabilidade, termina entre as últimas semanas de agosto e o início de setembro". Qualquer previsão fora desse formato é mentirosa.

## Escolha o modo

- **Prever**: o usuário traz o tamanho do backlog e o histórico de entregas e quer prazo (ou quanto cabe até uma data). Pedidos como "quando fica pronto?", "quantos itens saem até dezembro?".
- **Avaliar uma previsão**: traz uma data prometida ou um plano e quer saber se é honesto. Pedidos como "esse prazo faz sentido?".
- **Ler o fluxo**: traz tempos de entrega, quadro ou CFD e quer entender. Pedidos como "qual o nosso lead time?", "o que esse CFD diz?".
- **Estimar**: quer ajuda com estimativa de esforço. Veja `references/conceitos.md`.

Responda no idioma do usuário (padrão: português do Brasil), com tom de mentor.

## Modo prever

1. **Levante os dados:** itens entregues **por semana** nas últimas 8 a 12 semanas (inclua as semanas com zero), tamanho do backlog em itens (itens de tamanho parecido, depois de fatiar) e data de início. Pergunte também se o escopo ainda cresce.
2. **Rode a simulação.** Se puder executar código: `python3 ${CLAUDE_SKILL_DIR}/scripts/prever.py quando --itens 50 --vazao 3,2,5,4,3,2,4,3 --inicio 2026-10-12`. Para "quantos itens até a data": `prever.py quanto --semanas 8 --vazao ...`. Sem histórico detalhado, use `--vazao-min` e `--vazao-max` e avise que é grosseiro. No chat do claude.ai, use o caminho relativo `scripts/prever.py`. A semente fixa torna o resultado reproduzível.
3. **Sem execução de código**, não finja precisão: dê uma faixa grosseira (itens ÷ vazão máxima até itens ÷ vazão mínima) e diga que é uma faixa de extremos, não uma probabilidade.
4. **Responda em intervalo:** "Com 85% de probabilidade, os 50 itens terminam em até 17 semanas (até 08/02); há 15% de chance de passar disso." Mostre também a mediana, para o usuário ver a diferença entre o provável e o seguro.
5. **Avise as premissas:** escopo estável, ritmo parecido com o histórico, sem grandes mudanças de time. Se mudarem, simule de novo.
6. **Sugira as perguntas melhores** (veja abaixo) e ofereça atualizar a previsão a cada ciclo.

### Formato de saída (prever)

```
## Previsão: [time ou produto]

**Dados usados:** [n itens, n semanas de histórico, início]

### Resposta
(tabela do script e a frase em formato de intervalo)

### Como ler
(mediana x 85%, o que é o risco dos 15%)

### Premissas e riscos
### Perguntas melhores que "quando fica pronto?"
```

## Modo avaliar uma previsão

Leia `references/rubrica.md`. Pontue os 7 critérios de 0 a 100, com evidência; nota geral = soma de (nota x peso) dividida por 100; **teto de bloqueio:** se qualquer critério ficar abaixo de 40, não passa de 69. Faixas: 85 a 100 Honesta e útil; 70 a 84 Quase lá; 50 a 69 Precisa de dados; 0 a 49 Reescrever.

| # | Critério | Peso |
|---|---|---|
| 1 | Intervalo probabilístico | 20 |
| 2 | Base em dados históricos | 20 |
| 3 | Qualidade e tamanho da amostra | 14 |
| 4 | Premissas explícitas | 14 |
| 5 | Revisão e sensibilidade | 10 |
| 6 | Pergunta certa | 12 |
| 7 | Comunicação | 10 |

Entregue: nota no topo, tabela por critério com evidência, o que mais pesa, **previsão reescrita** (rode o script se houver dados) e perguntas. Calibre com rigor: promessas de prazo comuns ficam entre 20 e 50.

## Modo ler o fluxo

- **Lead time e cycle time.** Customer Lead Time é o tempo desde que o cliente fez o pedido até a entrega (a expectativa dele, que inclui o tempo no backlog). Cycle time, no sentido da engenharia de produção, é o tempo de trabalho no item, do início da construção à entrega. O Customer Lead Time é sempre maior. Defina uma vez qual medir e use a mesma definição para todos os itens.
- **Percentis em vez de média:** `prever.py tempos --dias 3,5,2,8,...` devolve os percentis e uma **expectativa de nível de serviço (SLE)**, como "85% dos itens em até 13 dias".
- **Lei de Little:** em média, itens em andamento = vazão x lead time. Para reduzir o lead time, reduza o trabalho em andamento.
- **CFD (Cumulative Flow Diagram):** faixas que se alargam indicam acúmulo (gargalo ou excesso de itens em andamento); a distância horizontal entre as linhas é o lead time e a vertical é o trabalho em andamento. Veja `references/conceitos.md`.

## Perguntas melhores que "quando fica pronto?"

- Quando a primeira versão entra no ar?
- Com que frequência atualizamos o produto?
- Estamos entregando o mais importante a cada versão?
- Qual o ponto mais cedo em que podemos parar o projeto?
- Qual é o nosso lead time?

É a analogia do avião e do metrô: no avião, perder o voo custa um ano e por isso se pede tudo no início. No metrô sai um a cada 6 minutos: pergunta-se a frequência, quantos passageiros leva e se os mais importantes vão primeiro. Com entregas frequentes, a necessidade de planejar tudo antes diminui.

Para fatiar o backlog em itens de tamanho parecido, use `user-story` ou `udd-fatiamento`. Para tratar o backlog que alimenta a previsão, use `saude-do-backlog`. Para ver um exemplo, leia `references/exemplo.md`.
