# Rubrica de avaliação de user stories

Use este arquivo para pontuar. Cada critério tem quatro faixas com descritores. Escolha a faixa pelos sinais que o texto realmente mostra e, dentro da faixa, ajuste a nota pela quantidade de sinais: mais sinais positivos, nota mais alta; mais sinais negativos, nota mais baixa. Se não há texto que sustente uma nota, a nota não sobe.

Conteúdo: 1 Persona · 2 Valor · 3 Efetividade · 4 Clareza · 5 Foco no problema · 6 Tamanho · 7 Critérios de aceitação · 8 Independência · 9 Estimabilidade

---

## 1. Persona (peso 8)

**Pergunta:** dá para imaginar uma pessoa real, num contexto real, querendo isso?

| Faixa | Descritor |
|---|---|
| 90-100 | Personagem com nome e característica ou contexto que influencia a solução e gera empatia. Ex.: "Eu, enquanto Valdir Detalhista" ou "Como recepcionista de clínica no horário de pico" |
| 70-89 | Papel claro, mas sem o contexto que diferenciaria a solução. Ex.: "Como recepcionista" |
| 40-69 | Genérica ("Como usuário", "Como cliente"), ou plausível mas incoerente com a ação pedida |
| 0-39 | Ausente; ou é o sistema ou o time ("Como sistema", "Como desenvolvedor") numa entrega de valor ao usuário final; ou mistura várias personas |

Papéis internos (suporte, financeiro, operação) são personas válidas quando a necessidade é realmente deles.

---

## 2. Valor (peso 12)

**Pergunta:** o "para" explica um benefício real, do ponto de vista da persona?

**Teste rápido:** apague o "para ..." e releia. Se não perdeu informação, o "para" era só a paráfrase do "quero".

| Faixa | Descritor |
|---|---|
| 90-100 | Benefício concreto, na perspectiva da persona, ligado a algo que importa (tempo, dinheiro, risco, decisão, esforço evitado). Não repete o "quero" |
| 70-89 | Benefício claro, porém genérico ("para ganhar eficiência") ou sem como perceber a diferença |
| 40-69 | O "para" existe, mas é paráfrase da ação ("quero filtrar pedidos para poder filtrar") ou é vago ("para melhorar a experiência", "para tomada de decisão") |
| 0-39 | Sem "para"; ou o valor é só do time ou da tecnologia, sem ligação com o usuário ou o negócio |

---

## 3. Efetividade (peso 10)

**Pergunta:** depois de entregue, existe um sinal observável de que a story cumpriu o propósito, além de estar entregue?

Uma story pode estar perfeitamente implementada e mesmo assim não resolver nada. Este critério olha o "para", os critérios de aceitação e qualquer "sinal de sucesso" do texto.

| Faixa | Descritor |
|---|---|
| 90-100 | Indica o resultado ou o comportamento esperado, de preferência mensurável ("reduzir de 10 para 2 minutos", "80% concluem sem ajuda"), ou deixa claro o que será observado |
| 70-89 | O resultado é implícito, mas claramente observável ("o cliente consegue pagar sem sair do app") |
| 40-69 | Descreve só a existência da funcionalidade ("a tela existe", "o botão faz X"); não dá para dizer se funcionou |
| 0-39 | Nenhum resultado observável; ou o resultado esperado contradiz o valor declarado |

---

## 4. Clareza (peso 14)

**Pergunta:** duas pessoas diferentes leriam e imaginariam a mesma coisa?

Procure: termos vagos, siglas sem definição, pronomes soltos, várias ações coladas com "e" ou "ou", frases longas demais.

Termos vagos frequentes: rápido, fácil, facilmente, simples, intuitivo, amigável, moderno, flexível, robusto, eficiente, adequado, "quando necessário", "etc.", "entre outros", "gerenciar", "melhorar".

| Faixa | Descritor |
|---|---|
| 90-100 | Uma ação, vocabulário do negócio, nenhum termo vago; entendida sem contexto extra |
| 70-89 | Entendível, mas com um termo vago ou uma lacuna que vai exigir conversa |
| 40-69 | Admite mais de uma interpretação razoável, ou usa jargão ou sigla que só quem esteve na reunião entende |
| 0-39 | Incompreensível sem contexto, contraditória, ou é só um título ou uma palavra |

---

## 5. Foco no problema (peso 8)

**Pergunta:** descreve a necessidade ou já prescreve a solução?

Sinais de solução prescrita: componentes de interface (botão, dropdown, modal, aba), cores, tecnologias, tabelas, endpoints, nomes de banco, verbos de implementação ("criar tabela", "integrar API") e canal ou meio de entrega escolhido sem necessidade ("receber um **e-mail**" quando a necessidade é ser avisado: "receber um aviso" deixa e-mail, WhatsApp, banner e ligação em aberto). Passo 5 do método K21.

Restrições reais (lei, integração obrigatória com sistema legado, padrão da marca) podem aparecer, desde que declaradas como restrição e não como o jeito de resolver.

