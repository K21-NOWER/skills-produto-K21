# Como contribuir

Obrigado por querer melhorar estas skills. Os caminhos mais simples:

- **Achou uma nota estranha ou uma explicação confusa?** Abra uma [issue](../../issues/new/choose) com o pedido que você fez e o que estranhou.
- **Tem uma ideia de skill nova?** Abra uma issue de sugestão, dizendo que problema ela resolve e em que conteúdo se apoia.
- **Quer corrigir ou escrever você mesmo?** Abra um pull request.

## Antes de abrir um pull request

1. Rode `python3 scripts/testar.py` na raiz. Ele roda os testes dos scripts, confere a estrutura das skills e valida o empacotamento. O GitHub roda o mesmo teste no PR.
2. Escreva em português do Brasil, sem travessão (longo ou curto) e sem hífen duplo no lugar dele.
3. Siga o padrão das skills existentes: `SKILL.md` com até 500 linhas e descrição de até 1024 caracteres; rubrica com notas de 0 a 100, pesos que somam 100 e faixas ancoradas; um `exemplo.md` que segue o "Formato de saída" da própria skill; números sempre marcados como dado ou suposição.
4. Skill nova: crie a pasta em `plugins/produto/skills/`, inclua-a no roteador `pacote-unico/SKILL.md` (o empacotador confere) e na tabela do README.

A estrutura do repositório e o fluxo de publicação estão no [README](README.md#para-quem-mantém-o-repositório).
