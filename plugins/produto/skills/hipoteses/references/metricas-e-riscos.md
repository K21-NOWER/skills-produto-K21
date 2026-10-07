# Métricas, critérios de sucesso e riscos

Conteúdo: Tipos de métricas · Boas práticas · Critério de sucesso e regra de decisão · Amostra e estatística · Riscos (tipos e como listar) · LGPD e ética

---

## Tipos de métricas

| Tipo | Papel | Exemplo (lembrete antes da consulta) |
|---|---|---|
| **Principal** | A que decide. Só uma, vinculada ao problema e não à solução. | Taxa de faltas |
| **De apoio** | Explicam o porquê do resultado | Entrega e leitura da mensagem; taxa de confirmação |
| **De equilíbrio (guardrail)** | Equilibram a principal e impedem dano em outro lugar. Medir uma só leva o time a perseguir o número a qualquer custo | Cancelamentos de última hora; reclamações e opt-out; taxa de crescimento |

**Indicador antecedente e indicador resultado.** Antecedente (leading) é o que muda primeiro e permite reagir (taxa de confirmação). Resultado (lagging) é o que importa de fato, mas demora (faltas, receita). Use os dois: o antecedente para acompanhar durante o teste, o resultado para decidir.

**Métricas de ação e de vaidade.** Métrica de ação liga-se a um comportamento que muda decisões (conversão, retenção, receita por cliente). Métrica de vaidade só enfeita (visitas, curtidas, downloads). Uma hipótese medida por vaidade é difícil de falsear.

**Ajudas para escolher** (quando o usuário não souber por onde começar):

- **AARRR (métricas piratas):** Aquisição (como chegam), Ativação (primeiro valor), Retenção (voltam), Receita (pagam), Indicação (recomendam). Escolha a etapa em que a hipótese mexe.
- **HEART (experiência):** Felicidade, Engajamento, Adoção, Retenção, Sucesso da tarefa.

---

## Boas práticas

1. **Defina a métrica, a unidade e a janela antes.** "Taxa de faltas por consulta agendada, medida em 4 semanas".
2. **Tenha uma linha de base.** Sem baseline, "melhorou" não significa nada. Se não existe, o primeiro passo do teste é medi-la.
3. **Compare grupos ao mesmo tempo**, não "antes e depois". Sazonalidade, feriados e campanhas contaminam comparações no tempo. Um grupo de controle sorteado resolve.
4. **Defina a métrica de equilíbrio.** Um bom resultado na métrica principal que quebra a de equilíbrio é um resultado ruim.
5. **Registre o que será medido e como** antes de começar. É o que impede o ajuste da régua depois.

---

## Critério de sucesso e regra de decisão

**Critério de sucesso:** numérico, com prazo e tamanho de amostra. Exemplo: "o grupo com lembrete tem pelo menos 6 pontos percentuais menos faltas que o controle, com pelo menos 650 consultas por grupo, em até 7 semanas".

**Regra de decisão** (escreva antes de rodar):

| Resultado | O que fazer |
|---|---|
| Atingiu o critério | Persistir: construir a fatia seguinte e testar a próxima suposição |
| Ficou abaixo, mas com sinal parcial | Investigar por segmento e mudar a solução, antes de abandonar |
| Ficou muito abaixo | Pivotar ou abandonar; registrar o aprendizado |
| Amostra pequena ou resultado no meio | Dizer que é **inconclusivo**; estender o teste ou mudar o método. Não forçar uma conclusão |

---

## Amostra e estatística

Esta seção é um guia de bolso, não substitui um estatístico quando a decisão é cara.

- **Pouca amostra = indício, não prova.** Com poucas dezenas de observações, só efeitos enormes são visíveis. Diga "indício" e planeje o próximo teste.
- **Qualitativo (entrevistas):** de 5 a 8 pessoas por segmento até as respostas começarem a se repetir.
- **Quantitativo com uma métrica de proporção** (conversão, faltas): uma aproximação conhecida (regra de Lehr, para 95% de confiança e 80% de poder) para o tamanho de cada grupo é

  `n por grupo ≈ 16 x p x (1 - p) / d²`

  em que `p` é a taxa atual e `d` é a diferença absoluta que você quer detectar. Exemplo: taxa atual de 18% de faltas e queda mínima de 6 pontos percentuais: `16 x 0,18 x 0,82 / 0,06² = 2,36 / 0,0036 ≈ 656` por grupo. Se a taxa atual é 10% e você quer detectar 2 pontos: `16 x 0,10 x 0,90 / 0,02² = 3.600` por grupo. Detectar diferenças pequenas custa muita amostra.
- **Não pare ao ver um resultado bom.** Olhar o resultado todo dia e parar quando "deu certo" infla os falsos positivos. Defina a duração antes.
- **Ciclos completos.** Rode por semanas inteiras para cobrir o ciclo de comportamento (dias úteis e fins de semana).
- **Muitas métricas, muitos cortes** até algo aparecer é o jeito mais comum de se enganar. Uma métrica primária, definida antes.

---

## Riscos

Liste os riscos da **hipótese** (podem estar errados os pressupostos) e do **teste** (o teste pode dar errado ou causar dano). Para cada um: tipo, probabilidade (alta, média, baixa), impacto e mitigação.

| Tipo | O que pode dar errado | Exemplo de mitigação |
|---|---|---|
| **Desejabilidade (valor)** | O problema não existe, ou a causa é outra | Entrevistas e dados antes de construir |
| **Usabilidade** | Quem queria não consegue usar | Teste de protótipo com 5 a 8 pessoas |
| **Viabilidade técnica** | Não conseguimos construir no prazo ou custo | Spike com limite de tempo |
| **Viabilidade de negócio** | Não fecha a conta ou fere regra de negócio | Margem unitária simples; pré-venda com preço real |
| **Ético e legal** | Uso indevido de dados, consentimento, discriminação | Revisar com jurídico ou encarregado de dados; minimizar dados |
| **Reputação e confiança** | Porta falsa frustra cliente; preço de teste vaza | Mensagem honesta; limitar exposição |
| **Risco do próprio experimento** | Contaminar a base atual; atrapalhar clientes; canibalizar receita | Pequenos grupos; botão de desligar; guardrails |
| **Viés** | Amostra viciada; efeito novidade; viés de confirmação | Sortear grupos; testar por semanas; critério definido antes |

---

## LGPD e ética (Brasil)

Experimentos que usam dados pessoais precisam de cuidado desde o desenho. Pontos de atenção, que **não substituem** a orientação de um profissional jurídico:

- **Base legal** para tratar os dados (consentimento, execução de contrato, legítimo interesse, entre outras). Descubra qual se aplica antes de coletar.
- **Finalidade e minimização.** Colete só o que o teste exige e use só para o que foi informado.
- **Transparência e opt-out.** A pessoa deve saber que seus dados serão usados e conseguir sair com facilidade.
- **Canais com regras próprias** (por exemplo, mensagens por WhatsApp têm políticas de consentimento e de modelos de mensagem aprovados pela plataforma).
- **Experimentos com consequência real** (preço, acesso a serviço de saúde, crédito) merecem um olhar de ética extra: quem pode ser prejudicado e como evitamos?
- **Dados de crianças, de saúde e outros sensíveis** têm regras mais rígidas. Pare e consulte quem entende antes de testar.
