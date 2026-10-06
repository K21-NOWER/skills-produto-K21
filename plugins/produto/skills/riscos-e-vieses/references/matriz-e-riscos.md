# Matriz de Hipóteses, riscos e dependências

Conteúdo: Matriz de Hipóteses · Como conduzir · Exemplo · Riscos (evento, probabilidade, impacto) · Mapa de dependências

## Matriz de Hipóteses

Ferramenta da K21 para mapear os 4 principais riscos de investir em uma ideia, em vez de uma planilha de riscos cheia de palpites. Baseia-se em Marty Cagan (gestão de produto), Steve Blank (Four Steps to the Epiphany), Eric Ries (Lean Startup) e na validação de hipóteses do Test Card. Pré-requisito: o Tanque de Decantação feito, para escolher uma ideia priorizada.

**Material:** uma folha grande, post-its, canetas, o time e os stakeholders.

**Antes de começar:** a matriz não é prova a gabaritar. Times que respondem "sim" às perguntas antes de entender mostram um ambiente **error safe** (à prova de falhas, sem segurança para errar). O que buscamos é **safe to error**: errar rápido, aprender rápido, chegar mais cedo ao sucesso.

Desenhe uma cruz na folha (quatro partes). Em cada parte, uma pergunta:

| Pergunta | O que escrever | Exemplo de critério |
|---|---|---|
| **1. O problema existe?** | Hipótese de problema e 1 a 3 métricas que comprovam (ou comprovariam) que é real e dói o bastante | "Com 200 clientes ouvidos, ao menos 25% citam o esquecimento como motivo da inadimplência" |
| **2. A solução resolve o problema?** | Hipótese de solução e métricas de que ela resolve, em ciclos mais curtos que a solução final | "Enviar um lembrete por SMS reduz a inadimplência em pelo menos 10% entre os clientes testados" |
| **3. É economicamente viável?** | Retorno financeiro previsto para compensar o esforço, e o limite de custo | "Se a economia for de R$ 240 mil por ano, o custo de construir e manter precisa ser menor que isso" |
| **4. É tecnicamente viável?** | Critérios técnicos de sucesso: custo mensal, cobertura de testes, volumetria | "Custo mensal abaixo de R$ 1 mil, 80% de cobertura de testes, 100 mil clientes por mês" |

## Como conduzir

1. Escolha uma ideia priorizada no Tanque e o problema ligado a ela.
2. Para cada pergunta, use ciclos de 3 minutos no formato **1-2-all** (Liberating Structures): cada pessoa pensa sozinha em uma métrica, depois em pares discutem e iteram, depois o grupo escolhe as finais.
3. **"X% ou N clientes" não é uma métrica que comprove nada.** Provoque um número, mesmo que o time não tenha certeza dele, e peça que busquem o valor correto com outras áreas. Isso gera conhecimento sobre o produto que não existia.
4. Na pergunta 2, o time tende a pensar na solução final (o app). Provoque o teste mais curto, com a menor solução possível (um SMS com o código de barras, por exemplo). Se o cliente nem tem acesso à internet, não faz sentido seguir com o app.
5. Na pergunta 3, a maioria dos times não faz ideia do retorno, e esse desconhecimento costuma gerar falta de compromisso com evitar desperdício.
6. Ao final, você tem mapeados os **4 principais riscos** do investimento. Escolha o de maior incerteza e o experimento mais barato para ele (`hipoteses`).

## Exemplo (app de agendamento para clínicas, fictício)

| Pergunta | Hipótese | Como saberemos |
|---|---|---|
| O problema existe? | Pacientes faltam por esquecimento | Dos pacientes que faltaram nos últimos 3 meses, ao menos [40%] de uma amostra de 20 ligações citam esquecimento |
| A solução resolve? | Um lembrete 24h antes reduz as faltas | O grupo com lembrete tem ao menos 6 pontos percentuais menos faltas que o controle em [7 semanas] |
| É economicamente viável? | Cada falta custa [R$ 120] de receita | Reduzir 6 pontos de [400] consultas por mês economiza [R$ 2.880] por clínica; o custo de mensagens e manutenção precisa ficar abaixo disso |
| É tecnicamente viável? | Dá para enviar mensagens a partir da agenda existente | Integração em até [2 semanas] de trabalho, custo por mensagem dentro do limite, consentimento resolvido |

## Riscos: evento, probabilidade e impacto

Risco é uma incerteza com efeito positivo ou negativo. Cada risco tem:

- **Evento:** o fato gerador (perda de dados, falta de clientes, excesso de clientes).
- **Probabilidade:** a chance de ocorrer (por exemplo, 30%).
- **Impacto:** o efeito se ocorrer (prejuízo financeiro, perda de confiança, incapacidade de atendimento).

Tabela para o mapeamento:

| Risco (evento) | Domínio | Probabilidade | Impacto | Mitigação | Dono |
|---|---|---|---|---|---|

Domínios (exemplos): **negócio** (produto não aceito pelo mercado, falta de feedback, métricas mal definidas), **cultural** (medo de errar, rotatividade), **organizacional** (dependência de outro time, cadeia de aprovações), **técnico** (integração incerta, dívida técnica). Priorize pelo produto probabilidade x impacto e trate os de negócio primeiro: são os que decidem o sucesso.

**Mitigações recorrentes de negócio:** invalidar a ideia antes do alto custo (MVP, Cemitério Mexicano, Validation Board), ciclos curtos de entrega incremental e métricas acionáveis que mostrem o valor esperado.

## Mapa de dependências

Dependências travam o roadmap: o time trabalha, os dias passam e nada que o usuário possa usar é entregue. Mapeie, para cada item da fatia em foco:

| Item | Depende de | Tipo (time, sistema, decisão, fornecedor) | Dono | Data em que precisa estar pronto | Risco se atrasar |
|---|---|---|---|---|---|

Reduza dependências fatiando de forma vertical (para cada fatia caber no mesmo time), combinando acordos explícitos e deixando as dependências externas para as fatias seguintes quando possível.
