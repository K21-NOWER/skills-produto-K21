---
name: saude-do-backlog
description: Audita a saúde de um backlog de produto com nota de 0 a 100 por critério (horizonte de detalhe, tamanho do topo, priorização explícita, higiene, ligação com objetivos, upstream e descarte, prontidão do topo e volume), propõe a limpeza e faz a triagem de novas demandas com a decisão descartar, colocar na prateleira (shelve) ou investir. Inclui um script que resume um backlog exportado em CSV (idade, itens sem tamanho, épicos no topo, duplicados). Use sempre que o usuário falar de backlog gigante, refinar o backlog, "até que ponto detalhar", backlog desorganizado, itens velhos, épicos no topo, upstream, shelve, triagem de demandas, "o que faço com tanta demanda?", Definition of Ready ou Definition of Done, ou colar uma lista de itens para limpar, mesmo sem usar a palavra saúde.
---

# Saúde do backlog: auditar, limpar e decidir o que entra

Backlog não é uma lista para guardar tudo, é um instrumento de decisão. Todo item que entra tem custo (de analisar, de manter, de olhar de novo), e todos competem entre si pelo mesmo custo de oportunidade. Quando o PO assume um produto e abre um backlog com 256 itens (já se viu um com mais de 4.000), o que ele precisa fazer é Fatiar, Descartar e Priorizar, e não sair detalhando tudo.

Esta skill audita um backlog com a mesma régua das outras (nota 0 a 100), propõe a limpeza e ajuda a decidir o destino de cada nova demanda. A skill `user-story` avalia **uma** história; esta avalia o **conjunto**.

## Escolha o modo

- **Auditar**: o usuário traz o backlog (lista, texto ou CSV) e quer saber se está saudável. Pedidos como "dá uma nota ao meu backlog", "tá bagunçado, por onde começo?".
- **Triar**: traz uma ou mais demandas novas e quer decidir o que fazer. Veja `references/upstream-e-prateleira.md`.
- **Limpar**: quer o plano de faxina (o que descartar, fatiar, refinar, juntar).
- **Auditar e limpar** (o mais comum): faça a auditoria e entregue o plano.

Responda no idioma do usuário (padrão: português do Brasil), com tom de mentor.

## Como pensar um backlog

- **Horizonte.** Os itens do topo têm mais detalhe e os de baixo têm gradualmente menos, como as ruas que enxergamos de perto e os prédios que só enxergamos a distância. Detalhar o que está longe gera desperdício se mudarmos de direção, custa mais, força decisões antes da hora e cria um backlog ingerenciável. Planejamento é saber que é preciso mudar a rota.
- **Refinamento não é uma reunião.** São etapas do fluxo antes do compromisso (o upstream): piscina de opções, refinamento, estimativa, priorização, ponto de comprometimento. Todo trabalho que exige esforço do time precisa estar mapeado, ou vira trabalho escondido.
- **Três destinos para cada demanda no upstream:** descartar (esforço alto demais para o retorno), colocar na prateleira (importante, mas faltam informação ou recursos; é estado temporário, com limite e prazo) ou investir (continua refinando até o ponto de comprometimento).
- **Estimar serve a cinco Ps:** previsibilidade, produtividade, priorização (o esforço é o denominador do ROI), particionamento (o time avisa que o item é épico e precisa ser fatiado) e partilha (a conversa técnica alinha o que será feito). Estimativa não é promessa e perde valor se consome muito tempo.
- **Critérios de aceitação e Definição de Pronto são coisas diferentes.** Critérios de aceitação são específicos de cada item; a Definição de Pronto é o acordo geral do time sobre o que "pronto" significa para qualquer item.
- **Desenhe bem o cartão (ticket design).** Com as informações certas (critérios de aceitação, tipo de demanda, políticas explícitas), o item ganha clareza rápida sem depender de reuniões longas.

## Modo auditar

1. **Se o backlog veio em CSV e você puder executar código**, rode o script e use os números como evidência: `python3 ${CLAUDE_SKILL_DIR}/scripts/analisar_backlog.py backlog.csv` (as colunas reconhecidas estão no início do arquivo; `scripts/exemplo-backlog.csv` serve de modelo). No chat do claude.ai, use o caminho relativo `scripts/analisar_backlog.py`. Sem execução de código, estime pelo texto e diga que são estimativas.
2. Leia `references/rubrica.md`.
3. Pontue os 8 critérios de 0 a 100, com evidência (itens citados ou números do script).
4. Nota geral = soma de (nota x peso) dividida por 100. **Teto de bloqueio:** se qualquer critério ficar abaixo de 40, a nota geral não passa de 69.
5. Faixas: 85 a 100 Saudável; 70 a 84 Quase lá; 50 a 69 Precisa de faxina; 0 a 49 Reescrever o backlog.

| # | Critério | Peso |
|---|---|---|
| 1 | Horizonte de detalhe | 14 |
| 2 | Tamanho do topo | 14 |
| 3 | Priorização explícita | 14 |
| 4 | Higiene (duplicados, obsoletos, idade) | 12 |
| 5 | Ligação com objetivos e métricas | 12 |
| 6 | Upstream e descarte | 12 |
| 7 | Prontidão do topo | 14 |
| 8 | Volume gerenciável | 8 |

Calibre com rigor: backlogs reais costumam ficar entre 30 e 65. Reserve 90 ou mais para um backlog que você entregaria a um PO novo amanhã.

### Formato de saída

```
## Saúde do backlog: [produto ou time]

**Nota geral: NN/100** (faixa)

### 1. Notas por critério
| Critério (peso) | Nota | Por quê (evidência) | Como melhorar |
|---|---|---|---|

### 2. O que mais pesa
### 3. Plano de faxina
| Ação | Itens | Por quê |
|---|---|---|
(descartar, colocar na prateleira com prazo, fatiar, juntar duplicados, refinar o topo)

### 4. Regras para manter o backlog saudável
(horizonte, limite da prateleira, política de entrada, definição de pronto)

### 5. Perguntas e suposições
```

Se o usuário pedir só a nota, entregue as seções 1 e 2. Não apague nada por conta própria: proponha, e deixe a decisão ao PO.

## Modo limpar e triar

- **Descarte é saúde.** Item que ninguém defende com um resultado esperado vai para descartar ou para a prateleira com data de expiração.
- **Prateleira não é segundo backlog.** Tem capacidade limitada, custo de revisão e prazo de validade; ao vencer sem decisão, o item é descartado.
- **Fatie os épicos do topo** com a skill `user-story` ou `udd-fatiamento` antes de comprometer o time.
- **Junte duplicados** e itens que só fazem sentido juntos.
- **Cada item do topo tem um porquê:** a que objetivo ou métrica ele serve.

Para priorizar o que sobrou, use `priorizacao`. Para ver uma auditoria completa, leia `references/exemplo.md`.
