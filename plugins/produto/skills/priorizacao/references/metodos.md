# Métodos de priorização

Conteúdo: 1 RICE · 2 ICE · 3 Valor x Esforço · 4 MoSCoW · 5 Kano · 6 WSJF e Custo do Atraso · 7 Matriz ponderada · Como combinar métodos · Calibração das escalas · Vieses a vigiar

Cada método segue a mesma estrutura: quando usar, que pergunta responde, como pontuar, pontos cegos.

---

## 1. RICE

**Quando usar:** produto com usuários e alguma medição; muitos candidatos; é preciso comparar itens com um número.

**Pergunta que responde:** qual item gera mais resultado por unidade de esforço, considerando quantas pessoas alcança e o quanto confiamos na estimativa?

**Fórmula:** `RICE = (Alcance x Impacto x Confiança) / Esforço`

| Componente | Escala |
|---|---|
| **Alcance** (Reach) | Número de pessoas ou eventos no período (ex.: clientes por trimestre). Use o mesmo período para todos os itens |
| **Impacto** (Impact) | Efeito sobre o objetivo, por pessoa alcançada: 3 = massivo, 2 = alto, 1 = médio, 0,5 = baixo, 0,25 = mínimo |
| **Confiança** (Confidence) | 100% = alta (há dados), 80% = média, 50% = baixa (intuição). Abaixo de 50% é palpite: vire hipótese em vez de pontuar |
| **Esforço** (Effort) | Pessoas-mês (ou pessoas-semana) somando design, desenvolvimento e teste |

**Pontos cegos:** favorece itens de alcance grande e pode subestimar itens estratégicos de pouco alcance; o impacto é subjetivo (ancore sempre no objetivo do período: "impacto em quê?"); o esforço é uma estimativa e costuma ser otimista.

---

## 2. ICE

**Quando usar:** produto novo, poucos dados, ritmo rápido, lista de experimentos ou ideias de crescimento.

**Pergunta que responde:** o que vale tentar primeiro, considerando o ganho esperado, a certeza que temos e a facilidade?

**Fórmula:** `ICE = Impacto x Confiança x Facilidade`, cada um de 1 a 10 (alguns times usam a média em vez do produto; escolha um e mantenha).

**Como pontuar:** escolha um item de referência que vale 5 em tudo e compare os outros a ele. Isso evita inflar as notas.

**Pontos cegos:** notas subjetivas e relativas; não considera alcance; a facilidade pode privilegiar só o que é fácil. Marque como sinal de experimento todo item com impacto alto e confiança baixa.

---

## 3. Valor x Esforço

**Quando usar:** workshop com stakeholders; é preciso algo visual, rápido e fácil de explicar.

**Pergunta que responde:** onde estão os ganhos rápidos e o que não vale o esforço?

**Como pontuar:** valor de 1 a 10 e esforço de 1 a 10 (ou P, M, G). Posicione em quatro quadrantes, com o corte no meio da escala:

| Quadrante | Valor | Esforço | O que fazer |
|---|---|---|---|
| **Ganho rápido** | Alto | Baixo | Fazer agora |
| **Aposta grande** | Alto | Alto | Planejar e fatiar; confirmar o valor antes de investir |
| **Preenchimento** | Baixo | Baixo | Fazer só se sobrar capacidade |
| **Evitar** | Baixo | Alto | Descartar |

**Pontos cegos:** "valor" é uma nota só e mistura receita, retenção, risco; não considera confiança nem alcance; fácil de manipular em reunião. Ótimo como contraprova visual de um método numérico.

---

## 4. MoSCoW

**Quando usar:** escopo fechado (release, MVP, prazo regulatório); negociação do que entra e do que sai.

**Pergunta que responde:** o que é indispensável, o que é desejável e o que fica de fora desta vez?

| Categoria | Significado | Teste |
|---|---|---|
| **Must have** (Deve ter) | Sem isso a entrega não faz sentido, é ilegal ou insegura | "Se ficar de fora, ainda dá para lançar?" Se sim, não é Must |
| **Should have** (Deveria ter) | Importante, mas há um contorno aceitável | "Existe um jeito de lidar sem isso no começo?" |
| **Could have** (Poderia ter) | Bom de ter; entra se sobrar capacidade | |
| **Won't have** (Não terá, desta vez) | Combinado explicitamente que fica para depois | "Won't" não é "nunca" |

**Regra prática (DSDM):** deixe os Must have em até cerca de 60% da capacidade, para ter folga e absorver imprevistos.

**Pontos cegos:** tudo vira Must; não ordena dentro de cada grupo. Combine: use MoSCoW para cortar e RICE ou ICE para ordenar dentro de cada categoria.

