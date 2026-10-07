# Skills de Produto | K21 e Nower

[![Testes](https://github.com/K21-NOWER/skills-produto-K21/actions/workflows/testes.yml/badge.svg)](https://github.com/K21-NOWER/skills-produto-K21/actions/workflows/testes.yml) [![Licença MIT](https://img.shields.io/badge/licen%C3%A7a-MIT-green.svg)](LICENSE) [![Release](https://img.shields.io/github/v/release/K21-NOWER/skills-produto-K21)](https://github.com/K21-NOWER/skills-produto-K21/releases)

14 skills em português para o Claude que ajudam quem trabalha com produto a **escrever melhor, decidir melhor e testar antes de construir**, com base na metodologia da K21 (UDD, Test Card 2.0, Matriz RUT, Tanque de Decantação e outras). Feitas para os alunos da K21 e da Nower, de graça e abertas para todo mundo usar.

Uma *skill* é um pacote de instruções que o Claude carrega sozinho quando o seu pedido combina com ela. Você não precisa decorar comandos: descreva o que quer e o Claude usa a skill certa.

## As skills

**Escrever e fatiar**

| Skill | O que faz | Exemplo de pedido |
|---|---|---|
| **user-story** | Dá notas de 0 a 100 para uma user story (checklist da saúde da história em 9 passos da K21), diz se precisa fatiar e transforma ideias em stories com critérios de aceitação | "Avalia essa story e melhora: *Como usuário, quero gerenciar meus pedidos, para ter mais controle.*" |
| **udd-fatiamento** | Transforma uma ideia em plano UDD: epicentro, fatias verticais, sinal de uso por fatia, regra de expansão e o que descartar | "Quero lançar um app de pedidos. Me ajuda a fatiar no estilo UDD." |
| **saude-do-backlog** | Audita o backlog com nota por critério, propõe a limpeza e faz a triagem de demandas (descartar, prateleira ou investir). Lê um CSV exportado | "Aqui está meu backlog em CSV. Qual é a saúde dele?" |

**Direção e estratégia**

| Skill | O que faz | Exemplo de pedido |
|---|---|---|
| **visao-do-produto** | Avalia uma visão com notas por critério e cria visão, posicionamento e Product Vision Board (ou Tanque de Decantação) a partir de uma ideia | "Dá uma nota para a visão do meu produto e me diz como melhorar: ..." |
| **estrategia-e-roadmap** | Constrói e avalia estratégia e roadmap: Tanque de Decantação, Matriz de Estratégia, Bússola, Radar e roadmap enxuto | "Avalia meu roadmap e reescreve como Tanque de Decantação." |
| **okr** | Avalia, escreve e acompanha OKRs; diagnostica as 10 disfunções mais comuns | "Escreva meus OKRs do trimestre e diga o que está fraco." |
| **metricas-de-produto** | Avalia ou escolhe métricas: North Star, principal, de equilíbrio, Métricas do Pirata e fórmulas | "Quais métricas devo acompanhar no meu produto de assinatura?" |

**Decidir e validar**

| Skill | O que faz | Exemplo de pedido |
|---|---|---|
| **priorizacao** | Escolhe o método (RICE, ICE, Matriz RUT, MoSCoW, Kano, WSJF, Valor x Esforço ou ponderada), pontua, ordena e explica | "Tenho 8 ideias e 6 pessoas-mês neste trimestre. A meta é reduzir o churn. Me ajuda a priorizar: ..." |
| **hipoteses** | Avalia hipóteses, sugere experimentos, métricas e riscos, monta o Test Card 2.0 e o Learning Card e gera a user story | "Acho que se a gente enviar lembrete por WhatsApp, as faltas caem. Avalia, sugere como testar e escreve a story." |
| **discovery-com-clientes** | Prepara roteiros de entrevista (Teste da Mãe), sintetiza notas e transcrições, monta Mapa de Empatia e personas | "Prepara o roteiro de entrevista para descobrir por que os clientes cancelam." |
| **riscos-e-vieses** | Pré-mortem, detecção de vieses cognitivos, mapa de riscos e Matriz de Hipóteses | "Faz um pré-mortem do lançamento do mês que vem." |

**Entregar e comunicar**

| Skill | O que faz | Exemplo de pedido |
|---|---|---|
| **previsibilidade** | Responde "quando fica pronto?" e "quanto cabe até a data?" com Monte Carlo sobre o histórico do time, e avalia promessas de prazo | "São 30 itens e entregamos 3, 2, 5, 4, 3, 2, 4, 3 por semana. Quando termina?" |
| **papel-de-produto** | Autodiagnóstico de PO, PM ou GPM (7 arquétipos, disfunções), comparação de papéis e plano de evolução | "Faz meu diagnóstico como PO: ..." |
| **apresentacao-de-produto** | Cria e avalia apresentações enxutas: 4 slides, pitch, Sprint Review e data storytelling | "Monta a Sprint Review focada em feedback do cliente." |

Todas respondem em português do Brasil por padrão, explicam o raciocínio e mostram de onde veio cada nota.

## Como instalar

Escolha o caminho pelo app e pelo plano que você usa:

| Eu uso... | Caminho |
|---|---|
| Claude no site, no app desktop ou no Cowork, com plano pago (Pro, Max, Team ou Enterprise) | **Opção 1**: adiciona o repositório como marketplace e instala o plugin. As 14 skills de uma vez |
| Claude Code (terminal, VS Code ou aba Code do app) | **Opção 2**: 2 comandos |
| Claude com plano Free | **Opção 3**: 1 arquivo `.zip` |
| Quero só uma das skills | **Opção 4**: o `.zip` daquela skill |

### Opção 1: marketplace no Claude (plano pago)

Passo a passo testado no claude.ai. O caminho é o mesmo no app desktop e no Cowork. Os nomes dos menus podem aparecer traduzidos.

1. Abra o Claude e vá em **Customize**, na aba **Plugins**.
2. Clique em **Add**, escolha **Add marketplace** e depois **Add from a repository**.
3. No campo de endereço, escolha `skills-produto-K21` na lista (ela mostra os seus repositórios do GitHub) ou digite `K21-NOWER/skills-produto-K21`, e clique em **Sync**.
4. Quando o plugin **Produto** aparecer, clique em **Add**. O Claude confirma com "Produto is installed and ready to use".

Pronto: as 14 skills ficam em **Customize > Skills** e o Claude as usa quando o seu pedido combina. Para chamar uma na mão, digite `/` no chat e escolha a skill.

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

O `produto-k21.zip` junta as 14 skills em uma só, chamada `produto-k21`, que escolhe sozinha o modo certo para o seu pedido. Nos planos Team e Enterprise, o Owner da organização controla se skills e plugins podem ser adicionados.

### Opção 4: uma skill por vez

Baixe só o `.zip` da skill que quiser (por exemplo `user-story.zip`, `okr.zip` ou `previsibilidade.zip`; há um por skill) na página de Releases e envie como na Opção 3. Algumas skills sugerem outras: a `hipoteses` usa a `user-story` para gerar a story, e a `priorizacao` sugere `saude-do-backlog`, `user-story` e `hipoteses`, então vale instalar juntas.

## Um fluxo de trabalho possível

As skills funcionam sozinhas, mas foram feitas para conversar entre si. O núcleo do fluxo:

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

A skill de hipóteses chama a skill de user-story para gerar a story, e a de priorização sugere fatiar (user-story) ou testar (hipóteses) os itens que pedem isso. As demais entram ao redor desse núcleo: **discovery-com-clientes** alimenta a visão, **estrategia-e-roadmap**, **okr** e **metricas-de-produto** dão direção e medida, **udd-fatiamento** e **saude-do-backlog** mantêm o trabalho fatiado e limpo, **previsibilidade** diz quando fica pronto, **riscos-e-vieses** protege as decisões, e **papel-de-produto** e **apresentacao-de-produto** apoiam quem conduz tudo isso.

## Como as notas funcionam

As skills que avaliam (**user story**, **visão do produto**, **hipóteses**, **métricas**, **OKR**, **saúde do backlog**, **estratégia e roadmap**, **discovery**, **apresentação**, **riscos e vieses**, entre outras) usam a mesma lógica:

- Cada critério recebe uma nota de **0 a 100**, com uma justificativa que cita um trecho do seu texto.
- A **nota geral** é uma média ponderada: os critérios que mais impedem o time de avançar pesam mais.
- Há um **teto de bloqueio**: se algum critério fica abaixo de 40, a nota geral não passa de 69. Uma média alta não pode esconder um furo grave.
- As notas seguem uma rubrica com âncoras escritas (veja a pasta `references/` de cada skill), para ficarem comparáveis de uma avaliação para outra.

A nota é um **guia para a conversa**, não um veredito. O objetivo é você entender o porquê e melhorar, e não perseguir 100.

## Um exemplo para acompanhar

Os exemplos dos arquivos `references/` usam quase sempre o mesmo produto fictício: um app de agendamento para clínicas pequenas, com a meta de reduzir as faltas dos pacientes. Dá para ler a visão, a priorização, a hipótese e a story em sequência e ver como uma coisa leva à outra.

## Estrutura do repositório

```
.claude-plugin/marketplace.json     catálogo do marketplace de plugins
plugins/produto/
  .claude-plugin/plugin.json        metadados do plugin
  README.md, LICENSE                exigidos para listar o plugin no diretório do Claude
  skills/
    user-story/ visao-do-produto/ priorizacao/ hipoteses/
    metricas-de-produto/ udd-fatiamento/ okr/ saude-do-backlog/
    previsibilidade/ papel-de-produto/ discovery-com-clientes/
    estrategia-e-roadmap/ apresentacao-de-produto/ riscos-e-vieses/
                                    cada uma: SKILL.md + references/ (+ scripts/ em
                                    priorizacao, saude-do-backlog e previsibilidade)
pacote-unico/SKILL.md               roteador do pacote único (produto-k21.zip)
scripts/empacotar.py                valida e gera os .zip em dist/
scripts/testar.py, tests/           testes automáticos (scripts, estrutura, acionamento, empacotamento)
.github/                            workflow de testes, modelos de issue e de pull request
CONTRIBUTING.md, CODE_OF_CONDUCT.md, CHANGELOG.md
```

## Para quem mantém o repositório

- **Testar antes de publicar:** `python3 scripts/testar.py` roda os testes dos scripts (contas conferidas à mão e entradas inválidas), da estrutura das skills (frontmatter, rubricas, pesos, referências), do acionamento (aproximado) e o empacotamento. O GitHub roda o mesmo em todo pull request.
- **Gerar os arquivos da Release:** `python3 scripts/empacotar.py`. O script valida frontmatter, nomes, tamanho das descrições, caminhos e se o roteador do pacote único lista todas as skills, e só então gera 16 arquivos em `dist/`: um `.zip` por skill (14), o `produto-k21.zip` (pacote único) e o `produto-plugin.zip` (plugin completo).
- **Fonte única da verdade:** o pacote único é montado a partir das skills de `plugins/produto/skills/`, mais o roteador `pacote-unico/SKILL.md`. Edite só esses arquivos, nunca o `.zip`.
- **Atualizações:** no Claude Code, quem usa o marketplace acompanha o `main`. No claude.ai, a atualização automática só chega para quem der ao Claude GitHub App acesso ao repositório; sem isso, a pessoa fica na versão instalada. Quem enviou um `.zip` só atualiza ao enviar de novo, então publique uma Release nova a cada mudança relevante.
- O plugin não define `version`: o Claude Code acompanha os commits. Se um dia quiser fixar versões, defina `version` no `plugin.json` e aumente a cada publicação, ou os alunos não recebem as mudanças.
- **O que já foi testado:** no claude.ai (plano Pro), o marketplace, a instalação do plugin e uma avaliação real de user story. Na máquina de quem mantém, a bateria automática descrita acima, incluindo o conteúdo dos zips da Release. Ainda não foram testados no claude.ai: o upload dos `.zip` (`produto-plugin.zip` e `produto-k21.zip`), a atualização automática, o plano Free e as skills novas em conversas reais. Se você testar, conte numa [issue](https://github.com/K21-NOWER/skills-produto-K21/issues/new/choose).

## Feedback

Achou uma nota estranha, uma explicação confusa ou quer sugerir uma skill nova? Abra uma [issue](https://github.com/K21-NOWER/skills-produto-K21/issues/new/choose) (há um modelo para cada caso) e veja o [guia de contribuição](CONTRIBUTING.md).

## Licença

[MIT](LICENSE). Use, adapte e compartilhe, mantendo o aviso de copyright.
