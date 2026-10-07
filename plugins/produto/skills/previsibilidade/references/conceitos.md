# Conceitos: estimativa, Monte Carlo, tempos e fluxo

Conteúdo: Por que estimar (os 5 Ps) · Como estimar · Cuidados · Por que não converter esforço em tempo · Monte Carlo em poucas linhas · Lead time, cycle time e Lei de Little · Lendo um CFD

## Por que estimar (os 5 Ps)

1. **Previsibilidade:** prever quando a entrega será possível e o que provavelmente ela conterá.
2. **Produtividade:** entender se estamos entregando mais ou menos ao longo do tempo.
3. **Priorização:** o esforço é o denominador do retorno sobre o investimento. Quanto menor o esforço, maior o ROI.
4. **Particionamento:** quando o time estima, indica ao PO itens grandes demais (épicos), que devem ser fatiados antes de entrar no fluxo.
5. **Partilha:** a conversa técnica alinha o que será feito e evita itens que não conversam entre si.

Estimar não gera valor direto ao produto: se o time perde muito tempo estimando, algo está errado.

## Como estimar

A pior forma é pessoa-hora. A mais comum na agilidade é o Planning Poker com a sequência de Fibonacci (story points); uma alternativa leve é o T-Shirt Size (P, M, G). Se o time já tem métricas de fluxo, como Customer Lead Time e vazão, elas respondem "quando fica pronto?" com folga e a estimativa vira apoio para particionar e priorizar.

## Cuidados

- **Não é assertiva.** Há sempre margem de erro.
- **Consenso, não unanimidade.** Buscar que todos concordem exatamente é irrealista. A maioria decide, e quem discorda precisa conviver com a decisão.
- **Não perca muito tempo.**
- **Quem estima é quem faz,** e a estimativa é do item, não da pessoa.

## Por que não converter esforço em tempo

Planilhas que dizem "tamanho P equivale a X dias" quase nunca funcionam, porque o esforço é só uma das variáveis que influenciam o tempo. Pesam mais: o **tipo de demanda** (erro, melhoria, criação), o **fluxo do trabalho**, as **dependências externas** e a **classe de serviço** (prioridade). Para falar de prazo, use tempos reais de entrega ou a simulação.

## Monte Carlo em poucas linhas

Monte Carlo usa amostragem aleatória massiva para obter resultados numéricos em situações de grande incerteza. Para prazo:

1. Informe o histórico (por exemplo, itens entregues por semana nas últimas 12 semanas) e o tamanho do backlog.
2. A simulação "joga" milhares de vezes: a cada semana sorteia uma vazão do histórico e desconta do backlog, até acabar.
3. O resultado é uma distribuição: em quantas semanas terminou em cada rodada. Os percentis viram a resposta ("85% das rodadas terminaram em até 17 semanas").

Serve também para custo e para "quantos itens saem até a data". O script `scripts/prever.py` implementa isso com sorteio do próprio histórico. Limites: sem histórico, a resposta é incipiente; a previsão vale enquanto o ritmo e o escopo forem parecidos.

## Lead time, cycle time e Lei de Little

- **Customer Lead Time:** da solicitação do cliente à entrega. É a expectativa dele; por isso é maior que o cycle time.
- **Cycle time** (engenharia de produção): tempo líquido de trabalho no item. No jargão ágil, às vezes é usado para "tempo em uma etapa do fluxo"; a Kanban University chama isso de lead time da etapa. Escolha uma definição e explicite.
- **Vazão (throughput):** itens entregues por período.
- **Lei de Little:** itens em andamento (em média) = vazão x lead time. Se o lead time está alto e a vazão não muda, há itens demais em andamento.
- **SLE (service level expectation):** "85% dos itens em até N dias", calculado pelo percentil dos tempos reais.

## Lendo um CFD (Cumulative Flow Diagram)

O CFD mostra, ao longo do tempo, quantos itens acumulados estão em cada estado do fluxo.

- **Linhas paralelas e estáveis:** fluxo saudável.
- **Faixa que se alarga:** acúmulo naquele estado (gargalo ou excesso de trabalho em andamento).
- **Linha de entregues achatada:** nada está saindo.
- **Distância horizontal** entre a entrada e a saída em um ponto é aproximadamente o lead time; a **vertical** é o trabalho em andamento.
- **Linha de chegada que sobe mais rápido que a de entrega:** a demanda cresce mais que a capacidade.
