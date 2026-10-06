# Rubrica de avaliação de previsões e promessas de prazo

Use este arquivo para pontuar. Escolha a faixa pelos sinais que o material realmente mostra. Se não há evidência, a nota não sobe.

| Critério (peso) | 90-100 | 70-89 | 40-69 | 0-39 |
|---|---|---|---|---|
| **1. Intervalo probabilístico (20)** Dá faixa e chance? | Intervalo com probabilidade ("85% até X") e leitura do risco restante | Faixa de datas, sem probabilidade explícita | Data única com "margem" informal | Data exata como se fosse certa |
| **2. Base em dados históricos (20)** Vem do histórico real? | Calculada sobre vazão ou tempos reais do time (simulação ou percentis) | Baseada em média do histórico | Baseada em estimativa de esforço convertida em dias | Palpite ou desejo ("precisa ser até dezembro") |
| **3. Amostra (14)** Dados bons e suficientes? | 8 ou mais períodos, definição consistente, inclui zeros e variações | 5 a 7 períodos, definições razoáveis | Poucos períodos ou definição mudou no meio | Sem dados, ou dados de outro time e contexto |
| **4. Premissas explícitas (14)** Diz o que precisa ser verdade? | Escopo, capacidade, dependências e mudanças de time declarados | Algumas premissas citadas | Premissas implícitas | Nenhuma; promessa "com escopo aberto" |
| **5. Revisão e sensibilidade (10)** Atualiza? | Revisão a cada ciclo, com gatilhos (mudou escopo ou ritmo) | Revisão eventual | Só no início | Congelada |
| **6. Pergunta certa (12)** Foca no que importa? | Complementa com primeira versão, frequência de entrega, prioridade e ponto de parada | Cita frequência de entrega | Só "quando termina tudo" | Escopo fechado como pré-condição |
| **7. Comunicação (10)** Clara e honesta? | Linguagem de probabilidade, riscos e opções para o stakeholder | Clara, com riscos genéricos | Técnica demais ou otimista demais | Esconde incerteza |

## Referências de calibração

- "Entregamos o MVP em 15 de dezembro": intervalo 15, base 30, premissas 20.
- "Com 85% de probabilidade, entre 21 e 28 de dezembro, com base nas últimas 8 semanas; reviso a cada sprint": intervalo 90, base 85, amostra 70, revisão 85.

## Sinais de alerta

- Conversão fixa de pontos em dias.
- Data decidida antes de olhar o histórico.
- "Escopo fechado" com data fixa e sem plano de corte.
