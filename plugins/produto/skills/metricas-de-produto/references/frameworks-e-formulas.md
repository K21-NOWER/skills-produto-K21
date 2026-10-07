# Frameworks de métricas e fórmulas

Conteúdo: Quais métricas devo usar (guia de frameworks) · Os 4 Domínios das Métricas · Métricas do Pirata · Fórmulas · Níveis de voo

## Quais métricas devo usar

Siglas como DORA, GEM, Pirata ou Fit for Purpose **não são métricas**. São frameworks, jeitos de organizar as milhares de métricas possíveis. Escolha pelo que você precisa responder.

| Framework | O que responde | Use quando |
|---|---|---|
| **4 Domínios da Agilidade** | Estamos olhando o todo (negócio, cultura, organização, técnica)? | Quer uma visão completa, ou classificar métricas de outros frameworks |
| **OKR** | Como ligamos a estratégia ao trabalho dos times? | Precisa de foco e alinhamento por objetivo e resultado-chave |
| **Fit for Purpose (F4P)** | O produto cumpre o propósito pelo qual o cliente o procurou? | Quer medir o que importa para o cliente (critérios de adequação) |
| **GEM** | O produto está crescendo, engajando e monetizando? | Avalia a evolução de um produto no mercado |
| **Métricas do Pirata (AARRR)** | O que o cliente faz no funil? | Quer entender aquisição, ativação, retenção, receita e recomendação |
| **North Star Metric** | Qual é o valor central que entregamos? | Quer uma métrica principal que oriente toda a estratégia |
| **Métricas Scrum e Kanban** | Como está o fluxo de trabalho? | Quer aumentar a eficiência de entrega dos times |
| **DORA** | Qual o desempenho e a maturidade da entrega e operação de software? | Time de engenharia de produto |

## Os 4 Domínios das Métricas (K21)

| Domínio | Tipo de métrica | O que avalia | Exemplos |
|---|---|---|---|
| **Negócio** | Eficácia | Resultado dos produtos, serviços e estratégia; fronteira entre cliente e empresa | Faturamento, churn, aquisição, satisfação do cliente |
| **Cultural** | Ecossistema | Satisfação de quem trabalha (geralmente qualitativa) | Health check, Radar da Satisfação, turnover, eNPS |
| **Organizacional** | Eficiência | Como o time se organiza para entregar | Lead time, vazão, taxa de descarte, taxa de chegada |
| **Técnico** | Excelência | Qualidade do que é entregue e evolução técnica | Reclamações e devoluções no período, ações de capacitação |

Um conjunto saudável não precisa de tudo, mas não pode ter um domínio relevante completamente cego.

## Métricas do Pirata (eficácia)

Cinco categorias: **Aquisição, Ativação, Retenção, Receita e Recomendação**. As métricas de eficácia ficam na fronteira entre produto e cliente e medem o quanto o produto atrai e entrega. Aquisição sozinha mede mais o marketing do que o produto: nenhum exemplo de aquisição implica uso.

## Fórmulas

**Aquisição (campanhas pagas)**

- `CTR = cliques ÷ impressões x 100`. Não espere números enormes: perto de 10% já é sucesso.
- `CPM = custo da campanha ÷ (impressões ÷ 1.000)`.
- `CPC = custo da campanha ÷ cliques`.
- `CPV = custo da campanha ÷ visitas ao site vindas do anúncio` (mais fiel que o CPC).
- `CPA = custo da campanha ÷ pontos-chave atingidos pelo cliente` (mais fiel que o CPV).
- **Taxa de rejeição:** visitas em que a pessoa sai sem interagir.

**Receita**

- `Ticket médio = soma da receita no período ÷ (soma de clientes no período x número de períodos)`.
- `LTV = ticket médio x média de compras por período x tempo de vida médio do cliente até o churn`.
- `Churn = clientes perdidos no período ÷ clientes no início do período`; `retenção = 1 - churn`.
- `Revenue churn = receita perdida no período ÷ receita no início` (versão positiva: retenção de receita).
- `Taxa de crescimento = novos clientes no período ÷ clientes no início`.
- `CAC = custo de aquisição no período ÷ novos clientes` e `LTV ÷ CAC` para ver se o crescimento se paga.

Defina sempre o período da análise, porque clientes entram e saem em momentos diferentes. Se o resultado é bom ou ruim depende do negócio: use comparação com histórico, produtos parecidos e referências do setor.

## Níveis de voo (Flight Levels)

Métricas precisam ser adaptadas ao nível em que serão usadas:

- **Nível 3, estratégico:** direção do negócio.
- **Nível 2, tático:** coordenação entre as áreas ao longo da cadeia de valor.
- **Nível 1, operacional:** times e áreas que desenvolvem produtos e serviços.

Para ver o negócio de forma sistêmica, olhe também na horizontal, não só para dentro: além das métricas internas (financeiras, de qualidade, de custo), considere as que importam para o cliente (os critérios de adequação do F4P).
