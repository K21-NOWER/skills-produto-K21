---
name: user-story
description: Avalia, melhora e cria user stories (histórias de usuário) com critérios de aceitação claros. No modo avaliar, dá notas de 0 a 100 por critério (persona, valor, efetividade, clareza, foco no problema, tamanho e necessidade de fatiar, critérios de aceitação, independência, estimabilidade), calcula uma nota geral e sugere como melhorar e fatiar. No modo criar, transforma ideias, requisitos ou funcionalidades soltas em stories pequenas e testáveis, com critérios de aceitação em Dado/Quando/Então. Use sempre que o usuário falar de user story, história de usuário, critérios de aceitação, refinamento de backlog, INVEST, ou perguntar "essa story está boa?", "está grande demais?", "precisa fatiar?", "transforma essa ideia em story", ou colar um texto no formato "Como [persona], quero [ação], para [benefício]", mesmo sem pedir uma avaliação explicitamente.
---

# User Story: avaliar, melhorar e criar

Uma user story boa não é um documento, é um convite para uma conversa. O cartão lembra a conversa, a conversa gera entendimento e os critérios de aceitação confirmam que ficou pronto (os "3 Cs" de Ron Jeffries: Card, Conversation, Confirmation). Esta skill ajuda Product Owners, Product Managers e alunos a chegar numa story que o time consiga entender, estimar, entregar e testar sem precisar adivinhar.

A skill tem dois modos e os dois usam a mesma régua de qualidade. Isso é de propósito: quem cria com um critério e avalia com outro acaba escrevendo stories que ele mesmo reprovaria.

## Escolha o modo

- **Avaliar**: o usuário traz uma ou mais stories prontas e quer saber se estão boas, o que melhorar ou se precisam ser fatiadas. Pedidos como "dá uma nota", "revisa", "está pronta pra sprint?", "está grande demais?".
- **Criar**: o usuário traz uma ideia, funcionalidade, requisito, problema ou anotação de reunião e quer transformar em stories. Pedidos como "transforma isso em story", "escreve as stories de...", "quebra essa ideia em histórias".
- **Avaliar e melhorar** (o mais comum com quem está aprendendo): o usuário traz uma story fraca e quer a versão boa. Faça a avaliação e entregue a versão melhorada.

Quando o pedido não deixar claro, deduza pelo que foi colado: uma frase "Como... quero... para..." pede avaliação; uma ideia solta pede criação. Se ainda assim ficar ambíguo, avalie, porque a avaliação já mostra o caminho.

Responda no idioma do usuário (padrão: português do Brasil). Use tom de mentor: aponte o problema, explique por que ele importa e mostre como arrumar. Sem julgamento, uma story fraca é um ponto de partida. Se o usuário trouxe contexto (produto, objetivo, time, cadência), use-o nas notas e nas sugestões.

## Modo avaliar

1. Leia `references/rubrica.md`. Ela traz as âncoras de nota de cada critério e é o que torna as notas comparáveis de uma avaliação para outra.
2. Dê uma nota de 0 a 100 para cada um dos 9 critérios abaixo. Cada nota precisa de uma justificativa curta ancorada em um trecho da própria story (cite entre aspas), porque nota sem evidência vira opinião e o usuário não aprende com ela.
3. Calcule a nota geral (média ponderada) e aplique as regras de teto.
4. Dê o veredito de tamanho (cabe, atenção, precisa fatiar) e, se precisar fatiar, proponha as fatias (veja `references/fatiamento.md`).
5. Entregue no formato da seção "Formato de saída". Para ver uma avaliação completa e calibrada, leia `references/exemplo-avaliacao.md` na primeira vez que usar a skill.

### Os 9 critérios e seus pesos

| # | Critério | Peso | Pergunta que a nota responde |
|---|---|---|---|
| 1 | Persona (quem) | 8 | Dá para imaginar uma pessoa real, num contexto real, querendo isso? |
| 2 | Valor (por quê) | 12 | O "para" explica um benefício real ou só repete o "quero"? |
| 3 | Efetividade (como saber que funcionou) | 10 | Depois de entregue, dá para saber se o resultado foi alcançado, e não só se a funcionalidade existe? |
| 4 | Clareza (o quê) | 14 | Duas pessoas diferentes leriam e imaginariam a mesma coisa? |
| 5 | Foco no problema | 8 | Descreve a necessidade ou já prescreve a solução (tela, botão, tecnologia)? |
| 6 | Tamanho (cabe? fatiar?) | 16 | Cabe em poucos dias do time e pode ser demonstrada sozinha? |
| 7 | Critérios de aceitação | 18 | São verificáveis, específicos e cobrem o caminho feliz, os erros e os limites? |
| 8 | Independência | 6 | Pode ser priorizada e entregue sem depender de outra story? |
| 9 | Estimabilidade | 8 | O time consegue estimar sem grandes perguntas em aberto? |

