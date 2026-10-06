# Exemplo completo de priorização

Exemplo fictício, num app de agendamento para clínicas pequenas. Serve para calibrar o formato, o nível de explicação e o uso das contas.

Pedido do usuário: "Tenho 7 ideias no backlog e capacidade para umas 6 pessoas-mês neste trimestre. A meta é reduzir as faltas dos pacientes de 18% para 12%. Me ajuda a priorizar."

---

## Priorização: backlog do trimestre

**Objetivo considerado:** reduzir a taxa de faltas de 18% para 12%  ·  **Capacidade:** 6 pessoas-mês  ·  **Restrições:** nenhuma obrigação legal informada
**Suposições:** o alcance usa a base de cerca de 4.000 pacientes por trimestre (E); o esforço foi estimado por mim a partir da descrição (E). Se a base for bem diferente, a ordem dos itens 1 a 3 praticamente não muda, mas o corte da capacidade pode mudar.
**Método:** RICE, porque há uma base de pacientes e muitos candidatos de natureza parecida. Contraprova: Valor x Esforço (os itens 1 e 2 caem em "ganho rápido", o 3 em "aposta grande" e os demais em "preenchimento" ou "evitar", o que confirma a ordem).

### Ranking

| # | Item | Nota | Alcance | Impacto | Confiança | Esforço | Origem (D/E) | Grupo |
|---|---|---|---|---|---|---|---|---|
| 1 | Lembrete automático por WhatsApp 24h antes | 6.400 | 4.000 | 3 | 80% | 1,5 | A: E, I: E, C: E, Es: E | Fazer agora |
| 2 | Confirmação com um toque no lembrete | 5.120 | 3.200 | 2 | 80% | 1 | A: E, I: E, C: E, Es: E | Fazer agora |
| 3 | Cobrança de sinal via Pix ao agendar | 2.400 | 4.000 | 3 | 50% | 2,5 | A: E, I: E, C: E, Es: E | Fazer agora (testar antes) |
| | **Linha de corte: 5 de 6 pessoas-mês usadas** | | | | | | | |
| 4 | Integração com Google Agenda do profissional | 300 | 1.500 | 0,5 | 80% | 2 | A: E, I: E, C: E, Es: E | Depois |
| 5 | Novo tema visual da tela de agenda | 267 | 4.000 | 0,25 | 80% | 3 | A: E, I: E, C: E, Es: E | Descartar |
| 6 | Relatório de faltas por profissional | 240 | 300 | 1 | 80% | 1 | A: E, I: E, C: E, Es: E | Depois |
| 7 | Lista de espera automática para horários vagos | 200 | 1.200 | 1 | 50% | 3 | A: E, I: E, C: E, Es: E | Descartar neste trimestre |

(Origem: A = alcance, I = impacto, C = confiança, Es = esforço; todas as estimativas são minhas, nenhuma é dado medido. Notas conferidas com `scripts/calcular.py`.)

### Por que está nessa ordem

1. **Lembrete por WhatsApp (6.400).** Alcança toda a base e ataca diretamente a causa mais provável das faltas (esquecimento), com esforço baixo. É a maior nota porque combina alcance total, impacto alto na meta e custo pequeno.
2. **Confirmação com um toque (5.120).** Complementa o lembrete: transforma a mensagem em ação e avisa a clínica de quem não vem. O alcance é menor (nem todo paciente responde pelo link) e o impacto é "alto" e não "massivo", porque depende do lembrete existir.
3. **Cobrança de sinal via Pix (2.400).** O impacto potencial é massivo (quem paga adiantado costuma comparecer), mas a confiança é só 50% e o esforço é o maior do trio: pode reduzir os agendamentos e irritar pacientes. Está entre os "fazer agora", mas **não construir antes de testar** (ver pontos de atenção).
4. **Google Agenda (300), relatório de faltas (240), tema visual (267), lista de espera (200).** Todos distantes da meta do trimestre. O relatório ajuda a medir, mas a meta já tem uma métrica; o tema não move nenhuma meta; a lista de espera recupera receita, mas não reduz as faltas.

### O que pode mudar essa ordem

- Se o impacto do lembrete sem confirmação cair de 3 para 2, a nota do item 1 vai para 4.267 e **a confirmação com um toque passa à frente**. Na prática, os itens 1 e 2 compartilham o mesmo canal e devem ser entregues juntos como uma fatia só.
- Se a confiança do Pix subir de 50% para 80% (por exemplo, depois de um teste), a nota dele vai para 3.840: continua em 3º lugar, mas a distância para o 2º cai.
- Se a meta do trimestre mudar de "reduzir faltas" para "recuperar receita de horários vagos", a lista de espera (item 7) sobe bastante e a ordem muda. A priorização depende desse objetivo.

### Recomendação

- **Fazer agora:** lembrete + confirmação (itens 1 e 2, 2,5 pessoas-mês juntos).
- **Próximo:** Pix de sinal, **depois de um teste barato** (piloto em 2 clínicas), 2,5 pessoas-mês.
- **Depois:** Google Agenda e relatório de faltas, se o objetivo do trimestre seguinte permitir.
- **Descartar (com a razão):** tema visual (não move a meta); lista de espera (ótima para outra meta, mas não para esta).

### Pontos de atenção

- **Pix de sinal tem confiança baixa e impacto alto.** É exatamente o item em que construir sem testar é mais arriscado. Use a skill `hipoteses` para desenhar um piloto antes de investir os 2,5 pessoas-mês.
- Os itens 1 e 2 dependem do mesmo canal de mensagens: valide cedo o custo e as regras do WhatsApp Business.
- Todas as notas são estimativas minhas. Valide as três que mais pesam (alcance do lembrete, impacto do lembrete, esforço do Pix) antes de comprometer o trimestre.
- Vieses possíveis: o Pix é o item "glamouroso" e pode ganhar prioridade por convicção, não por evidência.

### Decisões que são suas

1. A meta de 12% é a única do trimestre, ou há metas de receita?
2. Os 6 pessoas-mês incluem manutenção e correção de defeitos?
3. Quem decide se um piloto com 2 clínicas é aceitável para testar o Pix?
