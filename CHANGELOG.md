# Histórico de versões

## v1.2.1

- **Correções encontradas na bateria de testes das 14 skills:** `analisar_backlog.py` reconhece a coluna `Points`; `prever.py` usa vírgula decimal e o singular correto; a rubrica da `user-story` reconhece canal escolhido sem necessidade ("receber um e-mail") e "para tomada de decisão" como propósito vago; `papel-de-produto` aciona também para pedidos em primeira pessoa; cinco skills ganharam a regra "sem dado, sem número"; os exemplos de estratégia e UDD seguem o formato de saída.
- **Testes automáticos no repositório:** `python3 scripts/testar.py` roda os testes dos scripts, da estrutura, do acionamento e do empacotamento, e o GitHub roda o mesmo a cada pull request.
- **Repositório:** guia de contribuição, código de conduta, modelos de issue e de pull request.

## v1.2.0

- 10 skills novas, baseadas na metodologia da K21: `metricas-de-produto`, `udd-fatiamento`, `okr`, `saude-do-backlog`, `previsibilidade`, `papel-de-produto`, `discovery-com-clientes`, `estrategia-e-roadmap`, `apresentacao-de-produto` e `riscos-e-vieses`.
- Ajustes nas 4 originais: Test Card 2.0 e Learning Card (`hipoteses`), Matriz RUT (`priorizacao`), saúde da história em 9 passos (`user-story`) e Tanque de Decantação (`visao-do-produto`).
- Pacote único com 14 modos; scripts de contas de priorização, análise de backlog em CSV e previsão por Monte Carlo.

## v1.1.0

- Instalação em um passo pelo marketplace do Claude, plugin em `.zip` e pacote único.

## v1.0.0

- Primeira versão, com 4 skills: `user-story`, `visao-do-produto`, `priorizacao` e `hipoteses`.