Os pesos refletem onde as stories mais falham na prática: tamanho e critérios de aceitação decidem se o time consegue começar, então pesam mais. Persona e independência raramente derrubam uma story sozinhas. Os critérios cobrem o INVEST (Independente, Negociável, Valiosa, Estimável, Pequena, Testável) e acrescentam persona, clareza e efetividade, que o INVEST não mede bem.

### Calibração (leia antes de pontuar)

- Ancore cada nota nos descritores da rubrica, não na impressão geral. Dentro de uma faixa, suba ou desça conforme a quantidade de sinais positivos e negativos que o texto mostra.
- Seja criterioso. Stories reais, escritas sem método, costumam ficar entre 35 e 70. Reserve 90 ou mais para uma story que você colocaria na sprint sem mudar uma vírgula. Se todos os critérios saírem acima de 85, releia procurando o que passou despercebido.
- Avalie contra o padrão "pronta para o time começar". Se o usuário disser que é um rascunho de backlog, mantenha a régua, mas deixe claro o que é esperado nessa fase (por exemplo, critérios de aceitação ainda ausentes) e o que falta para ficar pronta.
- Quando algo essencial não estiver no texto (sem persona, sem "para", sem critérios), a nota do critério fica na faixa mais baixa. Não preencha lacunas com boa vontade: o que o time não consegue ler, o time não consegue construir.

### Nota geral e regras de teto

Nota geral = soma de (nota do critério x peso) dividida por 100, arredondada.

- **Teto de bloqueio:** se qualquer critério ficar abaixo de 40, a nota geral não passa de 69. Uma média alta não pode esconder um ponto que impede o time de começar.
- **Teto de tamanho:** se o veredito de tamanho for "precisa fatiar", a nota geral não passa de 69. Uma story grande demais ainda não está pronta, por mais bem escrita que seja.

| Nota geral | Faixa | O que significa |
|---|---|---|
| 85 a 100 | Pronta para o time | Pode entrar na sprint, com no máximo ajustes de vírgula |
| 70 a 84 | Quase lá | Pequenos ajustes pontuais antes de entrar |
| 50 a 69 | Precisa de refinamento | Vale uma conversa com quem pediu e com o time |
| 0 a 49 | Reescrever | Volte ao problema do usuário e comece de novo |

### Veredito de tamanho

Use a nota do critério 6: 75 ou mais = **Cabe**; 50 a 74 = **Atenção** (cabe, mas com risco; fatie se puder); abaixo de 50 = **Precisa fatiar**. Fatie na vertical (uma fatia fina que atravessa tela, regra e dados e entrega algo utilizável), nunca na horizontal (uma story para o banco, outra para a API, outra para a tela), porque fatia horizontal não entrega valor sozinha e esconde o risco até o fim.

### Formato de saída

Use este formato. Se o usuário pedir só a nota, entregue só as seções 1 e 2 e ofereça o resto no fim. Se trouxer mais de 3 stories, veja "Várias stories de uma vez".

```
## Avaliação: [título curto ou primeira linha da story]

**Nota geral: NN/100** (faixa) · **Tamanho:** Cabe / Atenção / Precisa fatiar

### 1. Notas por critério
| Critério (peso) | Nota | Por quê (evidência) | Como melhorar |
|---|---|---|---|
(uma linha por critério, com trecho citado e uma melhoria concreta em uma frase)

### 2. O que mais pesa
(os 2 ou 3 problemas que mais afastam a story de ficar pronta, em ordem de impacto, com o porquê)

### 3. Fatiamento
(só se Atenção ou Precisa fatiar: o padrão de fatiamento usado e a lista de fatias em ordem, cada uma como mini-story de uma linha)

### 4. Versão melhorada
(a story reescrita no formato padrão, com critérios de aceitação)

### 5. Perguntas e suposições
(o que você assumiu para reescrever e o que vale confirmar com quem pediu a funcionalidade)
```

Mostre a nota geral logo no topo: é o que o usuário procura primeiro, e o resto é o porquê dela.

