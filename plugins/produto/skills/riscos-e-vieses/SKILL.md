---
name: riscos-e-vieses
description: Faz um pré-mortem de decisões e iniciativas de produto: avalia a robustez com nota de 0 a 100 por critério, detecta vieses cognitivos (otimismo, pessimismo, confirmação, sobrevivência, paradoxo da escolha, HiPPO, achismo), mapeia riscos (evento, probabilidade e impacto) nos 4 domínios da agilidade e roda a Matriz de Hipóteses (o problema existe? a solução resolve? é economicamente viável? é tecnicamente viável?), além de dependências e plano de mitigação com experimento barato. Use sempre que o usuário falar de risco, pré-mortem, viés, achismo, "o chefe mandou fazer", decisão de investimento em produto, "vale a pena construir isso?", matriz de hipóteses, dependências entre times, otimismo de início de projeto, ou colar uma decisão ou plano para ser desafiado, mesmo sem citar esses termos.
---

# Riscos e vieses: desafiar a decisão antes de pagar por ela

Nosso cérebro cria atalhos para reduzir esforço, e não são ruins por si. Mas, para quem cria produtos, é bom perceber quando um viés está agindo, porque ele custa meses de trabalho em algo que ninguém usa. Um dos maiores riscos para uma organização é justamente não correr riscos de forma consciente: acreditar que a ideia brilhante vai funcionar e que só falta executá-la.

Esta skill desafia uma decisão ou iniciativa: o que ela supõe, que vieses a inflam, que riscos carrega e qual é o experimento mais barato para reduzir a incerteza. Mantenha o tom de mentor: não é uma prova que o time precisa gabaritar.

## Escolha o modo

- **Avaliar a decisão (pré-mortem):** o usuário traz uma decisão, plano ou iniciativa. Entregue nota de robustez, vieses, riscos e plano.
- **Matriz de Hipóteses:** quer rodar as 4 perguntas de risco para uma ideia. Veja `references/matriz-e-riscos.md`.
- **Mapear riscos e dependências:** quer a lista de riscos com probabilidade e impacto.
- **Detectar vieses:** quer saber que vieses estão em jogo num argumento ou numa reunião. Veja `references/vieses.md`.

Responda no idioma do usuário (padrão: português do Brasil), com tom acolhedor e direto. Fale de viés como algo humano, nunca acuse pessoas.

## Modo avaliar a decisão

1. Leia `references/rubrica.md`.
2. Pontue os 8 critérios de 0 a 100, citando trechos do plano ou da justificativa.
3. Nota geral = soma de (nota x peso) dividida por 100. **Teto de bloqueio:** se qualquer critério ficar abaixo de 40, a nota geral não passa de 69.
4. Faixas: 85 a 100 Robusta, pode seguir; 70 a 84 Quase lá; 50 a 69 Reduza incertezas antes de investir; 0 a 49 Não invista ainda.

| # | Critério | Peso |
|---|---|---|
| 1 | Evidência (fatos x opinião) | 18 |
| 2 | Alternativas e invalidação | 14 |
| 3 | Critério de sucesso definido antes | 12 |
| 4 | Riscos mapeados e quantificados | 14 |
| 5 | As 4 perguntas de risco | 14 |
| 6 | Dependências | 8 |
| 7 | Reversibilidade e custo de errar | 10 |
| 8 | Diversidade de visões e vieses | 10 |

### O que entregar

```
## Pré-mortem: [decisão ou iniciativa]

**Robustez: NN/100** (faixa)

### 1. Notas por critério
| Critério (peso) | Nota | Por quê (evidência) | Como melhorar |
### 2. Vieses em jogo
| Viés | Sinal no texto | Antídoto |
### 3. Riscos
| Risco (evento) | Domínio | Probabilidade | Impacto | Mitigação |
### 4. As 4 perguntas
| Pergunta | Hipótese | Como saberemos (métrica e critério) |
### 5. Experimento mais barato e decisão
(o menor teste, o critério de sucesso e a regra: seguir, ajustar ou enterrar a ideia)
### 6. Perguntas e suposições
```

Calibre com rigor: decisões comuns, tomadas sem método, ficam entre 20 e 55. Reserve 90 ou mais para uma decisão que você assinaria. Se o usuário pedir só a nota, entregue as seções 1 e 2.

## Como pensar riscos

- **Risco é incerteza** com efeito positivo ou negativo (oportunidade ou ameaça). Aqui, o foco está nos negativos.
- **Todo risco tem três componentes:** o **evento** (o fato gerador), a **probabilidade** e o **impacto**.
- **Classifique pelos 4 domínios da agilidade:** negócio (resultado, aceitação do mercado, feedback, métricas), cultural (como nos relacionamos, segurança para errar), organizacional (como nos organizamos, dependências, aprovações) e técnico (maestria da execução, qualidade, integrações). O domínio de negócio costuma ser o menos acompanhado e o que decide o sucesso.
- **Riscos de negócio mais comuns:** o produto não ser aceito pelo mercado (reduza com invalidação de ideias e MVP, antes dos altos custos), a falta de feedback ("não tem nada pior do que fazer muito bem algo que ninguém quer") e métricas ausentes ou mal definidas. A principal forma de reduzir risco em projetos ágeis são ciclos curtos de entrega: quem demora a entregar aumenta o risco.
- **Sem métricas, é suposição, não certeza.**

## Princípios

- **Invalidar é mais barato que provar.** Teste o que derrubaria a ideia, não o que a confirma.
- **Quanto menor a incerteza, melhores as decisões.** O experimento mais barato que reduz a maior incerteza vem primeiro.
- **Ambiente "safe to error", não "error safe".** Se o time responde "sim" a todas as perguntas da matriz antes de entender, é sinal de que não há segurança para errar.
- **Não ignore os pessimistas** (podem ter informação), mas não entre na marcha da morte com eles.

Para transformar o experimento em Test Card, use `hipoteses`. Para entrevistar clientes, `discovery-com-clientes`. Para as métricas, `metricas-de-produto`. Para priorizar o que sobra, `priorizacao`. Para ver um pré-mortem completo, leia `references/exemplo.md`.
