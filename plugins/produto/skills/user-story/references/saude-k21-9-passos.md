# Saúde da história: os 9 passos da K21

Conteúdo: Formato K21 · Os 9 passos (4 blocos) · Como combinar com a rubrica · Nível de detalhe da solução (maturidade x sentimento de dono) · Como fortalecer o sentimento de dono

Este material vem do método da K21 ("Avalie a Saúde da sua História de Usuário em 9 passos"). Use-o como lista de verificação rápida, de sim ou não, e como vocabulário para explicar ao aluno o que está errado. A nota de 0 a 100 continua vindo da `rubrica.md`: os 9 passos dizem **o que olhar**, a rubrica diz **quanto vale**.

## Formato K21

`Eu, enquanto <personagem>, desejo <necessidade> para <propósito>.`

Variações aceitas no verbo ("quero", "gostaria", "preciso", "necessito") e na ligação ("para", "pois", "porque"). O formato "Como [persona], quero [ação], para [benefício]" é equivalente: o que importa são as três respostas, **quem** (personagem), **o quê** (necessidade) e **por quê** (propósito). Aceite os dois formatos e não penalize a diferença de redação.

## Os 9 passos

| Bloco | # | Passo | Verificação (sim ou não) | Mau exemplo | Bom exemplo |
|---|---|---|---|---|---|
| Estrutura | 1 | Estrutura recomendada | Responde quem, o quê e por quê no formato acima? | "Enviar e-mail de alerta de turma lotada." | "Eu, enquanto Paula PO, desejo me inscrever no treinamento de Product AI porque preciso aprimorar a minha forma de trabalhar." |
| Estrutura | 2 | História PARA o usuário | Está escrita do ponto de vista do usuário e não de solução técnica? | "Eu, enquanto Alvin Aluno, desejo acessar a API do meio de pagamento para pagar com meu cartão." | "Eu, enquanto Alvin Aluno, desejo pagar os cursos em que me inscrevi com meu cartão de crédito para efetuar a matrícula." |
| Personagem | 3 | Toda história tem um personagem | Há uma pessoa (persona) e não "departamento", "setor" ou "o sistema"? | "Criar um relatório de vendas da região Sul para avaliarmos se abrimos filial." | "Eu, enquanto Sérgio Expansão Segura, desejo avaliar as vendas da região Sul para decidir se abriremos mais filiais." |
| Personagem | 4 | Personagem específico | Tem nome e uma característica que gera empatia (a Paula PO, o Valdir Detalhista)? | "Eu, enquanto usuário, preciso de um relatório de alunos inscritos para saber se abro outra turma." | "Eu, enquanto Valdir Detalhista, desejo verificar se a turma ficará lotada para saber se preciso abrir uma nova turma." |
| Necessidade | 5 | Necessidade não é solução | Admite mais de uma solução? | "...desejo receber um **e-mail** informando o início das aulas..." | "...desejo receber um **aviso** sobre o início das aulas..." (e-mail, WhatsApp, banner, ligação) |
| Necessidade | 6 | Só uma necessidade | Há conjunção ("e", "ou", "mas", "nem", "entretanto")? Se sim, é sinal de fatiar | "...desejo me inscrever em um curso **E** pagar..." | Duas histórias: inscrever para reservar a vaga; pagar para efetuar a matrícula |
| Necessidade | 7 | Necessidade objetiva | Dá para dizer, sem ambiguidade, o que muda? ("facilmente" não dá) | "...desejo acessar o sistema facilmente..." | "...desejo acessar o sistema com a minha conta e senha..." |
| Propósito | 8 | Propósito obrigatório | Existe um "para" que explica por que a pessoa precisa disso? | "Eu, enquanto Amanda Administrativo, preciso das informações das pessoas inscritas." | "...preciso das informações de contato das pessoas inscritas para comunicar o início das aulas." |
| Propósito | 9 | Propósito objetivo | O "para" é específico, sem "tomada de decisão" genérica? | "Fernanda Financeira precisa das informações de custo das turmas para tomada de decisão." | "...desejo receber as informações de custo do catering e da locação para escolher a melhor data de pagamento de ambos." |

Conta rápida: 9 respostas "sim" é uma história saudável. Cada "não" aponta o critério da rubrica a olhar.

## Como combinar com a rubrica

