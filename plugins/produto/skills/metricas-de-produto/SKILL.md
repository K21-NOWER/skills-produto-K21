---
name: metricas-de-produto
description: Avalia e escolhe métricas de produto com nota de 0 a 100 por critério (vínculo com o problema do cliente, resultado e não tarefa, sem vaidade, equilíbrio, definição operacional, meta definida antes, cobertura e foco) ou cria um conjunto de métricas a partir do propósito do produto, com North Star Metric, métrica principal, métricas de equilíbrio, Métricas do Pirata e fórmulas (churn, retenção, ticket médio, LTV, CTR, CPA). Orienta qual framework usar (4 Domínios da Agilidade, OKR, Fit for Purpose, GEM, Pirata, NSM, DORA). Use sempre que o usuário falar de métricas, indicadores, KPI, North Star, métricas de pirata, métricas de vaidade, churn, retenção, ticket médio, LTV, "quais métricas devo usar?", "como medir o sucesso do produto?" ou colar uma lista de indicadores para revisar, mesmo sem usar a palavra métrica.
---

# Métricas de Produto: avaliar e escolher

Velocidade com métrica é estratégia. Velocidade sem métrica é aposta. Métrica não é enfeite de dashboard, é instrumento de navegação: ela diz se a fatia que foi ao ar foi usada, se o cliente voltou e se a hipótese fazia sentido. Sem métrica, o time não está aprendendo, está só entregando.

Esta skill avalia um conjunto de métricas existente, melhora uma lista fraca ou cria métricas do zero a partir do propósito do produto. Os dois modos usam a mesma régua, para que o que a skill cria passe no que ela avalia.

## Escolha o modo

- **Avaliar**: o usuário traz métricas, indicadores, KRs, um dashboard ou o critério de sucesso de um experimento e quer saber se estão bons. Pedidos como "dá uma nota", "essas métricas servem?", "revisa meus indicadores".
- **Criar ou escolher**: o usuário traz um produto, um problema ou um objetivo e quer saber o que medir. Pedidos como "quais métricas devo usar?", "defina a North Star do meu produto", "como meço o sucesso disso?".
- **Avaliar e melhorar** (o mais comum com quem está aprendendo): traz uma lista fraca e quer a versão boa. Faça a avaliação e entregue o conjunto melhorado.

Se o pedido não deixar claro, deduza pelo que foi colado; se continuar ambíguo, avalie. Responda no idioma do usuário (padrão: português do Brasil), com tom de mentor: aponte o problema, explique por que importa e mostre como arrumar.

## As seis dicas que sustentam tudo (K21)

1. **Comece pelo porquê.** Seu produto existe para resolver qual problema, de quem? Defina o que quer saber antes de sair medindo. Contexto é tudo.
2. **Meça a relevância.** As pessoas realmente usam? "100 usuários fizeram 3 ou mais pesquisas nos últimos 15 dias" diz mais do que "temos 5.000 cadastros".
3. **Fuja da vaidade.** Downloads, visitas e curtidas dão falsa sensação de sucesso. Prefira uso, retorno e resultado.
4. **Métrica não é tarefa.** "Entregar X funcionalidades no prazo" não é métrica de sucesso. Sucesso é ter impacto: se você cumpre todas as tarefas e nada melhora, não houve sucesso.
5. **Combine quantitativo e qualitativo.** O número diz quanto, a conversa diz por quê.
6. **Aplique 80/20.** 80% do que importa está em 20% das métricas possíveis. Meça pouco e acompanhe sempre. O fluxo é: Dados, Análise, Informações, Análise, Ações.

## Modo avaliar

1. Leia `references/rubrica.md`, com as âncoras de nota de cada critério.
2. Dê uma nota de 0 a 100 para cada um dos 8 critérios, com evidência citada do material do usuário (nota sem evidência vira opinião).
3. Calcule a nota geral e aplique o teto.
4. Entregue no formato abaixo, com o conjunto melhorado.

### Os 8 critérios e seus pesos

| # | Critério | Peso | Pergunta que a nota responde |
|---|---|---|---|
| 1 | Vínculo com o problema | 18 | Cada métrica mede o problema do cliente, e não a solução ou o marketing? |
| 2 | Resultado, não tarefa | 14 | Mede mudança de comportamento ou impacto, e não entrega e prazo? |
| 3 | Acionável e sem vaidade | 12 | Cada métrica muda uma decisão? |
| 4 | Equilíbrio | 14 | Há métricas que impedem otimizar um número destruindo outro? |
| 5 | Definição operacional | 14 | Tem fórmula, unidade, período, fonte e linha de base? |
| 6 | Meta definida antes | 10 | O critério de sucesso numérico existe antes de medir, com origem? |
| 7 | Cobertura e nível | 8 | Cobre eficácia e algum sinal de eficiência, ecossistema ou excelência, no nível certo? |
| 8 | Foco (80/20) | 10 | São poucas, e combinam número com conversa? |

