# Exemplo completo de análise de hipótese

Exemplo fictício, num app de agendamento para clínicas pequenas. Serve para calibrar o rigor das notas, o formato e a ligação com a skill `user-story`.

Pedido do usuário: "Acho que se mandarmos lembrete por WhatsApp, as pessoas vão faltar menos. Me ajuda a avaliar e a testar?"

---

## Análise da hipótese: lembrete por WhatsApp reduz faltas

**Qualidade da hipótese: 54/100** (faixa: ainda é uma ideia) · **Criticidade:** Alta

A nota geral passa de 50, mas a mensurabilidade (25) ficou abaixo de 40. Sem métrica, critério e prazo, ainda não há o que testar. A reescrita abaixo é o que transforma a ideia em hipótese.

### 1. Hipótese reescrita

> **Acreditamos que** enviar um lembrete por WhatsApp 24 horas antes da consulta **para** pacientes de clínicas pequenas que agendam pelo app **vai reduzir** a taxa de faltas de [18%] para [12%] ou menos, **porque** [a maioria das faltas parece ser esquecimento e hoje a recepção só consegue ligar para parte dos pacientes; intuição, sem evidência ainda]. **Saberemos que estamos certos quando** a taxa de faltas do grupo que recebe o lembrete for pelo menos 6 pontos percentuais menor que a do grupo que não recebe, em até 7 semanas.

Os valores entre colchetes são suposições minhas. Troque pelos números reais da clínica.

### 2. Notas por critério

| Critério (peso) | Nota | Por quê (evidência) | Como melhorar |
|---|---|---|---|
| Clareza e especificidade (12) | 55 | "lembrete por WhatsApp" é específico, mas "faltar menos" é vago | Dizer quanto menos |
| Público (10) | 35 | "as pessoas" | Dizer quem: pacientes de quais clínicas |
| Falseabilidade (16) | 45 | Qualquer redução, mesmo mínima, "confirma" | Definir o quanto precisa reduzir |
| Mensurabilidade (16) | 25 | Sem métrica, baseline, critério ou prazo | Taxa de faltas, de 18% para 12%, em 7 semanas |
| Fundamento (12) | 30 | Nenhuma evidência citada | Levantar os motivos reais das faltas |
| Foco (10) | 80 | Uma crença central: o lembrete muda o comportamento | Manter |
| Conexão com o resultado (10) | 85 | Faltas ligam direto ao negócio da clínica | Manter |
| Testabilidade (14) | 90 | Fácil e barato de testar | Manter |

Cálculo: (55x12 + 35x10 + 45x16 + 25x16 + 30x12 + 80x10 + 85x10 + 90x14) ÷ 100 = 54.

### 3. Suposições por trás

| Suposição | Tipo de risco | Importância | Evidência atual | Testar primeiro? |
|---|---|---|---|---|
| A1. A maior parte das faltas é por esquecimento, e não por imprevisto, custo ou medo | Desejabilidade | Alta | Baixa | **Sim (salto de fé)** |
| A2. Um lembrete muda o comportamento de quem iria faltar | Desejabilidade | Alta | Baixa | **Sim (salto de fé)** |
| A3. Os pacientes leem o WhatsApp a tempo e aceitam receber mensagens | Desejabilidade | Alta | Média | Em paralelo |
| A4. A clínica consegue reaproveitar o horário liberado | Viabilidade de negócio | Média | Baixa | Depois |
| A5. Dá para enviar as mensagens a custo viável e dentro das regras do canal e da LGPD | Viabilidade técnica, de negócio e legal | Alta | Média | Em paralelo |

### 4. Experimentos sugeridos (do mais barato ao mais robusto)

| Opção | O que fazemos | Custo e tempo | Evidência | Testa |
|---|---|---|---|---|
| **A. Dados e ligações** | Levantar os motivos de falta dos últimos 3 meses na agenda e ligar para 20 pacientes que faltaram | Muito baixo; 2 a 3 dias | Nível 2 | A1 |
| **B. Piloto manual com grupo de controle** | Em 2 ou 3 clínicas, enviar o lembrete por WhatsApp (por ferramenta de disparo) para metade das consultas sorteadas e nada para a outra metade; medir a taxa de faltas em cada grupo | Baixo (sem desenvolvimento); 5 a 7 semanas | Nível 3, forte | A1 a A3, A5 |
| **C. Funcionalidade automatizada com feature flag** | Construir o lembrete automático e liberar 50% da base | Alto (cerca de 1,5 pessoa-mês); 6 a 8 semanas | Nível 3, forte | Tudo, em escala |

**Recomendação:** rodar **A** agora (2 dias) e **B** em seguida. Só construir **C** se B confirmar. A é quase de graça e pode derrubar a hipótese antes de gastar semanas.

### 5. Métricas e critério de sucesso

- **Primária:** taxa de faltas = consultas não comparecidas e não canceladas com pelo menos 2 horas de antecedência ÷ consultas agendadas, por grupo.
- **Apoio:** taxa de entrega e de leitura da mensagem; taxa de confirmação; percentual de horários liberados que foram reaproveitados.
- **Proteção (guardrails):** reclamações e opt-out; cancelamentos de última hora (para o lembrete não trocar falta por cancelamento tardio); satisfação.
- **Baseline:** 18% (assumido; confirmar com os dados reais dos últimos 3 meses).
- **Critério de sucesso:** o grupo com lembrete tem pelo menos 6 pontos percentuais menos faltas que o controle, **com pelo menos 650 consultas por grupo**.
- **Amostra:** `16 x 0,18 x 0,82 / 0,06² ≈ 656` consultas por grupo. Com 2 clínicas de cerca de 400 consultas por mês cada, cada grupo (metade das consultas) acumula cerca de 400 por mês: são cerca de 7 semanas até chegar a 656. Com 3 clínicas, cerca de 5 semanas.
- **Regra de decisão:** se a redução for de 6 pontos ou mais, persistir e construir (C). Se ficar entre 2 e 6 pontos, investigar por segmento e melhorar a mensagem antes de decidir. Se ficar abaixo de 2, abandonar esta hipótese e voltar à A1 (a causa das faltas pode ser outra). Se a amostra não chegar a 650 por grupo, o resultado é inconclusivo: estender o teste.

