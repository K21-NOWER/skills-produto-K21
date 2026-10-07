---
name: papel-de-produto
description: Faz o autodiagnóstico do papel de Product Owner, Product Manager ou Group Product Manager com os 7 arquétipos do PO, as disfunções do papel (hierarquia de donos, PO comitê, desempoderado, garçom, mestre dos magos, César, técnico, freio de mão puxado) e um termômetro de 0 a 100, compara PO, PM, GPM e gerente de projetos, e monta plano de evolução e Matriz de Faixas para carreira e feedback. Use sempre que o usuário falar de papel do PO, diferença entre PO e PM, GPM, gerente de projetos x produto, arquétipo, disfunção do PO, carreira de produto, "meu PO não decide nada", "sou PO ou PM?", "será que estou fazendo certo como PO?", "me avalia como PO", dar feedback a quem trabalha com produto ou desenhar quem decide o quê, mesmo sem citar esses termos.
---

# Papel de produto: diagnóstico, comparação e evolução

"PO é o CEO do produto", como diz o Garrido. A pessoa dona do produto maximiza o valor do que o time entrega, comunica-se com o time, os clientes e os stakeholders, entende o mercado, acompanha as métricas de uso e eficácia e alimenta, prioriza e gere o backlog. É um trabalho de analisar problemas e sintetizar hipóteses de solução, em que **Fatiar, Descartar e Priorizar** é fundamental.

Esta skill ajuda quem exerce o papel (e quem lidera quem exerce) a se enxergar com clareza: qual padrão de atuação predomina, que disfunções do ambiente e da pessoa aparecem e qual o próximo passo de evolução.

**Regra de ouro: sem rótulo e sem julgamento.** Arquétipos não são prescritivos nem estereótipos: são padrões encontrados nas empresas, e não existe arquétipo certo ou errado, existem alguns mais completos que outros. E trate disfunção como disfunção, nunca como erro: elas nascem de soluções passadas que causaram novos problemas. Acolha, mostre com fatos e métricas que há caminhos melhores, e nunca diga "vocês estão errados".

## Escolha o modo

- **Diagnosticar**: a pessoa descreve o dia a dia do papel (ou o líder descreve o de alguém) e quer saber arquétipo, disfunções e o termômetro. Pedidos como "meu PO só repassa tarefa, o que é isso?".
- **Comparar papéis**: quer entender PO x PM x GPM x gerente de projetos, ou decidir como a empresa deve desenhá-los. Veja `references/papeis-comparados.md`.
- **Evoluir**: quer plano de desenvolvimento ou uma Matriz de Faixas para feedback e carreira. Veja `references/matriz-de-faixas.md`.
- **Diagnosticar e evoluir** (o mais comum): entregue o diagnóstico e o plano.

Responda no idioma do usuário (padrão: português do Brasil), com tom de mentor.

## Modo diagnosticar

1. Se faltar informação, faça no máximo 4 perguntas curtas (quem decide as prioridades, com quem fala todo dia, que métricas vê, como é a Review). Sem tempo para perguntar, declare suposições.
2. Leia `references/arquetipos-e-disfuncoes.md`.
3. **Arquétipos:** indique o predominante e, se houver, o secundário, com a **evidência** do relato. Uma pessoa pode ter mais de um conforme o contexto. Mostre o que cada um traz de bom e de limitação, e o próximo passo possível.
4. **Disfunções:** liste só as que aparecem no relato, com o sinal, a severidade (baixa, média ou alta) e um primeiro passo acolhedor.
5. **Termômetro do papel (0 a 100):** pontue as 6 dimensões, com evidência.
6. **Plano de evolução 30-60-90** com passos pequenos e medidos.

### O termômetro do papel

| # | Dimensão | Peso | Pergunta |
|---|---|---|---|
| 1 | Autonomia e decisão | 20 | A pessoa é a dona do produto, sem hierarquia paralela nem comitê? |
| 2 | Proximidade com o time | 16 | Está disponível durante a sprint, ou só aparece nos rituais? |
| 3 | Resultado e métricas | 18 | Tem acesso e usa métricas de uso e eficácia para decidir? |
| 4 | Cliente e mercado | 16 | Fala com todos os tipos de clientes e entende o mercado, ou só com um proxy? |
| 5 | Fatiar, Descartar, Priorizar | 18 | Decide por valor, e não por complexidade técnica ou por quem grita mais? |
| 6 | Entrega e feedback | 12 | Entrega com frequência e usa a Review para colher feedback, e não para aprovar? |

Nota geral = soma de (nota x peso) dividida por 100. **Teto de bloqueio:** se qualquer dimensão ficar abaixo de 40, a nota geral não passa de 69. Faixas: 85 a 100 Dono do produto; 70 a 84 Quase lá; 50 a 69 Em evolução; 0 a 49 Papel desempoderado. A nota descreve o **contexto e o comportamento**, não o valor da pessoa: muitas vezes a causa está na organização.

### Formato de saída

```
## Diagnóstico do papel: [pessoa ou contexto]

**Termômetro: NN/100** (faixa) · **Arquétipo predominante:** ...

### 1. Arquétipos
### 2. Disfunções percebidas
| Disfunção | Sinal no relato | Severidade | Primeiro passo acolhedor |
### 3. Termômetro por dimensão
| Dimensão (peso) | Nota | Evidência | Como evoluir |
### 4. Plano 30-60-90
### 5. Perguntas e suposições
```

Calibre com rigor e sem dureza: relatos reais ficam entre 30 e 75. Se o usuário pedir só o arquétipo, entregue só a seção 1.

## Princípios

- **O nome do cargo importa menos que a clareza de quem decide.** Product Owner, Product Manager ou "produteiro": a disfunção está em criar uma hierarquia de "donos", não na nomenclatura.
- **Um é pouco, dois é demais, para o papel de dono.** "O Product Owner é uma pessoa, não um comitê."
- **PO não é cliente nem intermediário.** Quem só repassa pedido do negócio ao time infantiliza o time e perde o contexto.
- **Quem lidera quem faz produto** desenvolve pessoas: mentoria, feedback e clareza de expectativas.
- **Sem dado, sem número.** Onde faltar informação (metas, volumes, prazos, nomes), escreva a suposição entre colchetes para o usuário substituir. Um resultado com números inventados parece pronto e leva o time a decidir com confiança no que não existe.

Para a Matriz de Faixas, leia `references/matriz-de-faixas.md`. Para fatiar, descartar e priorizar, use `udd-fatiamento` e `priorizacao`. Para ver um diagnóstico completo, leia `references/exemplo.md`.
