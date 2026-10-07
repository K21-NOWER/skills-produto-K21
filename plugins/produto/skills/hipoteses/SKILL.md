---
name: hipoteses
description: Avalia hipóteses de produto, negócio ou crescimento e as transforma em ação. Dá notas de 0 a 100 para a qualidade da hipótese (clareza, público, falseabilidade, mensurabilidade, fundamento, foco, conexão com o resultado, testabilidade), reescreve em formato testável, lista as suposições e os riscos, sugere experimentos baratos com métricas e critérios de sucesso definidos antes, monta um Test Card 2.0 (modelo da K21) e converte a hipótese em uma user story com critérios de aceitação, usando a skill user-story. Use sempre que o usuário falar de hipótese, "acredito que", "acho que se a gente...", experimento, teste A/B, MVP, validação de ideia, Test Card, Learning Card, discovery, métricas de sucesso, riscos de uma ideia, ou quiser saber como testar algo antes de construir, mesmo sem usar a palavra hipótese.
---

# Hipóteses: avaliar, testar e transformar em story

Uma ideia é uma aposta. Uma hipótese é uma aposta com dono, prazo e um jeito claro de ser derrubada. Discutir < Experimentar: o jeito mais barato de saber se uma ideia presta quase nunca é uma reunião, é um teste pequeno com um critério definido antes. Velocidade com métrica é estratégia; velocidade sem métrica é aposta.

Esta skill pega o que o usuário chamou de hipótese (ou só de "ideia") e faz cinco coisas: avalia se está bem formulada, reescreve em formato testável, desmonta nas suposições que a sustentam, desenha experimentos e métricas com riscos, e transforma o que vale construir em uma user story pronta para o time.

## Dois conceitos que não se misturam

- **Critério de sucesso da hipótese** responde "funcionou para o usuário e para o negócio?". Ele é definido **antes** do teste, para não ajustar a régua ao resultado.
- **Critérios de aceitação da user story** respondem "ficou pronto?". Eles verificam que a coisa foi construída como combinado.

Uma coisa pode estar perfeitamente pronta e não ter funcionado. A segunda pergunta é a que mais se esquece, e é por isso que esta skill sempre mantém as duas separadas.

## Fluxo

### 1. Entender e reescrever

Extraia a crença por trás do que o usuário escreveu. Se ele trouxe uma solução ("precisamos de um chat"), pergunte-se qual crença sobre o cliente ou o negócio faria dessa solução uma boa ideia, e escreva essa crença. Reescreva no formato do Test Card 2.0 da K21, que divide a hipótese em duas partes para evitar hipótese sem expectativa de resultado, métricas desequilibradas e métricas enviesadas pela solução e não pelo problema:

> **Nós acreditamos que** [ação ou mudança, para um público específico] **resultará em** [resultado observável], **porque** [insight ou evidência].

A métrica, o critério numérico e o prazo vão para o Test Card (passos 5 e 7). Onde faltar informação (público, número, prazo), escreva a suposição entre colchetes para o usuário confirmar. Nunca invente evidência: se o "porque" é intuição, escreva "intuição, sem evidência ainda".

**Invalidar em vez de validar.** Ao tentar validar uma ideia, tendemos a provar o quanto ela é boa (viés da confirmação) e a nos apegar à solução (viés da solução). Parta do princípio de que a ideia é ruim e tente derrubá-la: se sobreviver, ela merece ser construída; se não, vai para o Cemitério Mexicano (veja a skill `discovery-com-clientes`).

### 2. Avaliar a qualidade da hipótese

Leia `references/rubrica.md`. Dê uma nota de 0 a 100 para cada um dos 8 critérios, com evidência citada do texto original do usuário (nota sem evidência vira opinião):

