# Exemplo completo: auditoria de backlog

Exemplo fictício, num app de agendamento para clínicas pequenas. Os números vêm de `scripts/exemplo-backlog.csv` rodado com data de referência 2026-10-06 (9 itens abertos).

Pedido do usuário: "Esse é o backlog do app (exportei em CSV). Dá uma nota e me diz o que fazer."

---

## Saúde do backlog: app de agendamento

**Nota geral: 42/100** (faixa: Reescrever o backlog)

### 1. Notas por critério

| Critério (peso) | Nota | Por quê (evidência) | Como melhorar |
|---|---|---|---|
| Horizonte de detalhe (14) | 40 | Todos os itens têm o mesmo nível vago, inclusive os do topo | Detalhar só os 3 a 5 primeiros |
| Tamanho do topo (14) | 35 | No topo está "Gerenciar agendamentos do paciente" (tamanho G), um épico | Fatiar antes de comprometer |
| Priorização explícita (14) | 55 | Há ordem numérica, mas sem critério declarado | Declarar o critério (por exemplo, RUT) |
| Higiene (12) | 35 | 66% dos itens têm mais de 90 dias; há um par duplicado ("lembrete por WhatsApp 24h antes") | Juntar o duplicado e decidir sobre os velhos |
| Ligação com objetivos (12) | 40 | Os títulos descrevem funcionalidades, sem objetivo ou métrica | Ligar cada item do topo a um objetivo |
| Upstream e descarte (12) | 25 | Não há itens descartados nem prateleira; o backlog só acumula | Criar prateleira com limite e prazo |
| Prontidão do topo (14) | 40 | 1 dos 5 primeiros está sem tamanho; nada indica critérios de aceitação | Refinar o topo com `user-story` |
| Volume (8) | 80 | 9 itens é um volume saudável | Manter |

Cálculo: (40x14 + 35x14 + 55x14 + 35x12 + 40x12 + 25x12 + 40x14 + 80x8) ÷ 100 = 42,2, arredondado para 42.

### 2. O que mais pesa

1. **Não há decisão de descarte** (upstream 25): itens de nov/2025 e dez/2025 seguem na lista sem dono nem prazo.
2. **O topo é um épico** (35): "Gerenciar agendamentos" não cabe numa sprint e esconde o item de maior retorno.
3. **Os itens não dizem para que servem** (40): sem objetivo, a ordem vira opinião.

### 3. Plano de faxina

| Ação | Itens | Por quê |
|---|---|---|
| Fatiar | Gerenciar agendamentos do paciente | Épico no topo; começar por "confirmar presença" |
| Juntar | Os dois "Lembrete por WhatsApp" | Duplicados |
| Prateleira (prazo de 60 dias) | Relatório de faltas, Integração com Google Agenda | Úteis, mas sem evidência de retorno agora |
| Descartar | Novo tema visual da agenda, Sistema de cobrança completo | Antigos, sem objetivo ligado e de esforço alto |
| Refinar | Os 3 primeiros itens | Critérios de aceitação e tamanho |

### 4. Regras para manter o backlog saudável

- Detalhar só o que entra nas próximas 2 sprints.
- Prateleira com no máximo 5 itens e prazo de 60 dias.
- Todo item novo passa pelo cartão de triagem (necessidade, ligação com objetivo, decisão).
- Revisão mensal do que passou de 90 dias.

### 5. Perguntas e suposições

- Assumi que o objetivo do trimestre é reduzir faltas.
- Itens antigos podem ser importantes: as decisões acima são propostas para o PO confirmar, não ordens.
