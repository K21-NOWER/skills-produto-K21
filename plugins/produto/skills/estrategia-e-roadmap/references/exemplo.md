# Exemplo completo: avaliação de roadmap e Tanque de Decantação

Exemplo fictício, num app de agendamento para clínicas pequenas.

Pedido do usuário: "Esse é o roadmap de 2027: Q1 módulo de agenda completo, Q2 app mobile, Q3 relatórios, Q4 integrações. Dá uma nota e me ajuda a melhorar."

---

## Avaliação do roadmap 2027

**Nota geral: 23/100** (faixa: Reescrever)

### 1. Notas por critério

| Critério (peso) | Nota | Por quê (evidência) | Como melhorar |
|---|---|---|---|
| Propósito (12) | 30 | Não diz por que o produto existe; só módulos | Escrever o objetivo de negócio |
| Problema (14) | 25 | Nenhum problema de cliente citado | Partir da dor: faltas e horários vazios |
| Métricas (14) | 20 | Nenhuma métrica | Medir o tamanho do problema |
| Causalidade ideia, métrica (12) | 20 | "Relatórios" e "integrações" não dizem o que alteram | Ligar cada ideia a uma métrica |
| Foco (10) | 30 | Todos os módulos têm o mesmo peso | Escolher uma primeira aposta |
| Roadmap como hipóteses e resultados (14) | 15 | É uma lista de funcionalidades por trimestre | Objetivos, métricas, desafios e hipóteses por ciclo |
| Flexibilidade (10) | 20 | Plano anual com 4 entregas fixas | Ciclos curtos e revisão por aprendizado |
| Conexão com cliente e mercado (14) | 25 | Nada sobre propósito do cliente nem concorrência | Mapear propósitos (F4P) e concorrentes |

Cálculo: (30x12 + 25x14 + 20x14 + 20x12 + 30x10 + 15x14 + 20x10 + 25x14) ÷ 100 = 22,9, arredondado para 23.

### 2. O que mais pesa

1. **É um roadmap de funcionalidades, não de resultados** (15). Se cumprir os quatro trimestres, ainda não sabemos se algo melhorou.
2. **Não há problema nem métrica** (25 e 20). A priorização será na base do "eu acho que...".
3. **É um plano grande e rígido** (20): quanto mais massa, mais caro mudar de rota.

### 3. Versão reescrita: Tanque de Decantação

**Suposições:** o problema central é a falta do paciente; a clínica já tem alguma agenda.

| Etapa | Conteúdo |
|---|---|
| **Propósito** | Clínicas pequenas com a agenda cheia e atendida (por que somos pagos: a receita da clínica depende de horários ocupados) |
| **Problema** | Pacientes faltam sem avisar; a recepção só consegue ligar para parte deles; o horário vazio vira prejuízo |
| **Métricas** | Taxa de faltas [18%]; cancelamentos de última hora; confirmações; receita perdida por faltas |
| **Ideias** | Eu, enquanto recepcionista, desejo que o paciente seja lembrado do horário para ele não faltar (altera a taxa de faltas). Eu, enquanto paciente, desejo confirmar ou cancelar com um toque para liberar o horário (altera cancelamentos tardios) |
| **Foco** | Lembrete 24h antes, pela relação mais forte com o pior problema |
| **CCC** | Cartão: a ideia em foco. Conversa: o que é e o que não é (não é confirmação nem remarcação). Confirmação: critérios de aceitação e meta de reduzir a taxa de faltas de [18%] para [12%] em [7 semanas] |

### Roadmap enxuto (ciclo de 6 semanas)

| Ciclo | Objetivo | Métricas | Desafios | Hipóteses |
|---|---|---|---|---|
| Semanas 1 a 6 | Reduzir as faltas em 2 clínicas | Taxa de faltas; cancelamentos de última hora | Consentimento para mensagens; custo por mensagem | O lembrete 24h antes reduz as faltas em 6 pontos |
| Próximo ciclo | Definido pelo resultado do primeiro (confirmar com um toque, ou investigar outra causa) | | | |

### Qualidade (autoavaliação): 86/100

### Próximos passos

- Transformar a ideia em foco em Test Card com a skill `hipoteses` e em história com `user-story`.
- Definir as métricas de equilíbrio com `metricas-de-produto` antes de começar.

### 4. Perguntas e suposições

- Assumi que a empresa quer foco em uma causa. Se há outro objetivo (receita por clínica), o Tanque muda.
- Não foi preciso usar a Matriz de Estratégia: bastou o Tanque. Se for preciso escolher entre segmentos (clínica odontológica x estética), vale a Matriz com o F4P.
