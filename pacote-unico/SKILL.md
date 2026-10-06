---
name: produto-k21
description: Pacote de skills de gestão de produto da K21 e da Nower, em português do Brasil, com quatro modos: user story (avalia com nota de 0 a 100, fatia e cria stories com critérios de aceitação), visão do produto (avalia e cria visão, posicionamento e Product Vision Board), priorização (RICE, ICE, MoSCoW, Kano, WSJF, Valor x Esforço ou matriz ponderada, com explicação) e hipóteses (avalia, sugere experimentos, métricas e riscos, monta Test Card e gera a user story). Use sempre que o usuário falar de user story, história de usuário, critérios de aceitação, backlog, visão do produto, vision board, proposta de valor, priorizar, roadmap, RICE, MoSCoW, hipótese, experimento, MVP, validação de ideia ou métricas de sucesso, mesmo sem pedir uma avaliação ou citar o método.
---

# Produto K21: quatro skills em um pacote

Este pacote reúne quatro modos de trabalho de gestão de produto. Cada modo tem as instruções completas em um arquivo próprio. Escolha o modo pelo pedido do usuário, leia só o arquivo desse modo e siga-o do início ao fim, como se fosse uma skill independente.

| Quando o usuário quer... | Modo | Arquivo a ler |
|---|---|---|
| Avaliar, melhorar ou criar user stories e critérios de aceitação; saber se uma story precisa ser fatiada | user-story | `modos/user-story/MODO.md` |
| Avaliar ou criar a visão do produto, o vision board ou o posicionamento | visao-do-produto | `modos/visao-do-produto/MODO.md` |
| Priorizar uma lista de atividades, ideias ou iniciativas (RICE, ICE, MoSCoW, Kano, WSJF, Valor x Esforço) | priorizacao | `modos/priorizacao/MODO.md` |
| Avaliar hipóteses, desenhar experimentos, métricas e riscos, e transformar a hipótese em user story | hipoteses | `modos/hipoteses/MODO.md` |

## Como usar o pacote

1. **Leia só o modo que o pedido pede.** Os outros arquivos de modo só entram em cena se o trabalho precisar deles. Isso mantém o contexto enxuto.
2. **Os caminhos já estão ajustados.** Os arquivos de modo citam pastas `references` e `scripts`. Dentro deste pacote, elas ficam em `modos/<modo>/references` e `modos/<modo>/scripts`, e os caminhos escritos nos arquivos de modo já apontam para lá.
3. **Quando um modo mandar usar outra skill, leia o arquivo do modo correspondente e siga-o.** Onde um modo falar em "skill `user-story`", "skill `hipoteses`", "skill `priorizacao`" ou "skill `visao-do-produto`", leia o MODO.md desse nome. Exemplo: ao transformar uma hipótese em user story, siga `modos/user-story/MODO.md` no modo criar.
4. **Pedidos que misturam modos** seguem o fluxo natural do trabalho de produto: visão, hipóteses, priorização, user stories. Faça uma etapa de cada vez e avise o usuário quando passar para a próxima.
5. **Idioma:** responda no idioma do usuário (padrão: português do Brasil).
