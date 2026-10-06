# Catálogo de experimentos

Conteúdo: Escada de evidência · Como escolher · Os experimentos (1 a 12) · Armadilhas comuns

## Escada de evidência

Nem toda evidência vale o mesmo. Suba na escada sempre que o custo permitir.

| Nível | Tipo | Exemplo | Força |
|---|---|---|---|
| 1 | **Opinião** | "Acho que o cliente quer isso" | Fraca |
| 2 | **O que as pessoas dizem** | Respostas em entrevista ou pesquisa | Fraca a média |
| 3 | **O que as pessoas fazem** | Cliques, uso, cadastro, retorno | Média a forte |
| 4 | **O que as pessoas pagam ou assumem como compromisso** | Pré-venda, carta de intenção, tempo ou dados entregues | Forte |

Perguntar "você usaria?" gera simpatia, não evidência. Perguntar "como você resolve isso hoje e quanto custa?" gera fatos sobre o passado.

## Como escolher

1. Identifique o **tipo de risco** da suposição mais arriscada.
2. Escolha o experimento mais barato **daquele tipo** que ainda gera evidência forte o bastante para decidir.
3. Confira o que você precisa para rodar: acesso ao público, dados, tempo.

| Tipo de risco | Experimentos que costumam servir |
|---|---|
| **Desejabilidade** (as pessoas querem?) | Entrevistas, análise de dados existentes, landing page, porta falsa, pré-venda, concierge |
| **Usabilidade** (conseguem usar?) | Protótipo clicável com teste de usabilidade, Mágico de Oz |
| **Viabilidade técnica** (conseguimos?) | Spike ou prova de conceito com limite de tempo |
| **Viabilidade de negócio** (vale a pena?) | Pré-venda, concierge com preço real, conta simples de margem unitária |

---

## Os experimentos

Cada ficha traz: o que é, quando usar, custo e tempo, evidência, como rodar, métrica típica e armadilhas.

### 1. Entrevistas de problema

- **O que é:** conversas de 30 a 40 minutos com pessoas do público, sobre a vida delas, não sobre a sua ideia.
- **Quando usar:** para saber se o problema existe, com que frequência dói e como é resolvido hoje.
- **Custo e tempo:** baixo; 1 a 2 semanas.
- **Evidência:** nível 2 (o que dizem). Forte para o problema, fraca para prever o que farão com a sua solução.
- **Como rodar:** pergunte sobre o passado e sobre fatos ("quando foi a última vez?", "o que você fez?", "quanto custou?"). Evite descrever a ideia e perguntar se gostam. Entreviste de 5 a 8 pessoas por segmento e pare quando as respostas começarem a se repetir.
- **Métrica típica:** proporção que descreve o problema sem ser induzida; frequência; solução atual; quanto já gasta.
- **Armadilhas:** entrevistar amigos e família (viés de simpatia); induzir a resposta; contar elogios como evidência.

### 2. Pesquisa (survey)

- **O que é:** questionário curto para um público maior.
- **Quando usar:** quando você já sabe o que perguntar e quer medir a prevalência de algo.
- **Custo e tempo:** baixo; dias.
- **Evidência:** nível 2.
- **Métrica típica:** percentual que declara o problema; ordem de importância das dores.
- **Armadilhas:** perguntas que induzem; amostra viciada; confundir opinião declarada com comportamento.

### 3. Análise de dados existentes

- **O que é:** olhar o que já existe: analytics, tickets de suporte, buscas no site, funil, vendas.
- **Quando usar:** sempre como primeiro passo, se os dados existirem.
- **Custo e tempo:** muito baixo; horas ou dias.
- **Evidência:** nível 3, sobre o comportamento passado.
- **Armadilhas:** dados incompletos ou mal instrumentados; correlação confundida com causa.

### 4. Landing page (teste de fumaça)

- **O que é:** uma página que apresenta a proposta de valor com uma chamada para ação (lista de espera, pré-cadastro, agendar demonstração).
- **Quando usar:** para medir interesse em uma proposta de valor nova.
- **Custo e tempo:** baixo; 1 a 2 semanas (inclui tráfego pago, se não houver audiência).
- **Evidência:** nível 3 (interesse demonstrado). Mais forte se a chamada pede dados ou compromisso.
- **Métrica típica:** taxa de conversão da visita para a chamada; custo por contato.
- **Armadilhas:** tráfego do público errado; texto que promete mais do que o produto entrega; ler um bom resultado como prova de que vão pagar.

### 5. Porta falsa (fake door)

- **O que é:** um botão ou item de menu, dentro de um produto que já existe, para uma funcionalidade que ainda não existe. Quem clica vê uma mensagem honesta ("estamos construindo, quer ser avisado?").
- **Quando usar:** para medir demanda por uma funcionalidade dentro do contexto real de uso.
- **Custo e tempo:** baixo; dias.
- **Evidência:** nível 3.
- **Métrica típica:** percentual de quem viu e clicou; percentual que deixa o contato.
- **Armadilhas:** frustrar clientes (use mensagem honesta e um caminho alternativo); posição do botão influenciando os cliques; testar em amostra pequena demais.

