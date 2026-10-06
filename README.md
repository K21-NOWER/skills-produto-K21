# Skills de Produto | K21 e Nower

Quatro skills em português para o Claude que ajudam quem trabalha com produto a **escrever melhor, decidir melhor e testar antes de construir**. Feitas para os alunos da K21 e da Nower, de graça e abertas para todo mundo usar.

Uma *skill* é um pacote de instruções que o Claude carrega sozinho quando o seu pedido combina com ela. Você não precisa decorar comandos: descreva o que quer e o Claude usa a skill certa.

## As skills

| Skill | O que faz | Exemplo de pedido |
|---|---|---|
| **user-story** | Dá notas de 0 a 100 para uma user story (persona, valor, clareza, tamanho, critérios de aceitação e mais), diz se precisa fatiar, e transforma ideias em stories com critérios de aceitação | "Avalia essa story e melhora: *Como usuário, quero gerenciar meus pedidos, para ter mais controle.*" |
| **visao-do-produto** | Avalia uma visão de produto com notas por critério e cria visão, posicionamento e Product Vision Board a partir de uma ideia | "Dá uma nota para a visão do meu produto e me diz como melhorar: ..." |
| **priorizacao** | Escolhe o método certo (RICE, ICE, MoSCoW, Kano, WSJF, Valor x Esforço ou matriz ponderada), pontua, ordena e explica por que cada item ficou onde ficou | "Tenho 8 ideias e 6 pessoas-mês neste trimestre. A meta é reduzir o churn. Me ajuda a priorizar: ..." |
| **hipoteses** | Avalia hipóteses, sugere experimentos, métricas e riscos, monta um Test Card e transforma a hipótese em user story com critérios de aceitação | "Acho que se a gente enviar lembrete por WhatsApp, as faltas caem. Avalia, sugere como testar e escreve a story." |

Todas respondem em português do Brasil por padrão, explicam o raciocínio e mostram de onde veio cada nota.

## Como instalar

### Opção 1: Claude Code (recomendada)

Dois comandos, e você recebe as atualizações quando elas forem publicadas:

```
/plugin marketplace add K21-Nower/skills-produto-K21
/plugin install produto@k21-produto
```

Se preferir o terminal, os equivalentes são `claude plugin marketplace add K21-Nower/skills-produto-K21` e `claude plugin install produto@k21-produto`.

Depois é só pedir em linguagem natural, ou chamar uma skill pelo nome, por exemplo `/produto:user-story`.

Para atualizar:

```
/plugin marketplace update k21-produto
```

### Opção 2: Claude.ai e Claude Desktop

1. Baixe o `.zip` de cada skill que quiser na página de [Releases](https://github.com/K21-Nower/skills-produto-K21/releases).
2. No Claude, abra **Configurações**, vá em **Capacidades** (Capabilities) e **Skills**, e envie o arquivo `.zip`. Os nomes dos menus podem variar conforme a versão do aplicativo.
3. Ative a skill.

### Opção 3: copiar a pasta (Claude Code, sem plugin)

Copie a pasta da skill desejada, de `plugins/produto/skills/`, para `~/.claude/skills/`.

## Um fluxo de trabalho possível

As quatro skills funcionam sozinhas, mas foram feitas para conversar entre si:

```mermaid
flowchart LR
    V["Visão do produto"] --> H["Hipóteses"]
    H --> P["Priorização"]
    P --> U["User stories"]
    U --> A["Uso e aprendizado"]
    A --> H
```

1. A **visão** aponta a direção e lista as premissas que precisam ser verdade.
2. As **hipóteses** transformam cada premissa de risco em um experimento barato, com métrica e critério definidos antes.
3. A **priorização** ordena o que fazer primeiro, em função do objetivo.
4. As **user stories** transformam o que vale construir em fatias pequenas e testáveis.
5. O **uso** ensina algo, e o ciclo recomeça.

A skill de hipóteses chama a skill de user-story para gerar a story, e a de priorização sugere fatiar (user-story) ou testar (hipóteses) os itens que pedem isso.

## Como as notas funcionam

As skills de **user story**, **visão do produto** e **hipóteses** avaliam com a mesma lógica:

- Cada critério recebe uma nota de **0 a 100**, com uma justificativa que cita um trecho do seu texto.
- A **nota geral** é uma média ponderada: os critérios que mais impedem o time de avançar pesam mais.
- Há um **teto de bloqueio**: se algum critério fica abaixo de 40, a nota geral não passa de 69. Uma média alta não pode esconder um furo grave.
- As notas seguem uma rubrica com âncoras escritas (veja a pasta `references/` de cada skill), para ficarem comparáveis de uma avaliação para outra.

A nota é um **guia para a conversa**, não um veredito. O objetivo é você entender o porquê e melhorar, e não perseguir 100.

## Um exemplo para acompanhar

Todos os exemplos dos arquivos `references/` usam o mesmo produto fictício: um app de agendamento para clínicas pequenas, com a meta de reduzir as faltas dos pacientes. Dá para ler a visão, a priorização, a hipótese e a story em sequência e ver como uma coisa leva à outra.

## Estrutura do repositório

```
.claude-plugin/marketplace.json     catálogo do marketplace de plugins
plugins/produto/
  .claude-plugin/plugin.json        metadados do plugin
  skills/
    user-story/                     SKILL.md + references/
    visao-do-produto/               SKILL.md + references/
    priorizacao/                    SKILL.md + references/ + scripts/
    hipoteses/                      SKILL.md + references/
scripts/empacotar.sh                gera um .zip por skill, em dist/
```

## Para quem mantém o repositório

- Para gerar os `.zip` e anexar a uma Release: `./scripts/empacotar.sh`.
- O plugin não define `version`: quem instala acompanha os commits. Se um dia quiser fixar versões, defina `version` no `plugin.json` e lembre de aumentá-la a cada publicação, ou os alunos não recebem as mudanças.
- Antes de publicar uma mudança grande, rode os exemplos de `references/` em cada skill e compare com a saída esperada.

## Feedback

Achou uma nota estranha, uma explicação confusa ou quer sugerir uma skill nova? Abra uma [issue](https://github.com/K21-Nower/skills-produto-K21/issues).

## Licença

[MIT](LICENSE). Use, adapte e compartilhe, mantendo o aviso de copyright.
