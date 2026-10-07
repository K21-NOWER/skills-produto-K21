# Rubrica de avaliação de planos UDD

Use este arquivo para pontuar. Escolha a faixa pelos sinais que o plano realmente mostra e, dentro dela, ajuste pela quantidade de sinais. Se não há texto que sustente uma nota, ela não sobe.

| Critério (peso) | 90-100 | 70-89 | 40-69 | 0-39 |
|---|---|---|---|---|
| **1. Hipótese e direção (16)** Cada fatia nasce de uma hipótese? | Propósito, problema e hipótese claros; toda fatia diz o que quer aprender | Direção clara; hipótese só na primeira fatia | Direção implícita; fatias nascem de "features desejadas" | Sem direção; lista de funcionalidades |
| **2. Epicentro (14)** Começa pelo que mais importa? | A primeira fatia é a parte mais importante do problema mais importante do usuário mais importante, com justificativa | Primeira fatia boa, sem justificar a escolha | Primeira fatia é a mais fácil ou a mais óbvia | Começa por infraestrutura, cadastro ou "base" |
| **3. Fatia vertical (14)** São fatias e não camadas? | Todas atravessam o produto e podem ser usadas e demonstradas sozinhas | Maioria vertical, uma ou duas por camada | Mistura de fatias e camadas ("API", "banco", "tela") | Fatiado por camada ou por etapa de processo |
| **4. Sinal de uso definido antes (16)** Mede comportamento? | Cada fatia tem comportamento esperado, critério numérico e limite de tempo, definidos antes | Sinal e critério na maioria das fatias | Métricas vagas, de vaidade ou de opinião ("gostaram") | Nenhuma métrica ou "mede depois" |
| **5. Ciclo curto até o uso real (12)** Chega rápido ao usuário real? | A primeira fatia entra em uso real em dias ou poucas semanas, mesmo com poucas pessoas | Primeiras semanas, mas com etapas de aprovação | Meses até o primeiro uso | Só "lança quando estiver pronto" |
| **6. Progressão 1-2-N (8)** Do simples ao geral? | Caso básico, variação significativa e generalização, em passos explícitos | Progressão implícita | Salta direto para o caso geral | Tudo ao mesmo tempo |
| **7. Descarte explícito (10)** Diz o que não faz? | Lista do que ficou de fora, com motivo, e itens que podem nunca ser feitos | Lista de adiados, sem descarte | Descarte citado só em tese | Nada fica de fora |
| **8. Regra de expansão (10)** Só cresce com prova? | Cada próxima fatia depende de um resultado da anterior, explícito | Regra geral, sem critério por fatia | Segue o calendário, com revisão eventual | Roadmap fixo, independente do uso |

## Referências de calibração

- "Módulo de cadastro completo, depois agenda completa, depois app mobile": fatia vertical 25, epicentro 25, regra de expansão 10.
- "Lembrete por WhatsApp para 2 clínicas por 5 semanas, expande se as faltas caírem 6 pontos": epicentro 85, sinal de uso 85, regra de expansão 90.
- "MVP" com 12 funcionalidades: epicentro 20 e descarte 15.

## Sinais de alerta

- "MVP" que tem tudo.
- Nenhuma fatia pode ser colocada em uso sozinha.
- Datas fixas de lançamento para todas as fatias, definidas no início.
- O plano só fala de construir, nunca de medir.
