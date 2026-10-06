# Exemplo completo: previsão e avaliação de uma promessa

Exemplo fictício, num app de agendamento para clínicas pequenas. Os números vêm de `scripts/prever.py` com semente 42.

Pedido do usuário: "O diretor quer que o MVP fique pronto em 15 de dezembro. O MVP tem 30 itens e nosso histórico das últimas 8 semanas é 3, 2, 5, 4, 3, 2, 4, 3 itens entregues por semana. Começamos em 12 de outubro. Dá para prometer?"

---

## Previsão: MVP do app de agendamento

**Dados usados:** 30 itens, 8 semanas de histórico, início em 12/10/2026, 10.000 simulações.

### Resposta

| Probabilidade | Termina em até | Data |
|---|---|---|
| 50% | 10 semanas | 21/12/2026 |
| 70% | 10 semanas | 21/12/2026 |
| 85% | 11 semanas | 28/12/2026 |
| 95% | 11 semanas | 28/12/2026 |

**Frase para o diretor:** "Com 85% de probabilidade, os 30 itens terminam em até 28 de dezembro; 15 de dezembro está abaixo da mediana (21/12), então hoje a chance de cumprir é menor que 50%."

Para saber o que cabe até 15 de dezembro (9 semanas), no mesmo ritmo, a simulação `prever.py quanto --semanas 9` mostra: com 85% de confiança saem pelo menos 26 itens, e a mediana é 29. Ou seja, na mediana falta 1 item para os 30 e, com 85% de confiança, faltam 4: dá para propor cortar os 4 de menor valor e prometer 15 de dezembro com folga razoável.

### Como ler

A mediana (10 semanas) é o resultado "do meio", e o percentil 85 (11 semanas) é o seguro. A diferença entre os dois é pequena porque o histórico é estável.

### Premissas e riscos

- Escopo fixo em 30 itens: se chegarem itens novos, a previsão piora; simule de novo a cada semana.
- Mesma equipe e mesmo ritmo, sem férias ou feriados fora do padrão (as semanas de fim de ano costumam entregar menos).
- Amostra de 8 semanas: no limite do aceitável. Cada semana nova de histórico melhora a previsão.

### Perguntas melhores que "quando fica pronto?"

- Quando a primeira versão (fatia 1) pode entrar em uso com 2 clínicas?
- Qual é o ponto mais cedo em que podemos parar, com as faltas já reduzidas?
- Dá para cortar os itens de menor valor para caber em 15 de dezembro?

---

## Avaliação da promessa original: "MVP em 15 de dezembro"

**Nota geral: 25/100** (faixa: Reescrever)

| Critério (peso) | Nota | Por quê |
|---|---|---|
| Intervalo probabilístico (20) | 15 | Data única, sem probabilidade |
| Base em dados históricos (20) | 30 | A data veio do desejo do diretor, não do histórico |
| Amostra (14) | 25 | Não cita dados |
| Premissas explícitas (14) | 20 | Nenhuma premissa sobre escopo ou capacidade |
| Revisão e sensibilidade (10) | 25 | Nada diz como será atualizada |
| Pergunta certa (12) | 40 | Pergunta só "quando termina tudo" |
| Comunicação (10) | 20 | Esconde a incerteza |

Cálculo: (15x20 + 30x20 + 25x14 + 20x14 + 25x10 + 40x12 + 20x10) ÷ 100 = 24,6, arredondado para 25.

A versão reescrita é a previsão acima.