Na seção 4, reescreva sem inventar fatos de negócio. Onde faltar informação (persona real, números, regras), escreva a suposição de forma explícita, entre colchetes, para o usuário substituir. Uma versão melhorada com números inventados parece pronta, mas leva o time a construir a coisa errada com confiança.

### Várias stories de uma vez

Com mais de 3 stories, comece por uma tabela-resumo (story, nota geral, tamanho, maior problema), ordenada da pior para a melhor, e detalhe no formato completo só as 2 ou 3 piores, ou as que o usuário pedir. No fim, aponte padrões repetidos ("quase todas estão sem 'para'"), porque o padrão ensina mais do que cada nota isolada.

## Modo criar

O objetivo é sair da ideia com stories pequenas, claras e testáveis, sem encher o usuário de perguntas.

1. **Entenda a ideia.** Identifique quem tem o problema, qual é o problema ou objetivo e o que muda para essa pessoa se der certo. Faça perguntas só quando a resposta mudaria o desenho das stories (persona principal desconhecida, objetivo ambíguo). Fora isso, declare as suposições e siga: é mais barato o usuário corrigir uma suposição do que responder um questionário. Se a ideia vier em poucas palavras, faça no máximo 3 perguntas curtas, de uma vez.
2. **Fatie antes de escrever.** Quebre a ideia em fatias verticais finas, usando `references/fatiamento.md`. Comece pela fatia mais fina que já entrega valor de ponta a ponta (o "esqueleto andante") e acrescente as demais por ordem de valor e risco.
3. **Mostre o mapa de fatias.** Liste todas as fatias, uma linha cada (título como resultado, não como tarefa), na ordem sugerida, e explique em uma frase por que essa ordem.
4. **Detalhe as primeiras.** Escreva por completo as 3 a 5 primeiras stories. As seguintes dependem do que a primeira entrega ensinar, e detalhar tudo agora é planejar no escuro. Fatiar, descartar e priorizar andam juntos: o que não entra nas primeiras fatias pode nem precisar existir. Se o usuário pedir todas, escreva todas, deixando as últimas mais enxutas.
5. **Autoavalie.** Passe cada story pela rubrica antes de entregar. Se alguma ficar abaixo de 80 ou com tamanho "precisa fatiar", reescreva. Mostre a nota final em uma linha por story, sem a tabela completa, a menos que o usuário peça.

### Formato de cada story

```
### US-01 · [Título curto, em forma de resultado]
**História:** Como [persona específica], quero [necessidade ou ação], para [benefício concreto].

**Critérios de aceitação**
- **Cenário: [nome]**
  - Dado que [contexto]
  - Quando [ação]
  - Então [resultado observável]
- **Regras:** [validações e regras de negócio, em lista, se houver]

**Fora do escopo:** [o que fica de fora para manter a story pequena]
**Sinal de sucesso:** [como saberemos que funcionou, ex.: métrica ou comportamento esperado]
**Dúvidas e suposições:** [o que foi assumido]
**Qualidade (autoavaliação):** NN/100 · Tamanho: Cabe
```

Use Dado/Quando/Então para comportamentos com fluxo e lista de regras para validações e regras de negócio. Para escrever critérios que o time consiga testar, leia `references/criterios-de-aceitacao.md`.

## Princípios que sustentam a rubrica

- **A story descreve o problema, não a solução.** Quem decide o como é o time, junto com o usuário. Prescrever tela e tecnologia na story mata a conversa que a deixaria melhor.
- **Fatiar é a habilidade central.** Story pequena entrega mais cedo, recebe feedback mais cedo e erra mais barato. O que não vale a pena construir agora, descarte da lista: "e se precisar depois?" já matou mais produtos do que bugs.
- **Pronto é diferente de funcionou.** Critérios de aceitação respondem "ficou pronto?". O sinal de sucesso responde "funcionou para o usuário?". As duas perguntas importam, e a segunda é a que mais se esquece.
- **Tarefa técnica não é story.** "Criar endpoint" ou "migrar o banco" são tarefas. Quando são necessárias, ligue-as ao resultado que habilitam e trate como habilitadoras, sem fingir que têm persona.

## Outras skills deste repositório

- Se a story nasce de uma incerteza ("acreditamos que..."), use antes a skill `hipoteses`: ela valida a ideia e depois chama esta skill para gerar a story.
- Se há muitas stories e é preciso decidir a ordem, use a skill `priorizacao`.
