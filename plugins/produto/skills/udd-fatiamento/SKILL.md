---
name: udd-fatiamento
description: Cria e avalia planos de produto no estilo UDD (Usage-Driven Development) da K21, em que o uso real, e não o roadmap, decide o que construir. Transforma uma ideia em epicentro, fatias verticais finas, hipótese e sinal de uso por fatia, regra de expansão e lista do que descartar (Fatiar, Descartar, Priorizar, Padrão 1-2-N), ou avalia um MVP, roadmap ou plano com nota de 0 a 100 por critério. Use sempre que o usuário falar de UDD, MVP, fatiar o produto, primeira versão, epicentro, "por onde começo?", "o que entra na primeira versão?", construir com IA ou Lovable sem desperdício, "velocidade sem direção", ou colar um plano grande de produto para reduzir de escopo, mesmo sem citar o UDD.
---

# UDD e fatiamento: construir pelo uso, não pelo plano

No UDD (Usage-Driven Development), o uso real é o único juiz legítimo do produto. Quando construir ficou fácil, o gargalo deixou de ser a velocidade e passou a ser a qualidade da decisão de produto. Cada fatia precisa provar que gera valor antes de você expandir para a próxima. Não é o roadmap, o Gantt, o PRD ou o story mapping que define o que construir, nem a facilidade de implementação: é o comportamento real do usuário.

Velocidade sem direção é só pressa. Velocidade com métrica é estratégia, e velocidade sem métrica é aposta. Waterfall com IA continua sendo waterfall: quem passa oito meses construindo sem colocar nada em uso só acelerou na direção errada.

Esta skill cria um plano UDD a partir de uma ideia e avalia planos, MVPs e roadmaps com a mesma régua. A skill `user-story` fatia **uma** história; esta fatia o **produto**, com hipótese e sinal de uso em cada passo.

## Escolha o modo

- **Criar**: o usuário traz uma ideia, produto ou escopo grande e quer o plano de fatias. Pedidos como "por onde começo?", "qual a primeira versão?", "monta o MVP".
- **Avaliar**: traz um plano, roadmap ou MVP e quer saber se está bom. Pedidos como "dá uma nota", "isso é um MVP de verdade?".
- **Avaliar e melhorar**: traz um plano inchado e quer a versão enxuta. Avalie e entregue o plano reescrito.

Responda no idioma do usuário (padrão: português do Brasil), com tom de mentor.

## Os ingredientes do UDD

- **Fatiar, Descartar, Priorizar.** Fatiar é buscar a menor parte que ainda agrega valor ao usuário final. Descartar é remover o que não é relevante (simplicidade é a arte de maximizar o trabalho não realizado). Priorizar é ordenar o que sobrou por valor.
- **A pergunta do epicentro:** "Qual é a parte mais importante do problema mais importante do usuário mais importante?" Comece pelo núcleo de maior impacto e só então expanda.
- **Fatia não é camada nem etapa.** Fatia é item que pode ser entregue para uso, avaliação e feedback. Tabela, consulta, serviço e tela são camadas: sozinhas não valem nada (uma roda sozinha não é um skate). "Fatia de planejamento, de desenvolvimento e de testes" é etapa de fluxo, não fatia.
- **Padrão 1-2-N.** Resolva em camadas de generalização: passo 1 é o caso básico, passo 2 é uma variação significativa, passo N generaliza. Vale para produto, entrevista, lançamento e campanha. Não acrescente passos demais antes do N, ou alguém chega ao N por você.
- **Toda fatia nasce de uma hipótese** e de uma forma de validá-la: o que queremos aprender, que comportamento esperamos ver, que sinal mostra que estamos no caminho certo, que evidência diz se insistimos, ajustamos ou abandonamos.
- **Roda, publica, testa, aprende, pensa na próxima ideia e roda de novo.** Cada fatia nasce do uso real da anterior, e nenhuma é planejada com antecedência demais.

## Modo criar

