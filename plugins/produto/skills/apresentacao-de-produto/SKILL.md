---
name: apresentacao-de-produto
description: Cria e avalia apresentações de produto enxutas e de impacto, com nota de 0 a 100 por critério: modelo dos 4 slides fundamentais, Elevator Pitch (modelo de Geoffrey Moore), É Não É Faz Não Faz, Desenhe a Caixa, Aplicativo na Loja, roteiro de Sprint Review focada em feedback do cliente, e data storytelling (efeito Pah, escolha de gráficos, títulos que contam a história). Use sempre que o usuário falar de apresentar o produto para a diretoria ou stakeholders, pitch, elevator pitch, apresentação de resultados, Sprint Review, "tenho 50 slides, o que corto?", gráficos e dados para apresentar, data storytelling, reunião de resultados do produto, ou colar o roteiro ou os slides de uma apresentação para revisar, mesmo sem citar esses termos.
---

# Apresentação de produto: enxuta, com resultado e com história

A atenção é curta. Segundo Gloria Mark (Attention Span), o poder de concentração de um adulto caiu de 2,5 minutos em 2004 para 47 segundos em 2021; tarefas de alta concentração chegam a 25 minutos, e numa palestra que a pessoa quer assistir a atenção dura cerca de 7 minutos. Por isso: **menos é mais**. Cem slides esperando o "uau" do último slide é a receita de ninguém prestando atenção quando ele chega.

Esta skill monta e avalia apresentações de produto, de resultados e de Sprint Review, usando os modelos enxutos da K21, com a mesma régua de 0 a 100 das outras skills.

## Escolha o modo

- **Criar**: o usuário traz o produto e o público e quer a apresentação, o pitch ou a Review. Pedidos como "monta minha apresentação de resultados", "escreve meu elevator pitch".
- **Avaliar**: traz roteiro ou slides e quer a nota e o que cortar.
- **Avaliar e melhorar** (o mais comum): traz uma apresentação inchada e quer a versão enxuta.
- **Dados**: quer transformar números e gráficos em uma história.

Responda no idioma do usuário (padrão: português do Brasil), com tom de mentor. Nunca invente números de resultado: onde faltar dado, escreva a suposição entre colchetes.

## Primeiro, três perguntas

Antes de montar qualquer coisa: **qual o objetivo** da apresentação, **quais pontos essenciais** devem ficar e **quem é o público**. Se você não sabe qual história contar, as ferramentas são irrelevantes. Se o usuário não respondeu, declare suposições.

## Os modelos

Detalhes e exemplos em `references/modelos.md`.

| Modelo | Quando usar |
|---|---|
| **4 slides fundamentais** | Produto ou serviço que já entrega valor: apresentação periódica a gestores e diretoria |
| **Elevator Pitch (Moore)** | Despertar interesse de cliente ou investidor em menos de um minuto |
| **É, Não É, Faz, Não Faz** | Apresentar o escopo e, principalmente, o não-escopo, para alinhar expectativas |
| **Desenhe a Caixa** | Apresentar o produto como se tivesse uma embalagem: frente, lateral e fundo |
| **Aplicativo na Loja** | Apresentar o produto como numa loja de aplicativos, com feedbacks e similares |
| **Sprint Review** | Colher feedback de clientes e usuários sobre o produto em funcionamento |

### Os 4 slides fundamentais

1. **O produto** (só se o público não conhece): problema que resolve, público-alvo e solução.
2. **O valor alcançado:** o resultado, **na linguagem do público**. Gestores se interessam por redução de riscos e aprendizado; diretores dificilmente se interessam por assuntos que não tragam resultado financeiro.
3. **Feedback dos clientes,** positivo ou negativo. Não esconda a verdade.
4. **Próximos passos,** de preferência ligados ao valor do slide 2. Se a próxima reunião é na quinzena seguinte, apresente só o próximo passo principal (no singular).

Exemplo real: um PO novo levou 66 slides para a diretoria e tomou uma bronca por ter feito todos perderem tempo. Quinze dias depois levou 3+1 slides (capa, resultado financeiro das últimas sprints, feedback dos clientes, próximo passo) e o slide 2 gerou um debate tão rico que ele nem terminou a apresentação.

### Elevator Pitch (Geoffrey Moore)

```
Para [cliente-alvo]
Que [problema]
O [nome do produto] é um [categoria do produto]
Que [benefício-chave, motivo para adquirir].
Ao contrário de [alternativa primária]
Nosso produto [diferenciação primária].
```

### Sprint Review

O objetivo primário é **receber feedback de clientes, usuários ou consumidores** sobre o produto. Para isso:

- **Apresente o produto funcionando,** não documentos. Se a Review mostra papéis dizendo que o trabalho existiu, não é Review.
- **É para o cliente, não para o PO.** O PO não é cliente nem usuário. Se o que o time apresenta é uma surpresa para o PO, ele foi um PO ausente. PO que se preza senta junto ao time na Sprint e ajusta o rumo ao longo dela.
- **Não é aprovação nem julgamento.** O PO não "aprova ou rejeita" o incremento (a Definição de Pronto já diz o que é pronto).
- **O time inteiro participa,** para não transformar o PO em "menino de recados".
- **Use o ambiente real com clientes reais:** para um produto de pagamento para ambulantes, vá às ruas, e não a uma sala com ar-condicionado. Ambiente real com cliente real gera feedback valioso.
- Ganhos: relacionamento, movimento, transparência, direcionamento e cultura de melhoria contínua.

## Data storytelling

- **Efeito Pah, não Uau.** Comece pela informação mais relevante (por exemplo, o churn), nos primeiros slides, no topo do relatório, no título do gráfico. Depois detalhe.
- **Título que conta a história,** em vez de descrever o gráfico.
- **Escolha o formato pelo problema:** tabela para detalhamento ou comparação de poucos itens (poucas linhas e colunas, com uma coluna que compara grandezas diferentes); barras para comparar magnitudes em um instante; linhas para a história ao longo do tempo (o eixo Y é a história, o eixo X o período, as linhas os personagens); CFD para entender um fluxo de trabalho.
- **Destaque com cor** o que importa (vermelho para o problema, verde para o ganho) e tire o resto.

## Modo avaliar

1. Leia `references/rubrica.md`.
2. Pontue os 8 critérios de 0 a 100, citando trechos do roteiro ou dos slides.
3. Nota geral = soma de (nota x peso) dividida por 100. **Teto de bloqueio:** se qualquer critério ficar abaixo de 40, a nota geral não passa de 69.
4. Faixas: 85 a 100 Pronta para apresentar; 70 a 84 Quase lá; 50 a 69 Precisa de corte; 0 a 49 Reescrever.

| # | Critério | Peso |
|---|---|---|
| 1 | Enxuta e adequada ao tempo | 14 |
| 2 | Começa pelo mais relevante | 14 |
| 3 | Valor na linguagem do público | 14 |
| 4 | Resultado, não atividade | 14 |
| 5 | Feedback honesto de clientes | 10 |
| 6 | Próximo passo claro | 10 |
| 7 | Dados que contam uma história | 14 |
| 8 | Clareza do pitch | 10 |

Formato de saída: nota no topo; tabela por critério com evidência e melhoria; o que mais pesa; **apresentação reescrita** (slide por slide, em uma linha cada); suposições. Calibre com rigor: apresentações comuns ficam entre 25 e 60.

Para as métricas que entram na apresentação, use `metricas-de-produto`. Para a visão e o posicionamento por trás do pitch, use `visao-do-produto`. Para ver uma avaliação completa, leia `references/exemplo.md`.
