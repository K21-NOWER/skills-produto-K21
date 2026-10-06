# Exemplo completo: avaliação e plano UDD

Exemplo fictício, num app de agendamento para clínicas pequenas, com a meta de reduzir as faltas.

Pedido do usuário: "Meu plano para o semestre é: 1) cadastro completo de pacientes, 2) agenda web completa, 3) app mobile para iOS e Android, 4) relatórios e 5) lembretes automáticos. Isso é um MVP? Dá uma nota e me ajuda."

---

## Avaliação do plano: semestre do app de agendamento

**Nota geral: 24/100** (faixa: Reescrever)

### Notas por critério

| Critério (peso) | Nota | Por quê (evidência) | Como melhorar |
|---|---|---|---|
| Hipótese e direção (16) | 25 | O plano é uma lista de módulos; não diz que problema resolve | Partir do problema: as faltas |
| Epicentro (14) | 30 | Começa por cadastro, que é base e não a parte mais importante do problema | Começar pelo que reduz a falta: o lembrete |
| Fatia vertical (14) | 35 | "Cadastro", "agenda" e "app" são módulos e camadas, nenhum entra em uso sozinho | Fatias que atravessam o produto |
| Sinal de uso definido antes (16) | 20 | Nenhuma métrica de comportamento | Definir comportamento e critério por fatia |
| Ciclo curto até o uso real (12) | 20 | Meses até o primeiro uso | Primeira fatia em semanas, com 2 clínicas |
| Progressão 1-2-N (8) | 30 | Vai direto ao "completo" | Caso básico, depois variação, depois geral |
| Descarte explícito (10) | 15 | Nada ficou de fora | Listar o que não faremos agora |
| Regra de expansão (10) | 15 | Os cinco itens seguem o calendário | Cada fatia depende de um resultado |

Cálculo: (25x16 + 30x14 + 35x14 + 20x16 + 20x12 + 30x8 + 15x10 + 15x10) ÷ 100 = 24,1, arredondado para 24.

### O que mais pesa

1. **É um plano de construção, não de aprendizado** (hipótese 25, sinal de uso 20). Dá para entregar os cinco módulos e as faltas continuarem iguais.
2. **O epicentro está no lugar errado** (30). Cadastro e agenda "completos" são o que a clínica já tem de algum jeito; o lembrete ataca a parte mais importante do problema mais importante.
3. **Não há como descartar nada** (15 e 15): sem regra de expansão, tudo vira obrigação.

### Plano UDD reescrito

**Suposições:** o problema central é a falta do paciente (18% hoje, assumido); as clínicas já têm uma agenda, mesmo que de papel ou planilha.

**Hipótese central:** acreditamos que lembrar o paciente 24 horas antes resultará em menos faltas.

**Epicentro:** a parte mais importante do problema mais importante da clínica mais importante: o paciente que esquece a consulta de amanhã.

| # | Fatia (resultado para o usuário) | Hipótese | Sinal de uso e critério | Limite | Só expande se... |
|---|---|---|---|---|---|
| 1 | Paciente recebe lembrete por WhatsApp 24h antes, enviado manualmente a partir da agenda existente, em 2 clínicas | Lembrar reduz esquecimento | Taxa de faltas do grupo com lembrete pelo menos 6 pontos abaixo do controle | 5 a 7 semanas | A queda for de 6 pontos ou mais |
| 2 | Paciente confirma presença com um toque no lembrete (caso 2: variação) | Confirmar compromete | 50% dos lembrados confirmam e as faltas caem mais | 3 semanas | A confirmação passar de [50%] |
| 3 | Lembrete automático para qualquer clínica que importe a agenda (caso N: generaliza) | Automatizar mantém o efeito em escala | Faltas continuam [12%] em 5 clínicas | 6 semanas | Fatias 1 e 2 baterem os critérios |

**O que ficou de fora:** cadastro completo, app mobile, relatórios. Podem nunca existir: se a fatia 1 não funcionar, o plano muda de causa e não de módulo.

**Qualidade (autoavaliação):** 88/100.

Próximos passos: transformar a fatia 1 em Test Card com a skill `hipoteses` e em história com `user-story`.