1. **Entenda a direção.** Propósito, problema e para quem, em uma linha cada. Se faltar, declare suposições e siga. Se o problema ainda não está claro, use a skill `estrategia-e-roadmap` (Tanque de Decantação) antes.
2. **Escreva a hipótese central** e a métrica de uso que a testa: "Acreditamos que [fatia] resultará em [comportamento]". Meça comportamento (usou, voltou, mudou o que fazia), não opinião.
3. **Ache o epicentro.** Responda a pergunta do epicentro e escolha a primeira fatia: a mais fina que ainda atravessa o produto de ponta a ponta, pode ser colocada em uso por poucas pessoas e ensina algo. Ela não precisa ser pública nem bonita.
4. **Desenhe as fatias seguintes** com as técnicas de `references/tecnicas-de-fatiamento.md` e a progressão 1-2-N. Ordene por valor e por aprendizado.
5. **Para cada fatia**, preencha: hipótese, sinal de uso e critério, limite de tempo, **regra de expansão** (o que precisa acontecer para a próxima fatia ser construída) e o que fica de fora.
6. **Descarte de verdade.** Liste o que o plano deixa de fazer. Se nada ficou de fora, o plano ainda não foi fatiado.
7. **Autoavalie** com a rubrica (`references/rubrica.md`) e reescreva o que ficar abaixo de 80.

### Formato de saída (criar)

```
## Plano UDD: [produto ou ideia]

**Suposições:** ...

### 1. Direção
Propósito, problema, para quem.

### 2. Hipótese central e sinal de uso

### 3. Epicentro e primeira fatia

### 4. Plano de fatias
| # | Fatia (resultado para o usuário) | Hipótese | Sinal de uso e critério | Limite de tempo | Só expande se... |
|---|---|---|---|---|---|

### 5. O que ficou de fora (descartado ou adiado)

### 6. Qualidade (autoavaliação): NN/100
```

## Modo avaliar

1. Leia `references/rubrica.md`.
2. Pontue os 8 critérios de 0 a 100, citando trechos do plano.
3. Nota geral = soma de (nota x peso) dividida por 100. **Teto de bloqueio:** se qualquer critério ficar abaixo de 40, a nota geral não passa de 69.
4. Faixas: 85 a 100 Pronto para rodar; 70 a 84 Quase lá; 50 a 69 Precisa de fatiar mais; 0 a 49 Reescrever.

| # | Critério | Peso |
|---|---|---|
| 1 | Hipótese e direção | 16 |
| 2 | Epicentro | 14 |
| 3 | Fatia vertical | 14 |
| 4 | Sinal de uso definido antes | 16 |
| 5 | Ciclo curto até o uso real | 12 |
| 6 | Progressão 1-2-N | 8 |
| 7 | Descarte explícito | 10 |
| 8 | Regra de expansão | 10 |

Formato de saída: nota geral no topo; tabela por critério com evidência e melhoria; os 2 ou 3 pontos que mais pesam; **plano reescrito** no formato de criar; suposições. Se o usuário pedir só a nota, entregue só as duas primeiras seções.

Calibre com rigor: planos reais, sem método, ficam entre 20 e 60. Reserve 90 ou mais para um plano que você colocaria em uso amanhã sem mudar nada.

## Princípios

- **Direção vem antes de velocidade.** Quando construir é fácil, escolher bem o que construir é o diferencial.
- **Produtividade não é progresso.** Dá para ser muito produtivo construindo a coisa errada.
- **Cada fatia prova valor antes da próxima.** Não é o roadmap que manda, é o uso.
- **Lançar algo pequeno o bastante para aprender rápido e relevante o bastante para gerar sinal.**
- **Sem dado, sem número.** Onde faltar informação (metas, volumes, prazos, nomes), escreva a suposição entre colchetes para o usuário substituir. Um resultado com números inventados parece pronto e leva o time a decidir com confiança no que não existe.

Para a hipótese e o experimento de cada fatia, use `hipoteses`. Para escrever as histórias de cada fatia, use `user-story`. Para as métricas de uso, use `metricas-de-produto`. Para ver uma avaliação completa, leia `references/exemplo.md`.