| # | Critério | Peso | Pergunta que a nota responde |
|---|---|---|---|
| 1 | Clareza e especificidade | 12 | Diz exatamente o que muda, para quem e com qual resultado? |
| 2 | Público | 10 | O segmento é específico e alcançável para o teste? |
| 3 | Falseabilidade | 16 | Existe um resultado concreto que derrubaria a hipótese? |
| 4 | Mensurabilidade | 16 | Tem métrica, linha de base, critério numérico e prazo? |
| 5 | Fundamento | 12 | Há evidência ou insight por trás, ou é só opinião? |
| 6 | Foco | 10 | Testa uma suposição central ou é um pacote de crenças? |
| 7 | Conexão com o resultado | 10 | Liga a um objetivo ou problema que importa e a métrica é a que importa? |
| 8 | Testabilidade | 14 | Dá para testar rápido, barato, com acesso ao público e dentro da ética e da lei? |

Nota geral = soma de (nota x peso) dividida por 100, arredondada.

- **Teto de bloqueio:** se qualquer critério ficar abaixo de 40, a nota geral não passa de 69.
- **"Ainda é uma ideia":** se **falseabilidade** ou **mensurabilidade** ficar abaixo de 40, classifique como "ainda é uma ideia, não uma hipótese", qualquer que seja a nota geral. Sem poder ser derrubada nem medida, não há o que testar, e a reescrita do passo 1 vira a entrega principal.

| Nota geral | Faixa |
|---|---|
| 85 a 100 | Pronta para testar |
| 70 a 84 | Quase lá |
| 50 a 69 | Precisa de refinamento |
| 0 a 49 | Ainda é uma ideia |

**Calibração:** hipóteses informais costumam ficar entre 30 e 65. Reserve 90 ou mais para uma hipótese que você testaria amanhã sem mudar nada. Se todos os critérios saírem acima de 85, releia procurando o que passou despercebido.

Além da nota, indique a **criticidade** da hipótese: **Alta** se, estando errada, derruba a iniciativa inteira; **Média** se obriga a mudar o plano; **Baixa** se muda só um detalhe. A nota mede se a hipótese está bem formulada; a criticidade mede o quanto vale testar.

### 3. Desmontar em suposições

Uma hipótese quase sempre embute várias suposições. Liste-as e classifique cada uma por **tipo de risco**:

- **Desejabilidade (valor):** as pessoas querem isso? O problema existe e dói?
- **Usabilidade:** conseguem usar?
- **Viabilidade técnica:** conseguimos construir?
- **Viabilidade de negócio:** faz sentido financeira e legalmente?

Para cada uma, dê **importância** (se estiver errada, a hipótese cai?) e **evidência atual** (o que já sabemos, de verdade?). A suposição de **importância alta e evidência baixa** é o "salto de fé": é ela que deve ser testada primeiro.

### 4. Sugerir experimentos

Leia `references/experimentos.md` para o catálogo. Proponha de 2 a 3 experimentos para o salto de fé, **do mais barato ao mais robusto**, e recomende um. Princípio: o teste mais barato que ainda gera evidência forte o bastante para decidir.

Lembre-se da escada de evidência: o que as pessoas **dizem** vale menos do que o que elas **fazem**, e o que fazem vale menos do que aquilo a que se **comprometem** (pagar, dar tempo, dar dados). Prefira testes mais altos na escada quando o custo permitir.

Para cada experimento, informe: o que fazemos, custo e tempo, o que mede, o que prova e o que não prova, e a principal limitação.

### 5. Métricas e critério de sucesso

Leia `references/metricas-e-riscos.md`. Defina:

- **Métrica principal** (a que decide), **vinculada ao problema e não à solução**, com linha de base. Se não houver baseline, o primeiro passo do teste é medi-la. Exemplo: para reduzir a perda de clientes, o contrato assinado ou a quantidade de conteúdo não medem o problema; o churn mede.
- **Métricas de equilíbrio** (guardrails): 1 ou 2 métricas que equilibram a principal e evitam efeito perverso. Medir só uma métrica leva o time a perseguir o número a qualquer custo (reduzir o churn oferecendo 20 meses grátis pode quebrar a empresa e barrar a entrada de novos clientes). Pares típicos: churn, revenue churn e taxa de crescimento. Podem ser negativas ou positivas (retenção em vez de churn).
- **Critérios de sucesso** numéricos, prazo e tamanho de amostra razoáveis, definidos **antes** de rodar. Podem vir de números de outras empresas do segmento, de comparação com produtos parecidos da empresa, do histórico do produto ou do **CHUTE** (Cálculo de Hipóteses Únicas para Teste e Experimentação): sempre há espaço para algo subjetivo, mas declare. Isso evita métricas de vaidade e "ajustar" o resultado depois para comprovar um sucesso que não existe.
- **Regra de decisão:** o que fazemos se confirmar, se refutar e se der inconclusivo.

