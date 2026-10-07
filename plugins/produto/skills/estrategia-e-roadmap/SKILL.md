---
name: estrategia-e-roadmap
description: Constrói e avalia a estratégia e o roadmap de um produto com as ferramentas da K21: Tanque de Decantação (propósito, problema, métricas, ideias, foco e CCC), Matriz de Estratégia de Produto (o tripé de performance do negócio, mercado e propósito do cliente com Fit for Purpose), Bússola Estratégica, Radar do Produto e roadmap enxuto por objetivos, métricas, desafios e hipóteses. Avalia estratégia e roadmap com nota de 0 a 100 por critério. Use sempre que o usuário falar de estratégia de produto, roadmap, Tanque de Decantação, Matriz de Estratégia, Bússola Estratégica, Radar do Produto, propósito do cliente, Fit for Purpose, "o que vamos construir este ano?", roadmap de features e datas, alinhar produto com objetivos de negócio, ou colar um roadmap para revisar, mesmo sem citar essas ferramentas.
---

# Estratégia e roadmap: do propósito ao foco, sem planejar demais

Estratégia de produto liga o propósito do negócio ao propósito do cliente, escolhe um foco e o mede. Roadmap é a forma de comunicar esse caminho, e o roadmap tradicional (uma lista de funcionalidades com datas) cria a ilusão do superplanejamento: dá falsa sensação de segurança, aumenta a rigidez e leva a construir coisas demais que ninguém usa. Quanto mais massa tem um objeto, mais energia é preciso para mudar sua direção, e isso vale para produtos. "Planejamento é saber que você precisa mudar a rota a cada 30 minutos" (Amyr Klink).

Esta skill cria e avalia estratégia e roadmap, escolhendo a ferramenta certa para a situação, com a mesma régua de 0 a 100 das outras skills.

## Escolha a ferramenta

| Situação | Ferramenta | Detalhes |
|---|---|---|
| Não sei o que construir nem em que ordem; falta ligar o trabalho ao objetivo de negócio | **Tanque de Decantação** | `references/ferramentas.md` |
| Preciso escolher a aposta estratégica do produto, olhando negócio, mercado e cliente | **Matriz de Estratégia de Produto** | idem |
| Quero saber onde e como evoluir o produto (mercado, deficiências, sinergias, oportunidades) | **Bússola Estratégica** | idem |
| Quero medir, com o time e as personas, o quanto já avançamos nos objetivos | **Radar do Produto** | idem |
| Preciso comunicar o caminho sem engessar | **Roadmap enxuto** | idem |

Se o usuário não souber qual, comece pelo Tanque: ele conecta propósito, problema, métricas e ideias, e abastece as outras.

## Escolha o modo

- **Criar**: o usuário traz um produto, ideia ou contexto e quer a estratégia ou o roadmap. Preencha a ferramenta escolhida.
- **Avaliar**: traz uma estratégia, canvas ou roadmap e quer a nota. Veja abaixo.
- **Avaliar e melhorar**: traz um roadmap de features e quer a versão por resultados.

Responda no idioma do usuário (padrão: português do Brasil), com tom de mentor. Se faltar informação, declare suposições em vez de interrogar.

## Modo criar

1. Escolha a ferramenta (ou combine: Tanque, depois Radar e roadmap).
2. Preencha-a seguindo `references/ferramentas.md`, mantendo as **relações entre os campos** (problema leva a propósitos, ideias afetam métricas).
3. Termine com um **foco**: a única primeira aposta, com a métrica que a testa. Se for ideia, transforme em hipótese (`hipoteses`) e em história (`user-story`).
4. **Roadmap enxuto**: escolha o menor ciclo possível; para cada ciclo, objetivos, métricas, desafios e hipóteses. Evite datas de funcionalidades distantes.
5. Autoavalie com a rubrica e reescreva o que ficar abaixo de 80.

### Formato de saída (criar)

```
## [Ferramenta]: [produto ou contexto]

**Suposições:** ...

(a ferramenta preenchida, em tabela ou lista, com as relações entre os campos)

### Foco e primeira aposta
### Próximos passos
### Qualidade (autoavaliação): NN/100
```

## Modo avaliar

1. Leia `references/rubrica.md`.
2. Pontue os 8 critérios de 0 a 100, citando trechos.
3. Nota geral = soma de (nota x peso) dividida por 100. **Teto de bloqueio:** se qualquer critério ficar abaixo de 40, a nota geral não passa de 69.
4. Faixas: 85 a 100 Pronto para guiar o time; 70 a 84 Quase lá; 50 a 69 Precisa de refinamento; 0 a 49 Reescrever.

| # | Critério | Peso |
|---|---|---|
| 1 | Propósito | 12 |
| 2 | Problema | 14 |
| 3 | Métricas | 14 |
| 4 | Causalidade entre ideias e métricas | 12 |
| 5 | Foco | 10 |
| 6 | Roadmap como hipóteses e resultados | 14 |
| 7 | Flexibilidade (baixo custo de mudança) | 10 |
| 8 | Conexão com cliente e mercado | 14 |

Formato de saída: nota no topo, tabela por critério com evidência, o que mais pesa, **versão reescrita** (por exemplo, o Tanque preenchido ou o roadmap por ciclos) e suposições. Calibre com rigor: estratégias e roadmaps comuns ficam entre 20 e 60.

## Princípios

- **Propósito antes de ideia.** Se o propósito é "modernizar o sistema X", pergunte que necessidade de negócio está por trás.
- **Problema na ótica do negócio e das pessoas,** nunca técnico.
- **Sem métrica, é "eu acho que".** A priorização do produto vira discussão interminável.
- **Todas as ideias valem, desde que haja causalidade entre cada ideia e a métrica que ela altera.**
- **Roadmap por resultado.** Visibilidade, adaptação e previsibilidade com possibilidade de mudar de direção, e não um compromisso de entregar tudo o que foi planejado.
- **Cliente no centro, de verdade.** Segmentar por renda ou perfil não garante centralidade: mapeie os **propósitos** do cliente.

Para as métricas, use `metricas-de-produto`; para os objetivos do ciclo, `okr`; para testar as ideias, `hipoteses`; para fatiar o foco, `udd-fatiamento`; para a visão, `visao-do-produto`. Para ver uma avaliação completa, leia `references/exemplo.md`.