| Passo | Critério da rubrica que ele alimenta |
|---|---|
| 1 | Clareza (4) e Persona (1) |
| 2 e 5 | Foco no problema (5) |
| 3 e 4 | Persona (1): persona com nome e característica é a faixa 90-100 |
| 6 | Tamanho (6): conjunção é um indício forte de que precisa fatiar |
| 7 | Clareza (4) e Estimabilidade (9) |
| 8 e 9 | Valor (2) e Efetividade (3) |

Na seção "O que mais pesa" da avaliação, cite o número do passo ("falha o passo 6: duas necessidades coladas com 'e'"). O aluno memoriza os passos e passa a revisar sozinho.

**Exceção da história técnica (passo 2).** Dívida técnica e atualização de biblioteca podem virar história técnica quando o risco é real e precisa ser priorizado, mesmo que o usuário final não perceba a mudança. Ex.: "Eu, enquanto Denis Dev, desejo alterar a solução X para evitar que ela torne o software difícil de manter no futuro." Nesse caso a persona é o time, e isso não é penalizado como erro de persona, desde que o propósito explique o risco que está sendo evitado. Mas se a lentidão ou o problema é percebido pelo usuário, escreva do ponto de vista dele ("desejo escolher rapidamente os cursos disponíveis para fazer minha inscrição sem perder tempo").

## CCC e INVEST como pano de fundo

- **CCC** (Mike Cohn): **C**artão (pequena o bastante para caber num cartão pautado), **C**onversa (o cartão tem pouco espaço, então a conversa entre negócio e técnico é inevitável) e **C**onfirmação (critérios de aceitação para garantir a mesma compreensão).
- **INVEST** descreve boas características, mas é subjetivo (o que é "pequena" para um time novo é diferente para um time experiente). Os 9 passos são o complemento objetivo.

## Nível de detalhe da solução: maturidade x sentimento de dono

Há quem reclame que uma história sem solução está "incompleta". A resposta da K21 é: **depende do time**. Duas variáveis:

- **Maturidade do time:** conhecimento do problema, do contexto da empresa, dos clientes, das ferramentas, dos membros do time e dos processos. Cresce com o tempo e cai quando pessoas-chave mudam.
- **Sentimento de dono do produto:** o quanto as pessoas se veem responsáveis pelo que constroem, e não como meras executoras ("pediram A, fiz A").

| Quadrante | Time | O que escrever na história | Papel do PO |
|---|---|---|---|
| 1. Baixa maturidade, baixo sentimento de dono | Em formação, executor | Necessidade clara **mais** campos extras: proposta de solução, modelo de tela, o que for importante. Cuidado com o Big Design Up Front: só acrescente campos se precisar | Protagonista, detalha bastante |
| 2. Baixa maturidade, alto sentimento de dono | Quer decidir, ainda não sabe como | Menos campos extras nas histórias simples; os campos servem de apoio para evitar ideias loucas | Professor: ajuda o time a ganhar maturidade |
| 3. Alta maturidade, baixo sentimento de dono | Capaz, mas travado (conflito com clientes, superproteção, represália passada) | Quase todos os campos extras saem; no máximo uma proposta de solução sucinta | Mentor: resolve o que impede o time de se apropriar e reduz a dependência |
| 4. Alta maturidade, alto sentimento de dono | Ponto ideal | Só a necessidade; os campos extras são preenchidos pelos próprios desenvolvedores | Consultor da solução: entrega a necessidade, o time propõe a solução |

**Como usar na avaliação:** antes de punir "falta de solução" ou "excesso de solução", pergunte (ou declare como suposição) em que quadrante o time está. Solução detalhada para um time do quadrante 1 é aceitável; a mesma solução para o quadrante 4 é um problema de foco no problema.

## Como fortalecer o sentimento de dono

1. **Compartilhe o "porquê", não só o "o quê"**: quem o time ajuda e como.
2. **Dê autonomia com responsabilidade**: não chegue com solução pronta; escute as propostas técnicas.
3. **Envolva o time nas decisões de produto**: descoberta, priorização, conversa com clientes.
4. **Dê visibilidade e protagonismo**: o time apresenta entregas e conversa com stakeholders; o PO não é o preposto.
5. **Reconheça atitudes de dono**: valorize quem se antecipa, questiona com foco no cliente ou melhora o que ninguém pediu.
6. **O cliente não é o inimigo**: sem embate, piada ou deboche; lembre que o time também é cliente de alguém.