### Calibração e nota geral

- Ancore nos descritores da rubrica. Conjuntos de métricas escritos sem método costumam ficar entre 30 e 65. Reserve 90 ou mais para um conjunto que você colocaria no painel amanhã sem mexer.
- Nota geral = soma de (nota x peso) dividida por 100, arredondada.
- **Teto de bloqueio:** se qualquer critério ficar abaixo de 40, a nota geral não passa de 69.
- Faixas: 85 a 100 Pronto para acompanhar; 70 a 84 Quase lá; 50 a 69 Precisa de refinamento; 0 a 49 Reescrever.

### Formato de saída

Se o usuário pedir só a nota, entregue as seções 1 e 2 e ofereça o resto.

```
## Avaliação das métricas: [produto ou iniciativa]

**Nota geral: NN/100** (faixa)

### 1. Notas por critério
| Critério (peso) | Nota | Por quê (evidência) | Como melhorar |
|---|---|---|---|

### 2. O que mais pesa
(os 2 ou 3 pontos que mais afastam o conjunto de ficar bom, com o porquê)

### 3. Conjunto melhorado
| Papel | Métrica | Fórmula e período | Linha de base | Critério (meta) |
|---|---|---|---|---|
(principal, equilíbrio, apoio; use [colchetes] onde faltar dado)

### 4. Perguntas e suposições
```

Não invente números: onde faltar informação, escreva a suposição entre colchetes.

## Modo criar ou escolher

1. **Entenda o propósito e o problema.** Para quem é, que problema resolve, o que muda para o cliente. Se o usuário não trouxe, declare suposições e siga, em vez de interrogar.
2. **Defina a North Star Metric** (uma única métrica que capture o principal valor entregue ao cliente, como "noites reservadas" para o Airbnb ou "horas de valor" para a Netflix) e liste as **variáveis que a movem**, ao longo do ciclo do cliente: aquisição, ativação, retenção, receita e recomendação (Métricas do Pirata).
3. **Escolha a métrica principal do ciclo e as de equilíbrio.** Se medir só uma, o time vai otimizar esse número a qualquer custo (reduzir churn oferecendo 20 meses grátis quebra a empresa). Toda principal ganha 1 ou 2 de equilíbrio que protegem o resto, por exemplo churn, revenue churn e taxa de crescimento.
4. **Escolha o(s) framework(s)** pelo objetivo, usando `references/frameworks-e-formulas.md` (4 Domínios da Agilidade, OKR, Fit for Purpose, GEM, Pirata, NSM, métricas de fluxo, DORA). Eles não são métricas, são jeitos de organizar milhares de métricas possíveis.
5. **Defina cada métrica operacionalmente:** fórmula, unidade, período, fonte, linha de base, critério, quem olha e que decisão ela alimenta.
6. **Limite e equilibre:** de 3 a 7 métricas, com ao menos uma qualitativa. Confira o nível (estratégico, tático, operacional) e se há algum sinal de ecossistema (satisfação do time) ou excelência (qualidade) quando relevante.
7. **Autoavalie** com a rubrica e reescreva o que ficar abaixo de 80. Mostre a nota em uma linha.

### Formato de saída (criar)

```
## Métricas de [produto]

**Suposições:** ...

### 1. Propósito e problema
### 2. North Star Metric e o que a move
### 3. Conjunto de métricas
(tabela: papel, métrica, fórmula e período, baseline, critério)
### 4. Como acompanhar
(frequência, quem olha, que decisão cada uma alimenta)
### 5. Qualidade (autoavaliação): NN/100
```

## Princípios

- **Métrica vinculada ao problema, não à solução.** "Contrato assinado" ou "quantidade de conteúdo" não dizem se o churn caiu.
- **Métrica sozinha engana.** Sempre acompanhe uma de equilíbrio.
- **Defina antes de medir.** Critério escolhido depois do resultado é ajuste de régua.
- **Número não substitui conversa.** Combine com entrevistas e leitura de causa.

Para a hipótese que usa a métrica, use a skill `hipoteses`. Para transformar métricas em objetivos e resultados-chave, use a skill `okr`. Para ver uma avaliação completa, leia `references/exemplo.md`.