### 6. Pré-venda ou carta de intenção

- **O que é:** pedir um compromisso real antes de construir: pagamento antecipado, depósito, carta de intenção assinada.
- **Quando usar:** para validar disposição de pagar e preço.
- **Custo e tempo:** baixo a médio; semanas.
- **Evidência:** nível 4, a mais forte.
- **Métrica típica:** número de compromissos firmados; preço aceito.
- **Armadilhas:** prometer o que não consegue entregar; pressão que gera um sim educado e não um compromisso real.

### 7. Concierge (serviço manual)

- **O que é:** entregar o valor manualmente, de ponta a ponta, para poucos clientes, sem automação.
- **Quando usar:** para aprender o que o cliente realmente valoriza e como o processo funciona, antes de automatizar.
- **Custo e tempo:** médio (tempo da equipe); 2 a 6 semanas.
- **Evidência:** nível 3 a 4, especialmente se o cliente paga.
- **Métrica típica:** retenção, satisfação, disposição de pagar, tempo gasto por cliente.
- **Armadilhas:** o que funciona manualmente pode não escalar; poucos clientes e muito esforço por cliente podem distorcer a leitura.

### 8. Mágico de Oz

- **O que é:** a interface parece automática para o cliente, mas por trás há trabalho manual.
- **Quando usar:** para testar a experiência e o valor percebido de algo que seria caro de automatizar.
- **Custo e tempo:** médio; semanas.
- **Evidência:** nível 3.
- **Armadilhas:** tempos de resposta manuais mais lentos que o produto real; custo oculto do trabalho manual.

### 9. Protótipo clicável e teste de usabilidade

- **O que é:** um protótipo (por exemplo, no Figma) que as pessoas tentam usar enquanto você observa.
- **Quando usar:** para o risco de usabilidade: "conseguem usar?"
- **Custo e tempo:** baixo a médio; 1 a 2 semanas.
- **Evidência:** nível 3 sobre a usabilidade; não prova que vão usar de verdade.
- **Como rodar:** de 5 a 8 pessoas por perfil já revelam os problemas mais recorrentes. Peça que cumpram tarefas, sem explicar como, e observe onde travam.
- **Métrica típica:** taxa de conclusão da tarefa; tempo; erros; onde hesitam.
- **Armadilhas:** explicar demais durante o teste; confundir "gostou do visual" com "conseguiu resolver o problema".

### 10. Teste A/B

- **O que é:** duas versões rodando ao mesmo tempo para grupos sorteados; compara-se a métrica.
- **Quando usar:** quando há tráfego suficiente e uma métrica clara.
- **Custo e tempo:** médio a alto (precisa de construção e instrumentação); semanas.
- **Evidência:** nível 3, forte para causalidade se bem feito.
- **Como rodar:** sorteie por usuário; rode por ciclos semanais completos; calcule o tamanho da amostra antes (veja `metricas-e-riscos.md`); defina a regra de parada antes e **não pare ao ver um resultado bom**.
- **Armadilhas:** amostra pequena; olhar o resultado cedo demais; várias métricas e vários cortes até aparecer algo "significativo"; grupos que não são realmente comparáveis.

### 11. Piloto, beta fechado ou lançamento gradual

- **O que é:** liberar a solução para um grupo pequeno (poucos clientes ou um percentual da base), por meio de convite ou feature flag, e comparar com o grupo que não recebeu.
- **Quando usar:** depois que testes mais baratos sustentaram a hipótese e é preciso ver o uso real.
- **Custo e tempo:** médio a alto; semanas.
- **Evidência:** nível 3 a 4.
- **Métrica típica:** adoção, retenção, comparação com o grupo de controle.
- **Armadilhas:** piloto com clientes "amigáveis" (viés de seleção); efeito novidade que some depois de semanas.

### 12. MVP funcional (fatia mínima)

- **O que é:** a menor versão real do produto que entrega o valor.
- **Quando usar:** só quando o risco não pode ser testado por um experimento mais barato.
- **Custo e tempo:** alto; semanas a meses.
- **Evidência:** nível 3 a 4.
- **Armadilhas:** chamar de "MVP" uma versão grande demais; construir antes de testar o salto de fé. Use a skill `user-story` para fatiar.

---

## Armadilhas comuns

- **Testar o que é fácil, não o que é arriscado.** Comece pelo salto de fé.
- **Definir o critério de sucesso depois de ver o resultado.** Escreva antes.
- **Um teste caro para uma pergunta barata.** Se uma conversa responde, não construa.
- **Um teste barato demais para uma pergunta cara.** Dizer "sim, compraria" em pesquisa não prova disposição de pagar.
- **Amostra pequena e conclusões grandes.** Resultado com poucos dados é indício, não prova.
- **Ignorar o resultado que contraria a ideia.** Uma hipótese refutada é aprendizado. Registre.
