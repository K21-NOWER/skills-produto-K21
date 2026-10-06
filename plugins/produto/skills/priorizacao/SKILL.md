---
name: priorizacao
description: Ajuda Product Owners e Product Managers a priorizar uma lista de atividades (funcionalidades, user stories, ideias, projetos, iniciativas) com critério e explicação. Escolhe o método certo para o contexto (RICE, ICE, Valor x Esforço, MoSCoW, Kano, WSJF e Custo do Atraso ou matriz ponderada), pontua cada item de forma transparente, ordena, explica por que cada item ficou onde ficou, mostra o que mudaria a ordem e separa o que fazer agora, depois e descartar. Use sempre que o usuário pedir para priorizar, ordenar o backlog, decidir o que fazer primeiro, montar um roadmap, escolher entre iniciativas, aplicar RICE, ICE, MoSCoW, WSJF ou Kano, ou perguntar "o que eu faço primeiro?", "como priorizar isso?", "qual desses vale mais a pena?", mesmo que não cite nenhum método.
---

# Priorização

Priorizar é escolher em função de um objetivo. Sem direção, qualquer ordem serve. Esta skill ajuda um Product Owner ou Product Manager a ordenar uma lista de atividades de forma criteriosa e, principalmente, **bem explicada**: quem vê o resultado precisa entender por que cada item ficou onde ficou e o que faria a ordem mudar.

Nenhum método de priorização é o certo. Cada um responde a uma pergunta diferente e tem pontos cegos. Por isso o trabalho aqui é escolher o método pelo contexto, usar com transparência e testar o resultado.

## Princípios (e por que importam)

1. **Sem objetivo, não há prioridade.** Todo método pontua "valor", e valor só existe em relação a um objetivo (a meta do trimestre, o problema do cliente, a restrição do prazo). Sempre deixe o objetivo explícito no topo da resposta.
2. **O método é um meio, não uma verdade.** Escolha pelo contexto e, quando a decisão for cara, confira com um segundo método. Onde os dois discordam está a conversa que vale ter.
3. **Transparência vale mais que precisão.** Cada número deve mostrar de onde veio: dado real ou estimativa. Um número inventado com cara de dado é pior do que não ter número, porque as pessoas passam a defender a conta em vez de discutir a premissa.
4. **Priorizar inclui dizer não.** A lista termina com o que será descartado ou adiado, com razão. Fatiar, descartar e priorizar é um dos princípios do UDD (Usage-Driven Development) da K21: o que não cabe agora não precisa ficar apodrecendo no backlog.
5. **A nota organiza a conversa, quem decide é o PO.** O resultado é uma recomendação fundamentada, não uma ordem automática. Mostre onde a decisão depende de julgamento humano.

## Fluxo

### 1. Entender o contexto

Levante, ou assuma e declare:

- **Objetivo do período** (meta, OKR, problema a resolver). É a pergunta mais importante.
- **Capacidade e prazo** (pessoas-mês disponíveis, data de entrega).
- **Restrições** (obrigações legais, datas fixas, dependências entre itens).
- **Estágio e dados** (há usuários? há métricas? ou é tudo estimativa?).
- **Quem decide** e quem é afetado.

Se o usuário só entregou a lista, **não bloqueie**: declare suas suposições de objetivo e capacidade na primeira linha da resposta, entregue a priorização e mostre como ela mudaria se a suposição estiver errada. Faça no máximo três perguntas, e só se a resposta mudar o resultado de forma importante.

Se o usuário pedir só "o que faço primeiro?" com poucos itens, responda de forma curta (a ordem, os dois motivos principais, o que mudaria o resultado) e ofereça a análise completa.

### 2. Preparar a lista

- Escreva cada item em **uma linha**, no formato "resultado desejado", não "tarefa". Separe o "o quê" do "como".
- **Junte duplicados** e itens que só fazem sentido juntos (se dois itens entregam valor só em conjunto, são uma fatia).
- **Itens grandes demais** (épicos) distorcem qualquer método: sugira fatiar com a skill `user-story` antes de pontuar.
- **Itens que são apostas incertas** (confiança baixa, ninguém sabe se funciona) são hipóteses: sugira testar com a skill `hipoteses` em vez de forçar uma nota.
- **Obrigações não competem pela mesma régua.** Correções críticas, segurança, compliance e incidentes entram antes como "obrigatório", e dívida técnica e manutenção costumam ter capacidade reservada (muitos times separam 10 a 20%). Pontue só o que de fato precisa competir.
- Com **mais de 25 itens**, faça uma triagem rápida (Valor x Esforço ou ICE) e pontue só os finalistas com o método principal.

### 3. Escolher o método

Leia `references/metodos.md` para fórmulas, escalas e pontos cegos de cada método. Use esta tabela para decidir:

