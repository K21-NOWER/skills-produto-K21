# Como escrever critérios de aceitação

Conteúdo: Para que servem · Formato · Regras de ouro · Checklist de cobertura · Antes e depois · Quantidade · Armadilhas · Exemplo completo

## Para que servem

Critérios de aceitação são o contrato de "pronto" entre quem pede e quem constrói. Eles respondem: "se isso for verdade, a story está entregue?". Um bom critério dispensa discussão na hora da validação, porque qualquer pessoa chega à mesma resposta (sim ou não).

Eles não respondem se a ideia funcionou para o usuário. Isso é o **sinal de sucesso** (uma métrica ou um comportamento esperado depois do uso). Não misture: critério de aceitação diz "construímos certo"; sinal de sucesso diz "construímos a coisa certa".

## Formato

**Dado/Quando/Então** (estilo Gherkin, bom para comportamentos com fluxo):

```
Cenário: [nome curto do comportamento]
  Dado que [contexto ou estado inicial]
  Quando [ação do usuário ou evento]
  Então [resultado observável]
  E [mais um resultado, se houver]
```

Palavras úteis: "E" para somar passos do mesmo tipo, "Mas" para exceção dentro do cenário.

**Lista de regras** (bom para validações e regras de negócio):

```
Regras
- A nova senha tem no mínimo 8 caracteres.
- O link vale por 30 minutos e só pode ser usado uma vez.
```

Combine os dois: cenários para o que acontece, regras para as condições que valem sempre.

## Regras de ouro

1. **Verificável.** A resposta é sim ou não. "Aparece a mensagem 'Presença confirmada'" é verificável; "o fluxo é intuitivo" não é.
2. **Específico, com valores concretos.** Troque adjetivos por números e exemplos: "em até 2 segundos", "no mínimo 8 caracteres", "até 5 tentativas".
3. **Declarativo, não passo a passo de tela.** Descreva o comportamento, não o clique. "Quando confirmo minha presença" em vez de "quando clico no botão verde no canto superior direito". Os passos de tela mudam, o comportamento não.
4. **Uma regra por critério.** Se tiver "e" ligando comportamentos independentes, quebre em dois.
5. **Linguagem do usuário e do negócio**, sem nome de tabela, endpoint ou componente.
6. **Sem contradição e sem repetição** entre critérios e com a própria story.
7. **Inclua o que não vai ser feito** quando houver risco de expectativa ("Fora do escopo: remarcação").

## Checklist de cobertura

Passe por esta lista e inclua o que for relevante para a story (nem tudo se aplica sempre):

- Caminho feliz (o que acontece quando tudo dá certo).
- Caminhos alternativos (outra forma legítima de chegar ao resultado).
- Erros e validações (dado inválido, falha de rede, sem permissão).
- Limites (mínimo, máximo, vazio, repetido, tamanho do texto).
- Permissões (quem pode e quem não pode; o que quem não pode vê).
- Estados da tela ou do dado (vazio, carregando, expirado, já usado).
- Segurança e privacidade quando a story mexe em dados pessoais (por exemplo, não revelar se um e-mail está cadastrado).
- Não funcionais que importam para o usuário e são testáveis ("a lista carrega em até 2 segundos com 1.000 itens").

## Antes e depois

| Ruim | Por quê | Melhor |
|---|---|---|
| "O sistema deve ser rápido" | Adjetivo, não dá para verificar | "A lista de consultas aparece em até 2 segundos com até 500 registros" |
| "O usuário clica em Salvar e vê uma mensagem" | Passo de tela; qual mensagem? | "Ao salvar, vejo a mensagem 'Dados salvos' e os dados aparecem atualizados na lista" |
| "Validar os campos" | Quais campos? Qual regra? | "Se o e-mail não tem '@', vejo 'Informe um e-mail válido' e nada é salvo" |
| "Funcionar em celular" | Quais celulares? Qual comportamento? | "A tela funciona em telas de 360 pixels de largura sem rolagem horizontal" |
| "Criar a tabela de pedidos" | Tarefa técnica, não comportamento | "Quando faço um pedido, ele aparece na minha lista de pedidos com status 'Recebido'" |
| "Tratar erros" | Quais erros? Tratar como? | "Se a conexão cair ao enviar, vejo 'Não foi possível enviar. Tente de novo' e meus dados continuam preenchidos" |

## Quantidade

Em geral, de 3 a 7 critérios por story. Menos de 3 costuma indicar que faltam erros e limites. Mais de 7 costuma indicar que a story é grande demais ou que os critérios estão descrevendo funcionalidades distintas: é sinal para fatiar, não para escrever critério mais curto.

## Armadilhas

- **Escrever a solução como critério** ("usar um dropdown de 3 opções").
- **Copiar a story como critério** ("o usuário consegue confirmar presença"). Isso repete o "quero" sem dizer como verificar.
- **Só o caminho feliz.** A maior parte dos defeitos mora nos erros e nos limites.
- **Critério que depende de interpretação** ("mensagem amigável").
- **Misturar regra de negócio com layout** no mesmo critério.

## Exemplo completo

**História:** Como cliente que esqueceu a senha, quero redefinir minha senha por e-mail, para voltar a acessar minha conta sem precisar falar com o suporte.

**Critérios de aceitação**

- **Cenário: pedido de redefinição com e-mail cadastrado**
  - Dado que tenho uma conta com o e-mail ana@exemplo.com
  - Quando peço a redefinição informando esse e-mail
  - Então vejo a mensagem "Se o e-mail estiver cadastrado, você receberá as instruções"
  - E recebo um e-mail com um link de redefinição em até 1 minuto
- **Cenário: e-mail não cadastrado**
  - Dado que o e-mail joao@exemplo.com não tem conta
  - Quando peço a redefinição com esse e-mail
  - Então vejo a mesma mensagem do cenário anterior
  - E nenhum e-mail é enviado
- **Cenário: link expirado ou já usado**
  - Dado que o link tem mais de 30 minutos ou já foi usado
  - Quando abro o link
  - Então vejo "Este link não é mais válido" e a opção de pedir um novo
- **Cenário: nova senha válida**
  - Dado que abri um link válido
  - Quando informo uma nova senha que atende às regras
  - Então minha senha é alterada, o link deixa de funcionar e consigo entrar com a nova senha
- **Regras:** a nova senha tem no mínimo 8 caracteres e é diferente das últimas 3 senhas usadas; o link vale por 30 minutos e só pode ser usado uma vez.

**Fora do escopo:** redefinição por SMS; bloqueio de conta por excesso de tentativas.
**Sinal de sucesso:** queda dos chamados ao suporte do tipo "esqueci minha senha" [meta a definir com o negócio].

Repare no segundo cenário: a mesma mensagem para e-mail cadastrado e não cadastrado evita revelar quais e-mails existem na base. Esse tipo de critério só aparece quando alguém pensa no que pode dar errado, e é por isso que erros e limites pesam tanto na nota.
