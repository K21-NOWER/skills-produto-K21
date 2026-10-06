# Exemplo completo de avaliação

Exemplo fictício, num app de agendamento para clínicas pequenas. Serve para calibrar o nível de rigor das notas, o tom da explicação e o formato de saída.

Pedido do usuário: "Avalia essa story e melhora ela: *Como usuário, quero gerenciar meus agendamentos, para ter mais controle.*"

---

## Avaliação: gerenciar meus agendamentos

**Nota geral: 32/100** (faixa: Reescrever) · **Tamanho:** Precisa fatiar

### 1. Notas por critério

| Critério (peso) | Nota | Por quê (evidência) | Como melhorar |
|---|---|---|---|
| Persona (8) | 40 | "Como usuário" é genérico. Em um app de clínica, pode ser paciente, recepcionista ou profissional | Dizer quem: "Como paciente com consulta marcada" |
| Valor (12) | 45 | "para ter mais controle" é vago: controle sobre o quê, para evitar qual problema? | Trocar por um benefício concreto: "para avisar a clínica que vou sem precisar ligar" |
| Efetividade (10) | 25 | Nada indica o que mudaria depois de entregue | Incluir um sinal de sucesso (ex.: queda das faltas, menos ligações para a recepção) |
| Clareza (14) | 35 | "gerenciar" pode significar ver, confirmar, remarcar, cancelar, ou tudo isso | Escolher uma ação específica |
| Foco no problema (8) | 85 | Não prescreve tela nem tecnologia, o que é bom | Manter assim |
| Tamanho (16) | 15 | "gerenciar" é um CRUD inteiro, com várias regras (prazo de cancelamento, disponibilidade de horário) | Fatiar (veja a seção 3) |
| Critérios de aceitação (18) | 10 | Não há nenhum | Escrever cenários verificáveis para cada fatia |
| Independência (6) | 60 | Não cita dependências, mas o escopo amplo sugere várias | Explicitar dependências por fatia |
| Estimabilidade (8) | 20 | Ninguém consegue estimar "gerenciar" | Estimar depois de fatiar |

Cálculo: (40x8 + 45x12 + 25x10 + 35x14 + 85x8 + 15x16 + 10x18 + 60x6 + 20x8) ÷ 100 = 32,2, arredondado para 32. Os tetos de bloqueio e de tamanho (69) também se aplicariam, mas a nota já está abaixo deles.

### 2. O que mais pesa

1. **É um épico, não uma story** (tamanho 15). "Gerenciar" esconde pelo menos quatro comportamentos diferentes, e é por isso que ninguém consegue estimar nem testar.
2. **Não há critérios de aceitação** (10). Sem eles, cada pessoa do time imagina um "gerenciar" diferente.
3. **O valor está vago** (45 e 25). "Mais controle" não dá para observar nem medir, então nunca saberemos se funcionou.

### 3. Fatiamento

Padrão usado: operações (CRUD) combinado com passos do fluxo. Fatias, em ordem:

1. Confirmar presença em uma consulta marcada, com um toque. (A mais fina que atravessa o sistema e já ajuda a clínica a se planejar.)
2. Ver minhas próximas consultas.
3. Cancelar uma consulta, liberando o horário.
4. Remarcar para outro horário disponível. (Concentra mais regras: disponibilidade, prazo mínimo.)
5. Ver o histórico de consultas passadas. (Candidata a descarte até o uso mostrar que alguém precisa.)

A ordem começa pelo que gera valor e aprendizado mais cedo. Antes de fechá-la, vale conversar com a clínica para saber qual das fatias 1 a 4 mais dói no dia a dia.

### 4. Versão melhorada (fatia 1)

### US-01 · Confirmar presença com um toque

**História:** Como paciente com consulta marcada, quero confirmar minha presença com um toque, para avisar a clínica que vou comparecer sem precisar ligar.

**Critérios de aceitação**

- **Cenário: confirmação bem-sucedida**
  - Dado que tenho uma consulta marcada para daqui a 2 dias e recebi o link de confirmação
  - Quando abro o link e toco em "Confirmar presença"
  - Então vejo "Presença confirmada" com data, hora e nome do profissional
  - E a clínica vê o status "Confirmada" na agenda em até 1 minuto
- **Cenário: consulta já confirmada**
  - Dado que já confirmei essa consulta
  - Quando abro o link de novo
  - Então vejo a consulta como "Confirmada", sem botão de confirmar
- **Cenário: consulta cancelada ou já realizada**
  - Dado que a consulta foi cancelada ou já passou
  - Quando abro o link
  - Então vejo "Esta consulta não está mais ativa" e o telefone da clínica
- **Cenário: link inválido ou de outra pessoa**
  - Dado que o link é inválido ou expirou
  - Quando abro o link
  - Então vejo uma mensagem genérica, sem nenhum dado de paciente
- **Regras:** a confirmação não exige login; o link vale até o horário da consulta [suposição].

**Fora do escopo:** remarcar, cancelar, ver outras consultas, envio do lembrete com o link (outra story).
**Sinal de sucesso:** [X%] dos pacientes lembrados confirmam sem ligar, e a taxa de faltas cai de [18%] para [12%] [metas assumidas; confirmar com o negócio].
**Dúvidas e suposições:** ver a seção 5.
**Qualidade (autoavaliação):** 86/100 · Tamanho: Cabe

### 5. Perguntas e suposições

- Assumi que "usuário" é o **paciente**. Se for a recepcionista confirmando em nome do paciente, o desenho muda.
- Assumi que o objetivo é **reduzir faltas**. Se for outro (por exemplo, reduzir ligações na recepção), a ordem das fatias muda.
- Os números entre colchetes (18%, 12%, 1 minuto) são suposições minhas. Troque pelos reais.
- O envio do link depende de uma story de lembrete (independência 70): esta story pode ser testada com um link gerado manualmente.

---

## Por que essas notas?

- **A nota geral é baixa por duas razões estruturais**, tamanho e critérios de aceitação, e não por detalhes de redação. Isso é típico: a maioria das stories ruins falha em escopo e verificabilidade, não em gramática.
- **Foco no problema ficou em 85** mesmo sendo uma story fraca, porque os critérios medem coisas diferentes: a story não prescreve solução alguma. Uma nota alta isolada não salva a nota geral.
- **A versão melhorada ficou em 86**, e não em 95, porque depende de uma story de lembrete (independência), usa suposições que precisam ser confirmadas e tem estimabilidade que só o time pode confirmar. Dar 95 sem esses pontos seria o tipo de inflação que a calibração pede para evitar.
