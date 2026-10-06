# Exemplo completo: avaliação de métricas

Exemplo fictício, num app de agendamento para clínicas pequenas. Serve para calibrar o rigor e o formato.

Pedido do usuário: "Esse é o painel que o time acompanha: downloads do app, número de funcionalidades entregues no trimestre, NPS e consultas agendadas. Dá uma nota e me ajuda a melhorar."

---

## Avaliação das métricas: painel do app de agendamento

**Nota geral: 36/100** (faixa: Reescrever)

### 1. Notas por critério

| Critério (peso) | Nota | Por quê (evidência) | Como melhorar |
|---|---|---|---|
| Vínculo com o problema (18) | 40 | "Downloads" e "funcionalidades entregues" medem marketing e solução; só "consultas agendadas" se aproxima do problema | Partir do problema: a clínica perde receita com faltas |
| Resultado, não tarefa (14) | 35 | "Funcionalidades entregues no trimestre" é entrega, não impacto | Trocar por uma métrica de comportamento, como taxa de faltas |
| Acionável e sem vaidade (12) | 35 | Downloads é vaidade: nada muda se subir ou cair | Definir a decisão ligada a cada métrica |
| Equilíbrio (14) | 25 | Todas puxam para "mais volume"; nada protege a qualidade | Incluir métricas de equilíbrio (cancelamentos de última hora, reclamações) |
| Definição operacional (14) | 30 | Só nomes: sem fórmula, período ou linha de base | Escrever fórmula, janela e baseline |
| Meta definida antes (10) | 20 | Nenhuma meta citada | Definir critério numérico e prazo |
| Cobertura e nível (8) | 40 | Só eficácia, sem nenhum sinal de eficiência ou ecossistema | Acrescentar lead time de entrega do time, por exemplo |
| Foco 80/20 (10) | 70 | Quatro métricas é pouco e saudável; falta uma qualitativa além do NPS | Somar perguntas abertas sobre o motivo da falta |

Cálculo: (40x18 + 35x14 + 35x12 + 25x14 + 30x14 + 20x10 + 40x8 + 70x10) ÷ 100 = 36,2, arredondado para 36.

### 2. O que mais pesa

1. **O painel mede atividade, não problema** (vínculo 40, resultado 35). Dá para bater todas as metas e as faltas continuarem em 18%.
2. **Nenhuma métrica de equilíbrio** (25). Se o time perseguir "consultas agendadas", pode empurrar agendamentos que ninguém cumpre.
3. **Sem definição nem meta** (30 e 20). Cada pessoa vai calcular de um jeito e ajustar a régua depois.

### 3. Conjunto melhorado

| Papel | Métrica | Fórmula e período | Linha de base | Critério (meta) |
|---|---|---|---|---|
| Principal | Taxa de faltas | Consultas não comparecidas e sem cancelamento com 2 horas de antecedência ÷ consultas agendadas, por mês | [18%] | Cair para [12%] em 3 meses |
| Equilíbrio 1 | Cancelamentos de última hora | Cancelamentos com menos de 2 horas ÷ consultas agendadas, por mês | [a medir] | Não passar de [5%] |
| Equilíbrio 2 | Taxa de crescimento de clínicas | Novas clínicas ativas ÷ clínicas no início do mês | [4%] | Manter [4%] ao mês |
| Apoio | Taxa de confirmação | Pacientes que confirmam ÷ pacientes lembrados, por semana | [a medir] | Subir para [60%] |
| Qualitativa | Motivo da falta | 10 ligações por mês a pacientes que faltaram, com resposta aberta | [a medir] | Entender a causa dominante |

**North Star sugerida:** consultas realizadas (compareceu) por clínica por mês, porque captura o valor central: agenda cheia e atendida.

### 4. Perguntas e suposições

- Assumi que o problema central é a falta do paciente. Se for outro (por exemplo, retenção de clínicas), a principal muda.
- Os números entre colchetes são suposições minhas. Troque pelos reais.
- O "2 horas de antecedência" é uma regra assumida para separar falta de cancelamento tardio.

Sugestão de próximo passo: transformar a métrica principal em hipótese testável com a skill `hipoteses` e em resultado-chave com a skill `okr`.