---

## 5. Kano

**Quando usar:** entender como o cliente percebe as funcionalidades e equilibrar básico, desempenho e encantamento.

**Pergunta que responde:** que tipo de reação esta funcionalidade provoca no cliente?

| Categoria | Descrição |
|---|---|
| **Obrigatória** (Must-be) | A ausência frustra; a presença é esperada e não encanta |
| **Desempenho** (One-dimensional) | Quanto mais, maior a satisfação |
| **Atrativa** (Delighter) | Inesperada; encanta; a ausência não incomoda |
| **Indiferente** | Ninguém liga |
| **Reversa** | Alguns clientes não querem |

**Como classificar:** para cada funcionalidade, faça duas perguntas ao cliente: "Como você se sentiria se o produto **tivesse** X?" e "Como se **não tivesse** X?" (respostas: gosto, espero, tanto faz, aceito, não gosto) e cruze as respostas na tabela de Kano. Sem pesquisa, classifique por hipótese e marque como "a validar".

**Como usar:** garanta as Obrigatórias; invista em Desempenho conforme a estratégia; escolha uma ou duas Atrativas para diferenciar. As categorias mudam com o tempo: o que encanta hoje vira obrigatório amanhã.

**Pontos cegos:** não gera ranking numérico sozinho; depende de pesquisa com clientes.

---

## 6. WSJF e Custo do Atraso

**Quando usar:** o custo de esperar é desigual entre os itens (prazos, janelas de mercado, riscos que crescem); várias equipes e dependências; ambientes que usam SAFe.

**Pergunta que responde:** o que perdemos a cada semana que adiamos, em relação ao tamanho do trabalho?

**Fórmula:** `WSJF = Custo do Atraso / Tamanho do trabalho`, em que `Custo do Atraso = Valor para o usuário ou negócio + Criticidade no tempo + Redução de risco ou habilitação de oportunidade`.

**Como pontuar:** escala relativa (1, 2, 3, 5, 8, 13, 20). Em cada componente, o item "menor" recebe 1 e os demais são comparados a ele. Pergunte: "o que acontece se esperarmos 3 meses?"

**Pontos cegos:** exige comparar itens entre si (trabalhoso e melhor em grupo); os componentes se sobrepõem; sem calibração coletiva, as notas viram opinião.

---

## 7. Matriz ponderada

**Quando usar:** há vários objetivos ou critérios estratégicos próprios (OKRs, compliance, risco, receita, retenção) e é preciso transparência para os stakeholders.

**Como fazer:**

1. Escolha de 3 a 6 critérios derivados do objetivo (ex.: alinhamento estratégico, impacto na receita, redução de risco, facilidade).
2. Dê pesos que somem 100, refletindo a estratégia.
3. Pontue cada item de 1 a 5, com um descritor para cada nota, para evitar interpretações diferentes.
4. `Nota = soma(peso x nota) / soma dos pesos`. O esforço entra como "Facilidade" (nota alta = fácil).

**Pontos cegos:** pesos arbitrários mudam o resultado, então teste a sensibilidade (mude cada peso em 10 pontos e veja se os 3 primeiros mudam); critérios correlacionados contam em dobro.

---

## Como combinar métodos

- **Filtro e ordenação:** MoSCoW corta; RICE ou ICE ordena dentro de cada grupo.
- **Triangulação:** método principal e Valor x Esforço como contraprova. Onde discordam, vale a conversa.
- **Do rápido ao refinado:** ICE para triar 30 ideias; RICE nas 8 finalistas.
- **Para a incerteza:** itens de confiança baixa viram hipóteses (skill `hipoteses`), testadas antes de pontuar de novo.

## Calibração das escalas

- Escolha um item **âncora** e compare os demais a ele.
- Use **a mesma escala e o mesmo período** para todos os itens.
- Prefira **faixas** a falsa precisão (1.000, 2.000, 4.000 em vez de 3.847).
- Estime **em grupo** quando possível: a divergência entre as estimativas é, ela mesma, informação.
- Revise as notas depois da entrega e compare com o real. É assim que o time calibra.

## Vieses a vigiar

- **HiPPO**: a opinião do mais bem pago na sala ("highest paid person's opinion").
- **Efeito de recência**: o último pedido que chegou parece o mais urgente.
- **Projeto de estimação**: o item que alguém ama e já "sabe" que é prioridade.
- **Viés do fácil**: só fazer o que é barato e adiar o que é importante.
- **Ancoragem**: a primeira nota dada contamina as seguintes.
- **Falsa precisão**: números com casas decimais não tornam a estimativa melhor.
- **"Tudo é prioridade"**: sem uma linha de corte, não há priorização.