### 6. Riscos

Liste os riscos do **teste** e da **hipótese**, em tabela: risco, tipo, probabilidade, impacto e mitigação. Inclua sempre uma checagem de ética, privacidade (LGPD) e viés. Veja `references/metricas-e-riscos.md`.

### 7. Montar o Test Card 2.0

Resuma o experimento recomendado no **Test Card 2.0 da Nower e K21**, uma evolução mais sintética do Test Card original de David Bland e Alexander Osterwalder (Strategyzer):

| Campo | Conteúdo |
|---|---|
| **Identificação do teste** | Nome curto, número na ferramenta de gestão ou descrição sucinta do que se testa |
| **Limite de tempo** | Prazo máximo: uma data ligada a um evento, X sprints ou semanas, ou uma data fixa |
| **Hipótese** | **Nós acreditamos que**... (a ação). **Resultará em**... (o resultado esperado) |
| **Métricas** | **Principal:** vinculada ao problema. **Equilíbrio 1 e 2:** protegem o resto |
| **Experimento** | Descrição sucinta, verificável empiricamente, do que será feito |
| **Critérios** | Resultados numéricos esperados nas métricas que comprovam ou refutam a hipótese, com a origem |
| Custo, tempo e confiabilidade da evidência | baixo, médio ou alto (opcional) |
| Responsável | [a definir] |

**Três cuidados ao executar** (K21):

1. **Não mexa em muitas variáveis em um mesmo experimento.** Se você muda catálogo, preço e mercado ao mesmo tempo e o resultado vem, não dá para saber o que causou. O ideal é um experimento por vez; quando for inevitável testar em paralelo, isole os resultados o máximo possível.
2. **Não reduza os critérios depois.** 10% não está "pertinho" de 50%. Boas ideias são diferentes de ideias de valor.
3. **Experimentos devem ser curtos.** Experimentos longos, se invalidados, dão muito trabalho para ser desfeitos. É melhor fazer muitos experimentos pequenos do que poucos longos.

Fatie o experimento para que o resultado se ligue diretamente à causa: "porque fizemos isso, o resultado foi esse".

**Learning Card (depois do teste).** Registre o aprendizado: **Identificação** (nome do insight, data, responsável), **Hipótese** (a mesma do Test Card, no passado: "nós acreditávamos que..."), **Observação** (o que as métricas mostraram), **Aprendizados e insights** e **Decisões e ações** (a decisão tomada ou o próximo experimento). Um Test Card pode ter vários Learning Cards.

### 8. Transformar em user story

Gere uma user story da **menor fatia que permite aprender**. Chame a skill `user-story` no **modo criar** (quando instalada pelo plugin, o nome completo é `produto:user-story`) e passe a hipótese reescrita, a persona, o experimento recomendado e o critério de sucesso. A story deve seguir o padrão da skill `user-story` e, por ser a story de um experimento, incluir nos critérios de aceitação:

- **O comportamento mínimo** que permite testar a hipótese (e nada além disso: o que não é necessário para aprender vai em "Fora do escopo").
- **Exposição controlada:** quem vê e quem não vê (grupo de teste e controle, percentual da base, convite), e como desligar o experimento.
- **Instrumentação:** os eventos e dados que alimentam a métrica (o que é registrado, quando, com quais propriedades).
- **Privacidade:** consentimento e uso de dados pessoais, quando se aplica.

O campo **"Sinal de sucesso"** da story recebe o critério de sucesso da hipótese. Ele **não** é critério de aceitação.