### 6. Riscos

| Risco | Tipo | Prob. | Impacto | Mitigação |
|---|---|---|---|---|
| A causa das faltas não é esquecimento | Desejabilidade | Média | Alto | Experimento A antes de investir |
| Clínicas do piloto são mais engajadas que a média | Viés | Média | Médio | Sortear por consulta dentro da mesma clínica |
| Pacientes do controle recebem lembrete por outro canal (a recepção já liga) | Contaminação | Média | Médio | Combinar com a clínica que não ligará para o grupo controle durante o teste |
| Consentimento e regras do canal (LGPD, políticas do WhatsApp) | Ético e legal | Média | Alto | Confirmar base legal e consentimento, e oferecer opt-out; revisar com o encarregado de dados |
| Custo por mensagem inviabiliza o produto em escala | Viabilidade de negócio | Baixa a média | Alto | Calcular margem unitária durante o piloto |
| Efeito novidade (o efeito some depois de semanas) | Viés | Média | Médio | Acompanhar por pelo menos 4 semanas |
| Sazonalidade (feriados, época de gripe) | Viés | Média | Médio | Comparar grupos ao mesmo tempo, não antes e depois |

### 7. Test Card

| Campo | Conteúdo |
|---|---|
| **Hipótese** | Acreditamos que um lembrete por WhatsApp 24h antes da consulta reduz as faltas de pacientes de clínicas pequenas |
| **Teste** | Para verificar isso, vamos enviar o lembrete para metade das consultas, sorteadas, em 2 ou 3 clínicas, durante 5 a 7 semanas, mantendo a outra metade como controle |
| **Métrica** | E vamos medir a taxa de faltas de cada grupo, a entrega e leitura, a confirmação e os cancelamentos de última hora |
| **Critério** | Estaremos certos se o grupo com lembrete tiver pelo menos 6 pontos percentuais menos faltas, com pelo menos 650 consultas por grupo |
| Custo / Tempo / Confiabilidade | Baixo / 5 a 7 semanas / Alta |
| Responsável e prazo | [a definir] |

### 8. User story pronta para o time

### US-01 · Lembrete por WhatsApp 24 horas antes (versão do experimento)

**História:** Como paciente com consulta marcada, quero receber um lembrete por WhatsApp 24 horas antes, para não esquecer do horário.

**Critérios de aceitação**

- **Cenário: envio do lembrete**
  - Dado que tenho uma consulta marcada para amanhã às 14h, aceitei receber mensagens e fui sorteado para o grupo com lembrete
  - Quando faltarem 24 horas (com tolerância de 15 minutos) para a consulta
  - Então recebo uma mensagem com o nome da clínica, o profissional, a data, a hora e o endereço
- **Cenário: sem consentimento**
  - Dado que não aceitei receber mensagens
  - Quando faltarem 24 horas para a consulta
  - Então nenhuma mensagem é enviada
- **Cenário: grupo de controle**
  - Dado que fui sorteado para o grupo de controle
  - Quando faltarem 24 horas para a consulta
  - Então nenhuma mensagem é enviada e minha participação no grupo fica registrada
- **Cenário: consulta cancelada ou agendada com menos de 24 horas**
  - Dado que a consulta foi cancelada antes do envio, ou foi agendada com menos de 24 horas de antecedência
  - Então nenhuma mensagem de lembrete é enviada [suposição: a confirmação do agendamento já cobre o caso das menos de 24 horas]
- **Cenário: sair da lista**
  - Dado que respondo "PARAR" a uma mensagem
  - Então não recebo novas mensagens e meu pedido fica registrado
- **Instrumentação:** para cada consulta, ficam registrados o grupo (lembrete ou controle), o horário de envio, o status de entrega e leitura, e o desfecho (compareceu, faltou, cancelou com antecedência).
- **Controle do experimento:** o envio pode ser desligado por clínica, sem nova publicação.

**Fora do escopo:** botão de confirmar presença, remarcação, segundo lembrete, painel de resultados.
**Sinal de sucesso (da hipótese; não é critério de aceitação):** a taxa de faltas do grupo com lembrete é pelo menos 6 pontos percentuais menor que a do controle, com pelo menos 650 consultas por grupo.
**Dúvidas e suposições:** o canal e a ferramenta de disparo ainda não foram escolhidos; a base legal do envio precisa ser confirmada.
**Qualidade (autoavaliação):** 84/100 · Tamanho: Cabe

Para o experimento B (piloto manual), essa story ainda **não precisa ser construída**: as mensagens podem ser enviadas por uma ferramenta de disparo. Ela fica pronta no backlog para o experimento C, se B confirmar.

### 9. O que fazer depois do teste

- **Se confirmar** (redução de 6 pontos ou mais): construir a automação (C) e testar a próxima suposição (A4: reaproveitamento do horário liberado).
- **Se refutar** (menos de 2 pontos): abandonar o lembrete como solução principal; voltar à A1 e entender a causa real das faltas.
- **Se for inconclusivo** (menos de 650 consultas por grupo ou resultado entre 2 e 6 pontos): estender o teste ou investigar por segmento, sem declarar vitória.