| Faixa | Descritor |
|---|---|
| 90-100 | Descreve a necessidade ou o resultado; a solução fica em aberto; restrições reais, se houver, aparecem como restrições |
| 70-89 | Uma prescrição pequena e desnecessária (cor, posição), mas a necessidade está clara |
| 40-69 | Já define a solução ("Quero um dropdown com..."), embora ainda dê para enxergar o problema por trás |
| 0-39 | Tarefa técnica disfarçada de story ("Criar endpoint /clientes", "Migrar para Postgres"), sem necessidade do usuário |

Este critério é independente da clareza: uma story vaga que não prescreve solução alguma pode ir bem aqui e mal em clareza.

---

## 6. Tamanho (peso 16)

**Pergunta:** cabe em poucos dias de trabalho do time e pode ser demonstrada sozinha?

Referência: no máximo metade de uma sprint, preferindo poucos dias. Se o usuário informar a cadência ou o costume do time, ajuste a referência.

**Sinais de que precisa fatiar** (cada sinal derruba a nota):

- Verbos amplos: gerenciar, administrar, manter, configurar, "sistema de", "módulo de", "completo", "end-to-end".
- CRUD inteiro numa só story (criar, editar, excluir, listar, buscar).
- Ações diferentes coladas com "e" ou "ou" ("cadastrar e aprovar e notificar").
- Mais de uma persona ou mais de um perfil de acesso.
- Vários fluxos ou regras de negócio diferentes (por tipo de cliente, forma de pagamento, região).
- Mais de 7 critérios de aceitação, ou critérios que descrevem funcionalidades distintas.
- Várias integrações com sistemas externos.
- "Etc.", "entre outros", "todos os tipos de".
- Não dá para demonstrar a story inteira em uma única demonstração.

| Faixa | Descritor | Veredito |
|---|---|---|
| 90-100 | Fatia vertical fina, um fluxo principal, até 5 critérios; cabe em poucos dias | Cabe |
| 75-89 | Um pouco maior que o ideal; poderia ser fatiada, mas cabe na iteração sem risco relevante | Cabe |
| 50-74 | Provavelmente aperta a iteração ou contém duas coisas independentes; vale fatiar | Atenção |
| 25-49 | Muito provavelmente estoura a iteração; mais de um fluxo ou regra independente | Precisa fatiar |
| 0-24 | Épico disfarçado de story: "gerenciar", CRUD completo, vários perfis, semanas de trabalho | Precisa fatiar |

---

## 7. Critérios de aceitação (peso 18)

**Pergunta:** são verificáveis, específicos e cobrem o que pode dar errado?

Checklist de cobertura (relevante conforme a story): caminho feliz; alternativas; erros e validações; limites (mínimo, máximo, vazio); permissões; estados (vazio, carregando, falha); regras de negócio; requisitos não funcionais críticos, desde que testáveis. Para escrever bons critérios, veja `criterios-de-aceitacao.md`.

| Faixa | Descritor |
|---|---|
| 90-100 | 3 a 7 critérios verificáveis (resposta sim ou não), com valores concretos em vez de adjetivos, cobrindo o caminho feliz e os erros e limites mais prováveis; declarativos; sem contradição; fora do escopo explícito quando importa |
| 70-89 | Bons e verificáveis, mas faltam exceções ou limites relevantes, ou um critério é vago |
| 40-69 | Existem, mas vários são vagos ("deve ser rápido"), misturam passos de tela com regra, cobrem só o caminho feliz, ou são lista de tarefas ("criar a tela") |
| 0-39 | Ausentes (normalmente nota de 0 a 20), inverificáveis ("funcionar bem"), ou contradizem a story |

---

## 8. Independência (peso 6)

**Pergunta:** pode ser priorizada e entregue sem depender de outra story?

Dependência declarada e inevitável (por exemplo, "precisa do login que já existe") não é falha, desde que esteja explícita.

| Faixa | Descritor |
|---|---|
| 90-100 | Pode ser priorizada e entregue em qualquer ordem em relação às demais; sem dependências, ou com dependências explícitas e inevitáveis |
| 70-89 | Dependência leve, conhecida e contornável |
| 40-69 | Depende de outra story não entregue ou não mencionada; ordem rígida |
| 0-39 | Só faz sentido junto com várias outras; é fatia horizontal (camada técnica) que não entrega nada sozinha |

---

## 9. Estimabilidade (peso 8)

**Pergunta:** o time consegue estimar sem grandes perguntas em aberto?

Incerteza técnica grande pede um spike (investigação com limite de tempo). Regra de negócio indefinida pede conversa com quem decide, antes da estimativa.

| Faixa | Descritor |
|---|---|
| 90-100 | Escopo, regras e dados conhecidos; o time estima sem perguntas grandes |
| 70-89 | Poucas dúvidas pequenas, que não mudam muito a estimativa |
| 40-69 | Incertezas relevantes (integração desconhecida, regra não definida) que mudariam bastante a estimativa |
| 0-39 | Grandes desconhecidos; precisa de investigação ou decisão antes de qualquer estimativa |