Se a skill `user-story` não estiver disponível, escreva a story neste mínimo: "Como [persona], quero [mínimo necessário], para [benefício]", com 3 a 6 cenários Dado/Quando/Então (comportamento, exposição, instrumentação), "Fora do escopo" e "Sinal de sucesso".

Se o melhor experimento **não exige construir nada** (entrevistas, página de captura em ferramenta pronta, concierge manual), diga isso claramente. Mesmo assim entregue a story da primeira fatia da solução, marcada como **"não construir antes do resultado do teste"**: ela fica pronta no backlog para o caso de a hipótese se confirmar.

### 9. O que fazer depois do teste

Escreva a regra de decisão combinada com o critério de sucesso:

- **Se confirmar** (atingiu o critério): persistir, construir a fatia seguinte e mirar a próxima suposição.
- **Se refutar:** pivotar (mudar a solução ou o público) ou abandonar; registrar o aprendizado no Learning Card. Uma ideia refutada cedo é motivo de festa (Cemitério Mexicano): poupou meses de trabalho.
- **Se for inconclusivo** (amostra pequena, resultado no meio): dizer que é inconclusivo, não forçar uma conclusão, e decidir entre estender o teste ou mudar o método.

Antes de investir, rode também a **Matriz de Hipóteses** com a skill `riscos-e-vieses`: o problema existe, a solução resolve, é economicamente viável, é tecnicamente viável.

## Formato de saída

Para **uma hipótese**, use as seções abaixo. Adapte ao pedido: se o usuário quiser só avaliar, entregue 1 a 3; se quiser só os experimentos, 4 a 6. Ofereça o resto no fim.

```
## Análise da hipótese: [título curto]

**Qualidade da hipótese: NN/100** (faixa) · **Criticidade:** Alta/Média/Baixa

### 1. Hipótese reescrita
> Acreditamos que ...

### 2. Notas por critério
| Critério (peso) | Nota | Por quê (evidência) | Como melhorar |
|---|---|---|---|

### 3. Suposições por trás
| Suposição | Tipo de risco | Importância | Evidência atual | Testar primeiro? |
|---|---|---|---|---|

### 4. Experimentos sugeridos (do mais barato ao mais robusto)
(2 ou 3 opções) + **Recomendação:** [uma frase]

### 5. Métricas e critério de sucesso
Principal, equilíbrio, apoio, baseline, critério numérico, prazo e amostra, regra de decisão.

### 6. Riscos
| Risco | Tipo | Prob. | Impacto | Mitigação |
|---|---|---|---|---|

### 7. Test Card 2.0
(tabela do passo 7)

### 8. User story pronta para o time
(saída da skill user-story)

### 9. O que fazer depois do teste
Se confirmar... Se refutar... Se inconclusivo...
```

Mostre a nota no topo. Mantenha cada seção enxuta: o valor está em decisões claras, não em volume.

### Várias hipóteses de uma vez

Comece por uma **tabela-resumo** (hipótese, nota, criticidade, salto de fé, experimento mais barato). Ofereça **priorizar** as hipóteses com a skill `priorizacao` (ICE costuma servir bem: impacto, confiança, facilidade) e detalhe no formato completo só as 1 ou 2 mais críticas, ou as que o usuário pedir.

## Princípios

- **Hipótese é aposta com jeito de perder.** Se nenhum resultado pode derrubá-la, ela é uma crença, não uma hipótese.
- **O critério vem antes do teste.** Definir o sucesso depois de ver o resultado é um jeito sofisticado de se enganar.
- **Teste a suposição mais arriscada primeiro**, não a mais fácil de testar.
- **Comportamento vale mais que opinião.** Perguntar "você usaria?" gera simpatia, não evidência. Observar o que a pessoa faz, ou pedir um compromisso real, gera evidência.
- **Aprender é um resultado.** Uma hipótese refutada cedo e barato é um bom resultado, não um fracasso.

Para ver uma análise completa, leia `references/exemplo.md`.
