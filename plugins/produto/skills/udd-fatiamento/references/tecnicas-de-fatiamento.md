# Técnicas de fatiamento de produto

Conteúdo: Fatia, camada e etapa · Pergunta do epicentro · As técnicas · Padrão 1-2-N · Como escolher a primeira fatia · Armadilhas

Para fatiar uma **única história** (padrões de Lawrence, SPIDR), veja a skill `user-story`. Aqui o foco é o produto inteiro.

## Fatia, camada e etapa

- **Fatia:** item do backlog sem dependência dos demais, que pode ser entregue para uso, avaliação e feedback de clientes e stakeholders. Toda vez que entrega uma fatia, observe as métricas de uso e de negócio: elas dizem qual é a próxima.
- **Camada:** item técnico necessário para criar a fatia (tabelas, consultas, serviços, tela). Importa, mas sozinha não agrega valor. Você não entrega um comando SQL ao consumidor.
- **Etapa:** parte do fluxo de desenvolvimento. Se o time tem uma "fatia" de planejamento, outra de desenvolvimento e outra de testes, isso não é fatiamento.

## Pergunta do epicentro

"Qual é a parte mais importante do problema mais importante do usuário mais importante?"

Responda, desenvolva a funcionalidade mínima que resolve essa parte, coloque em uso, colete os resultados e adapte. Repita. Começar pelo epicentro é a forma de mostrar valor com uma entrega menor.

## As técnicas (exemplo: e-commerce)

1. **Fluxo do consumidor.** Mapeie o fluxo e entregue etapas dele: buscar, escolher, carrinho, endereço, pagamento, receber. Mesmo só com a busca já dá para avaliar: convide consumidores a usá-la e observe o que fazem. Daí saem novos itens, e os desnecessários caem.
2. **Informações de entrada e de saída.** Nem toda informação é necessária na primeira fatia. A busca pode começar só pelo nome do produto, e filtros (marca, tamanho, avaliação) viram fatias seguintes. Na saída, também: para um relatório de vendas por região, a 1ª fatia pode ser os dados brutos numa planilha, a 2ª os dados condensados por cidade, estado e região, a 3ª com gráficos, a 4ª um mapa clicável. Muitas vezes a 4ª nunca é feita, porque o gestor já decidiu com a 1ª: ótimo, era esforço demais para pouco retorno.
3. **Canal de integração.** Boleto e cartão de crédito são duas fatias; dentro do cartão, cada bandeira. O primeiro canal já permite começar a vender. Conheça os canais mais importantes.
4. **Plataforma.** Conheça seu consumidor e como ele chega. Descarte as plataformas insignificantes ou incompatíveis com os objetivos.
5. **Operações (CRUD).** Comece pelas consultas; a inserção pode ser por planilha ou comando direto; depois criar, excluir, e só então editar.
6. **Tipo de consumidor.** Pessoa física e jurídica, gerente e cliente final têm interesses e formas de uso diferentes: atenda um tipo de cada vez.

## Padrão 1-2-N

Criado no eXtreme Programming (Kent Beck), serve para produto, gestão, ensino, entrevistas e inovação:

- **1:** o caso mais básico ou ideal.
- **2:** uma variação ou exceção significativa.
- **N:** generaliza para todos os cenários.

Exemplos: **entrevistas**, em vez de mandar um questionário para 200 pessoas, entreviste uma, ajuste o roteiro, entreviste outra, ajuste, e só então vá às 200. **Lançamento**, em vez de lançar no país, lance num bairro, ajuste, lance numa cidade, ajuste, e então generalize. **Campanha**, apresente a um grupo numa rede, ajuste, depois outra rede. É possível ter 1, 2, 3, 4, N, mas não acrescente passos demais: uma hora você chega ao N ou alguém (gerente, diretor, investidor) chega por você.

## Como escolher a primeira fatia

1. Liste o que o usuário mais importante tenta resolver hoje e como resolve (alternativa atual).
2. Escolha a parte do problema que, se resolvida, já muda o comportamento dele.
3. Reduza até caber em dias ou poucas semanas de trabalho e puder ser usada por poucas pessoas reais.
4. Defina o comportamento que prova valor e o critério numérico, antes de construir.
5. Pergunte: o que dá para fazer manualmente nesta primeira fatia (concierge, planilha, disparo manual) para aprender antes de automatizar?

## Armadilhas

- **Fatiar por camada.** Entrega só infraestrutura e adia o aprendizado.
- **Fatiar demais.** Fatias tão pequenas que ninguém consegue usar ou medir.
- **Escolher a mais fácil.** O epicentro é a mais importante, não a mais fácil.
- **Roadmap com datas para todas as fatias.** Quanto mais massa, mais energia para mudar de direção.
- **Não medir.** Fatia sem sinal de uso é só entrega.
