---
name: produto-k21
description: Pacote de 14 skills de gestão de produto da K21 e da Nower, em português do Brasil: user story, visão do produto, priorização (RICE, ICE, Matriz RUT), hipóteses (Test Card 2.0), métricas, UDD e fatiamento, OKR, saúde do backlog, previsibilidade (Monte Carlo), papel de PO/PM/GPM, discovery com clientes, estratégia e roadmap, apresentação de produto e riscos e vieses. Avalia com nota de 0 a 100, cria e explica. Use sempre que o usuário falar de produto, backlog, user story, critérios de aceitação, visão, priorizar, hipótese, experimento, métrica, OKR, roadmap, estratégia, entrevista com cliente, previsão de entrega, apresentação de produto, risco ou pré-mortem, mesmo sem citar o método.
---

# Produto K21: 14 skills em um pacote

Este pacote reúne 14 modos de trabalho de gestão de produto. Cada modo tem as instruções completas em um arquivo próprio. Escolha o modo pelo pedido do usuário, leia só o arquivo desse modo e siga-o do início ao fim, como se fosse uma skill independente.

| Quando o usuário quer... | Modo | Arquivo a ler |
|---|---|---|
| Avaliar, melhorar ou criar user stories e critérios de aceitação; saber se uma story precisa ser fatiada (saúde da história em 9 passos) | user-story | `modos/user-story/MODO.md` |
| Avaliar ou criar a visão do produto, o vision board, o posicionamento ou o Tanque de Decantação | visao-do-produto | `modos/visao-do-produto/MODO.md` |
| Priorizar uma lista de atividades, ideias ou iniciativas (RICE, ICE, Matriz RUT, MoSCoW, Kano, WSJF, Valor x Esforço) | priorizacao | `modos/priorizacao/MODO.md` |
| Avaliar hipóteses, desenhar experimentos, Test Card 2.0 e Learning Card, métricas e riscos, e transformar a hipótese em user story | hipoteses | `modos/hipoteses/MODO.md` |
| Avaliar ou escolher métricas de produto: North Star, métrica principal e de equilíbrio, Métricas do Pirata, fórmulas | metricas-de-produto | `modos/metricas-de-produto/MODO.md` |
| Transformar uma ideia em plano UDD: epicentro, fatias verticais, sinal de uso, Padrão 1-2-N, o que descartar | udd-fatiamento | `modos/udd-fatiamento/MODO.md` |
| Avaliar, escrever ou acompanhar OKRs e diagnosticar as disfunções mais comuns | okr | `modos/okr/MODO.md` |
| Auditar a saúde do backlog, limpar, fazer triagem de demandas (descartar, prateleira ou investir) | saude-do-backlog | `modos/saude-do-backlog/MODO.md` |
| Responder "quando fica pronto?" e "quanto cabe até a data?" com previsão probabilística e dados de fluxo | previsibilidade | `modos/previsibilidade/MODO.md` |
| Fazer autodiagnóstico do papel de PO, PM ou GPM: arquétipos, disfunções, plano de evolução e Matriz de Faixas | papel-de-produto | `modos/papel-de-produto/MODO.md` |
| Preparar, avaliar e sintetizar entrevistas e discovery com clientes | discovery-com-clientes | `modos/discovery-com-clientes/MODO.md` |
| Construir ou avaliar estratégia e roadmap: Tanque de Decantação, Matriz de Estratégia, Bússola, Radar, roadmap enxuto | estrategia-e-roadmap | `modos/estrategia-e-roadmap/MODO.md` |
| Criar ou avaliar apresentações de produto, pitch, Sprint Review e data storytelling | apresentacao-de-produto | `modos/apresentacao-de-produto/MODO.md` |
| Fazer pré-mortem, detectar vieses cognitivos, mapear riscos e rodar a Matriz de Hipóteses | riscos-e-vieses | `modos/riscos-e-vieses/MODO.md` |

## Como usar o pacote

1. **Leia só o modo que o pedido pede.** Os outros arquivos de modo só entram em cena se o trabalho precisar deles. Isso mantém o contexto enxuto.
2. **Os caminhos já estão ajustados.** Os arquivos de modo citam pastas `references` e `scripts`. Dentro deste pacote, elas ficam em `modos/<modo>/references` e `modos/<modo>/scripts`, e os caminhos escritos nos arquivos de modo já apontam para lá.
3. **Quando um modo mandar usar outra skill, leia o arquivo do modo correspondente e siga-o.** Onde um modo falar em "skill `<nome>`" (por exemplo `user-story`, `hipoteses`, `priorizacao`, `saude-do-backlog`), leia o MODO.md desse nome. Exemplo: ao transformar uma hipótese em user story, siga `modos/user-story/MODO.md` no modo criar.
4. **Pedidos que misturam modos** seguem o fluxo natural do trabalho de produto: descoberta com clientes, visão e estratégia, hipóteses, priorização, user stories e fatiamento, métricas e OKRs, acompanhamento e previsão. Faça uma etapa de cada vez e avise o usuário quando passar para a próxima.
5. **Idioma:** responda no idioma do usuário (padrão: português do Brasil).