| Situação | Método principal | Por quê |
|---|---|---|
| Produto com usuários e alguma métrica; muitos candidatos; precisa comparar com número | **RICE** | Considera alcance e confiança, não só impacto |
| Produto novo, poucos dados, ritmo rápido, backlog de experimentos | **ICE** | Leve, tolera estimativa grosseira |
| Workshop com stakeholders; precisa de algo visual e rápido | **Valor x Esforço** | Fácil de explicar e de discutir em grupo |
| Escopo fechado: release, MVP, prazo regulatório | **MoSCoW** | Define o mínimo viável do release |
| Entender como o cliente percebe as funcionalidades | **Kano** | Separa o obrigatório do que encanta |
| O custo de esperar é desigual (prazos, janelas, riscos); várias equipes | **WSJF / Custo do Atraso** | Sequencia pelo custo de adiar dividido pelo tamanho |
| Vários objetivos ou critérios estratégicos próprios | **Matriz ponderada** | Traduz a estratégia da empresa em critérios e pesos |

Explique a escolha em duas ou três frases ("usei RICE porque há dados de uso e muitos candidatos; usei Valor x Esforço como contraprova visual"). Use **no máximo dois métodos**: o segundo serve de contraprova, não de concorrente. Combinações úteis: MoSCoW para cortar e RICE para ordenar dentro de cada grupo; ICE para triar e RICE nos finalistas.

### 4. Pontuar

- Use as escalas de `references/metodos.md` e **a mesma escala e o mesmo período para todos os itens**.
- **Marque a origem de cada estimativa:** `D` (dado fornecido ou medido) ou `E` (estimativa sua, suposição). Pontue com faixas de referência e não com falsa precisão: "Alcance 4.000" ou "Alcance 4.137" dão o mesmo resultado prático, mas o segundo finge saber o que não sabe.
- **Calcule com cuidado.** Se puder executar código, grave os itens em um JSON temporário e rode o script `scripts/calcular.py` (o formato do JSON está no início do arquivo, e `scripts/exemplo-rice.json` serve de modelo): `python3 ${CLAUDE_SKILL_DIR}/scripts/calcular.py rice itens.json`. No chat do claude.ai, a pasta da skill é copiada para o ambiente de execução, então use o caminho relativo `scripts/calcular.py`. Confira um item à mão. Se não puder executar código, calcule manualmente mostrando a fórmula.
- **Itens de confiança baixa** (50% ou menos): pontue, mas sinalize. Alto impacto com baixa confiança é sinal para experimentar antes de construir.

### 5. Ordenar e testar a sanidade

Antes de entregar, confira:

- **A ordem faz sentido?** Se um item que parece óbvio ficou em último, ou o contrário, o método ou a estimativa pode estar errado. Investigue antes de defender o número.
- **Dependências.** Um item de nota baixa que destrava os de nota alta sobe na ordem. Itens que só funcionam juntos viram um bloco.
- **Capacidade.** Some o esforço em ordem e trace a **linha de corte**: o que cabe na capacidade informada. Itens abaixo da linha vão para "depois" ou "descartar".
- **Sensibilidade.** Quais duas ou três estimativas, se mudassem um nível, trocariam a ordem? São elas que merecem validação.
- **Equilíbrio.** A lista é só ganho rápido, só aposta grande ou só itens de um tipo? Uma carteira saudável mistura.
- **Vieses.** Opinião do mais sênior, projeto de estimação, efeito de recência. Se um item está alto por convicção e não por dado, diga.

### 6. Explicar e recomendar

Entregue no formato abaixo.

## Formato de saída

```
## Priorização: [nome da lista ou do produto]

**Objetivo considerado:** [...]  ·  **Capacidade:** [...]  ·  **Restrições:** [...]
**Suposições:** [o que foi assumido e que, se estiver errado, muda a ordem]
**Método:** [nome] porque [razão em uma frase]. Contraprova: [método, se houver].

### Ranking
| # | Item | Nota | [colunas do método] | Origem (D/E) | Grupo |
|---|---|---|---|---|---|
(grupo: Fazer agora, Próximo, Depois ou Descartar; marque a linha de corte da capacidade)

### Por que está nessa ordem
(para os 5 primeiros: o que mais pesou na nota, em uma ou duas frases; para os demais, uma linha)

### O que pode mudar essa ordem
(2 ou 3 estimativas mais sensíveis e o que acontece se mudarem; ex.: "se o impacto do item 1 cair de 3 para 2, o item 2 passa à frente")

### Recomendação
- **Fazer agora:** ...
- **Próximo:** ...
- **Depois:** ...
- **Descartar (com a razão):** ...

### Pontos de atenção
(dependências, itens de confiança baixa que pedem experimento com a skill `hipoteses`, itens grandes que pedem fatiamento com a skill `user-story`, vieses percebidos)

### Decisões que são suas
(as 2 ou 3 perguntas ou dados que mais mudariam o resultado)
```

Para a explicação de cada item, fale do **motivo**, não da conta: "alto porque alcança toda a base e ataca diretamente a meta de reduzir faltas", e não "porque 4000 x 3 x 0,8 dividido por 1,5". A conta fica na tabela, a razão fica no texto.

## Tom

Aja como um mentor que ajuda a pensar, não como uma calculadora que decreta. Se o usuário discordar do resultado, trate a discordância como informação: pode ser uma estimativa errada, um objetivo diferente do assumido ou um critério que faltou. Mostre qual, ajuste e recalcule. Para ver uma análise completa, leia `references/exemplo.md`.
