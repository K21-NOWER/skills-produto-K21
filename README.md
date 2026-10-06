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

Escolha o caminho pelo app e pelo plano que você usa:

| Eu uso... | Caminho |
|---|---|
| Claude no site, no app desktop ou no Cowork, com plano pago (Pro, Max, Team ou Enterprise) | **Opção 1**: adiciona o repositório como marketplace e instala o plugin. As 4 skills de uma vez |
| Claude Code (terminal, VS Code ou aba Code do app) | **Opção 2**: 2 comandos |
| Claude com plano Free | **Opção 3**: 1 arquivo `.zip` |
| Quero só uma das skills | **Opção 4**: o `.zip` daquela skill |

### Opção 1: marketplace no Claude (plano pago)

Passo a passo testado no claude.ai. O caminho é o mesmo no app desktop e no Cowork. Os nomes dos menus podem aparecer traduzidos.

1. Abra o Claude e vá em **Customize**, na aba **Plugins**.
2. Clique em **Add**, escolha **Add marketplace** e depois **Add from a repository**.
3. No campo de endereço, escolha `skills-produto-K21` na lista (ela mostra os seus repositórios do GitHub) ou digite `K21-NOWER/skills-produto-K21`, e clique em **Sync**.
4. Quando o plugin **Produto** aparecer, clique em **Add**. O Claude confirma com "Produto is installed and ready to use".

Pronto: as quatro skills ficam em **Customize > Skills** e o Claude as usa quando o seu pedido combina. Para chamar uma na mão, digite `/` no chat e escolha a skill.

Se aparecer o aviso "Auto-sync requires the Claude GitHub App...", o plugin funciona normalmente. O aviso só diz que a atualização automática depende de você dar acesso ao app (botão **Grant access**). Sem isso, você continua com a versão que instalou.

O plugin fica na sua conta, então também chega ao Cowork e ao Claude Code. Prefere um arquivo em vez do marketplace? Baixe `produto-plugin.zip` na página de [Releases](https://github.com/K21-NOWER/skills-produto-K21/releases) e use **Add > Upload plugin**.

### Opção 2: Claude Code

Dois comandos:

```
/plugin marketplace add K21-NOWER/skills-produto-K21
```

```
/plugin install produto@k21-produto
```

No terminal, os equivalentes são `claude plugin marketplace add K21-NOWER/skills-produto-K21` e `claude plugin install produto@k21-produto`. Depois é só pedir em linguagem natural, ou chamar uma skill pelo nome, por exemplo `/produto:user-story`. Para atualizar: `/plugin marketplace update k21-produto`.

Sem plugin, também dá para copiar a pasta de uma skill, de `plugins/produto/skills/`, para `~/.claude/skills/`.

### Opção 3: um arquivo só, qualquer plano

Serve principalmente para quem está no plano Free, já que a documentação oficial indica plugins para planos pagos.

1. Ative a execução de código: em **Settings > Capabilities**, ligue "Code execution and file creation". Skills precisam disso.
2. Baixe `produto-k21.zip` na página de [Releases](https://github.com/K21-NOWER/skills-produto-K21/releases).
3. Vá em **Customize > Skills**, clique em **+**, depois em **Create skill** e **Upload a skill**, e envie o arquivo. Ative a skill.

O `produto-k21.zip` junta as quatro skills em uma só, chamada `produto-k21`, que escolhe sozinha o modo certo para o seu pedido. Nos planos Team e Enterprise, o Owner da organização controla se skills e plugins podem ser adicionados.

### Opção 4: uma skill por vez

Baixe só o `.zip` da skill que quiser (`user-story.zip`, `visao-do-produto.zip`, `priorizacao.zip` ou `hipoteses.zip`) na página de Releases e envie como na Opção 3. Lembre que a `hipoteses` usa a `user-story` para gerar a story, e a `priorizacao` sugere usar as outras duas, então vale instalar juntas.

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
  README.md, LICENSE                exigidos para listar o plugin no diretório do Claude
  skills/
    user-story/                     SKILL.md + references/
    visao-do-produto/               SKILL.md + references/
    priorizacao/                    SKILL.md + references/ + scripts/
    hipoteses/                      SKILL.md + references/
pacote-unico/SKILL.md               roteador do pacote único (produto-k21.zip)
scripts/empacotar.py                valida e gera os .zip em dist/
```

## Para quem mantém o repositório

- **Gerar os arquivos da Release:** `python3 scripts/empacotar.py`. O script valida frontmatter, nomes, tamanho das descrições e caminhos, e só então gera 6 arquivos em `dist/`: um `.zip` por skill, o `produto-k21.zip` (pacote único) e o `produto-plugin.zip` (plugin completo).
- **Fonte única da verdade:** o pacote único é montado a partir das quatro skills de `plugins/produto/skills/`, mais o roteador `pacote-unico/SKILL.md`. Edite só esses arquivos, nunca o `.zip`.
- **Atualizações:** no Claude Code, quem usa o marketplace acompanha o `main`. No claude.ai, a atualização automática só chega para quem der ao Claude GitHub App acesso ao repositório; sem isso, a pessoa fica na versão instalada. Quem enviou um `.zip` só atualiza ao enviar de novo, então publique uma Release nova a cada mudança relevante.
- O plugin não define `version`: o Claude Code acompanha os commits. Se um dia quiser fixar versões, defina `version` no `plugin.json` e aumente a cada publicação, ou os alunos não recebem as mudanças.
- **O que já foi testado:** marketplace, instalação do plugin e uma avaliação real de user story no claude.ai (plano Pro). Os uploads de `.zip` (`produto-plugin.zip` e `produto-k21.zip`) foram validados só na estrutura, e a atualização automática e o plano Free ainda não foram testados.

## Feedback

Achou uma nota estranha, uma explicação confusa ou quer sugerir uma skill nova? Abra uma [issue](https://github.com/K21-NOWER/skills-produto-K21/issues).

## Licença

[MIT](LICENSE). Use, adapte e compartilhe, mantendo o aviso de copyright.
