# Como fatiar user stories

Conteúdo: Por que fatiar · Fatia vertical e horizontal · Como decidir se precisa fatiar · Os 9 padrões de fatiamento · Processo em 5 passos · Armadilhas · Exemplo

## Por que fatiar

Story pequena entrega mais cedo, recebe feedback mais cedo, erra mais barato e deixa o plano mais previsível. Fatiar também revela o que não precisa ser feito: ao quebrar uma ideia grande, quase sempre aparecem fatias que ninguém sentiria falta. Fatiar, descartar e priorizar são o mesmo movimento: reduzir o problema até sobrar o que realmente gera valor.

## Fatia vertical e horizontal

- **Vertical (o que queremos):** uma fatia fina que atravessa todas as camadas (tela, regra, dados) e entrega algo que o usuário consegue usar ou que dá para demonstrar. Exemplo: "confirmar presença na consulta com um toque".
- **Horizontal (o que evitar):** uma fatia por camada técnica. Exemplo: "criar tabela de confirmações", "criar API de confirmação", "criar tela de confirmação". Nenhuma entrega valor sozinha, o feedback só chega no fim e o risco fica escondido até a integração.

## Como decidir se precisa fatiar

Uma story precisa de fatiamento quando alguma destas perguntas tem resposta "sim":

- O time levaria mais da metade de uma sprint para entregar?
- Há mais de uma coisa que poderia ser entregue e usada separadamente?
- Os critérios de aceitação passam de 7, ou descrevem comportamentos diferentes?
- Há palavras como gerenciar, administrar, "sistema de", CRUD, "etc."?
- Há mais de um perfil de usuário ou mais de uma regra de negócio por variação (tipo de cliente, forma de pagamento)?

## Os 9 padrões de fatiamento

Os nove padrões abaixo seguem a coleção de Richard Lawrence (Humanizing Work). Tente na ordem e fique com a fatia que gera partes de tamanho parecido e que entregam valor sozinhas.

1. **Passos do fluxo.** Entregue o fluxo de ponta a ponta no mínimo, depois enriqueça os passos. "Publicar um produto" vira: publicar com nome e preço; depois adicionar fotos; depois agendar publicação.
2. **Operações (CRUD).** "Gerenciar" esconde várias operações. Separe criar, ver, editar, excluir, e muitas vezes só uma ou duas são realmente necessárias agora.
3. **Variações de regra de negócio.** Cada regra diferente vira uma fatia. "Pagar com cartão" vira: débito; crédito à vista; crédito parcelado.
4. **Variações de dados.** Comece com um tipo de dado e acrescente os outros. "Buscar por categoria" vira: uma categoria; depois subcategorias; depois várias ao mesmo tempo.
5. **Formas de entrada de dados.** Comece pelo jeito mais simples. "Informar endereço" vira: digitando; depois por CEP; depois pela localização do aparelho.
6. **Esforço maior primeiro.** Quando uma variação concentra quase todo o trabalho (por exemplo, a integração) e as outras são baratas, coloque o esforço pesado na primeira fatia e as demais viram acréscimos pequenos.
7. **Simples e complexo.** Pergunte "qual é a versão mais simples que já serve?". Entregue-a e transforme cada complexidade em fatia própria.
8. **Adiar desempenho.** "Funciona" primeiro, "funciona rápido" depois, quando o desempenho puder realmente esperar e o risco estiver controlado.
9. **Spike.** Quando a incerteza (técnica ou de negócio) é o maior obstáculo, faça uma investigação com limite de tempo e uma pergunta clara. O resultado é aprendizado, e a partir dele você fatia melhor.

**Atalho de memória (SPIDR, de Mike Cohn):** Spike, Paths (caminhos), Interfaces, Data (dados), Rules (regras).

## Processo em 5 passos

1. **Confirme que a story é boa em tudo, menos no tamanho.** Persona, valor e clareza precisam existir; fatiar uma story ruim só multiplica o problema.
2. **Ache o núcleo.** Qual é o coração do valor? Qual é o fluxo principal, sem variações?
3. **Aplique os padrões** e liste as fatias candidatas. Se o primeiro padrão não gerar boas fatias, tente o seguinte.
4. **Escolha a fatiação.** Prefira a que: gera fatias parecidas em tamanho; cada fatia entrega valor ou aprendizado sozinha; permite descartar partes (quais fatias, se nunca fossem feitas, ninguém sentiria falta?).
5. **Ordene.** A primeira fatia é a mais fina que ainda atravessa o sistema de ponta a ponta e ensina algo (o "esqueleto andante"). As demais seguem por valor e risco.

Depois de fatiar, passe cada fatia pela rubrica: ainda é demonstrável sozinha? Entrega valor? Tem critérios de aceitação próprios?

## Armadilhas

- **Fatiar por camada técnica** (banco, API, tela).
- **Fatias de processo**: "preparar", "testar", "documentar" como stories separadas. Teste e documentação fazem parte de cada fatia.
- **Fatias que não dá para demonstrar.** Se não dá para mostrar a alguém, não é fatia, é tarefa.
- **Fatiar demais**: fatias tão pequenas que o custo de coordenar supera o ganho. Pare quando cada fatia couber em poucos dias e entregar algo observável.
- **Guardar tudo "para depois".** O que ninguém sentiria falta, descarte em vez de deixar apodrecendo no backlog.

## Exemplo

Story grande: "Como paciente, quero gerenciar meus agendamentos."

Padrão usado: operações (CRUD) combinado com passos do fluxo. Fatias, em ordem:

1. Confirmar presença em uma consulta marcada, com um toque. (Fatia mais fina que atravessa o sistema e já ajuda a clínica.)
2. Ver minhas próximas consultas.
3. Cancelar uma consulta, liberando o horário.
4. Remarcar para outro horário disponível.
5. Ver o histórico de consultas passadas. (Candidata a descarte até o uso mostrar que alguém precisa.)

A ordem prioriza o que gera valor e aprendizado primeiro. A fatia 4 é a que mais concentra regra de negócio (disponibilidade, prazo mínimo, limites), então vem depois que o básico estiver rodando.
