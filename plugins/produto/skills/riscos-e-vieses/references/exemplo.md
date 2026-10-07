# Exemplo completo: pré-mortem de uma decisão

Exemplo fictício, num app de agendamento para clínicas pequenas.

Pedido do usuário: "A diretoria decidiu que vamos construir o app mobile em 6 meses, com 4 pessoas. Todos estão empolgados e a análise SWOT deu 8 forças e 7 oportunidades, com 2 fraquezas e 1 ameaça. Pode desafiar essa decisão?"

---

## Pré-mortem: app mobile em 6 meses

**Robustez: 23/100** (faixa: Não invista ainda)

### 1. Notas por critério

| Critério (peso) | Nota | Por quê (evidência) | Como melhorar |
|---|---|---|---|
| Evidência (18) | 25 | A justificativa é a empolgação e a SWOT; nenhum dado de uso ou de mercado | Levar dados de uso e de clientes |
| Alternativas e invalidação (14) | 20 | Nenhuma alternativa foi considerada (por exemplo, melhorar o canal web ou lembretes) | Listar alternativas e tentar invalidar o app |
| Critério de sucesso antes (12) | 20 | Não há métrica nem prazo de avaliação, só "lançar em 6 meses" | Definir sucesso e regra de parada |
| Riscos mapeados e quantificados (14) | 25 | SWOT com 2 fraquezas e 1 ameaça: lista de riscos quase vazia | Mapear riscos com probabilidade e impacto |
| As 4 perguntas de risco (14) | 20 | Não se sabe se o problema existe, se o app o resolve, quanto retorna nem o custo técnico | Rodar a Matriz de Hipóteses |
| Dependências (8) | 30 | Lojas de aplicativos, integração com agendas existentes: não citadas | Mapear |
| Reversibilidade (10) | 15 | 6 meses e 4 pessoas antes de qualquer uso real | Piloto em semanas |
| Diversidade e vieses (10) | 30 | Decisão da diretoria; sem clientes nem céticos | Ouvir clínicas e quem duvida |

Cálculo: (25x18 + 20x14 + 20x12 + 25x14 + 20x14 + 30x8 + 15x10 + 30x10) ÷ 100 = 22,9, arredondado para 23.

### 2. Vieses em jogo

| Viés | Sinal no texto | Antídoto |
|---|---|---|
| Otimismo | "Todos estão empolgados"; SWOT com 8 forças e 2 fraquezas | Métricas antes de começar e um experimento que possa invalidar a ideia |
| HiPPO | "A diretoria decidiu" | Levar dados que permitam à diretoria decidir com fatos |
| Viés da solução | O "app" já é a solução; o problema não aparece | Voltar ao problema: o que o app resolve que a web não resolve? |
| Sobrevivência | Nenhuma menção a produtos parecidos que fracassaram | Pesquisar o que não deu certo |

### 3. Riscos

| Risco (evento) | Domínio | Probabilidade | Impacto | Mitigação |
|---|---|---|---|---|
| Os pacientes não instalam o app | Negócio | Alta | Alto | Testar o canal mais simples (WhatsApp) antes |
| Não saber se o app reduz faltas | Negócio | Média | Alto | Piloto com critério numérico |
| Dependência das lojas de aplicativos e de atualizações | Técnico | Média | Médio | Versão web progressiva como primeira fatia |
| Time de 4 pessoas parado por 6 meses sem aprendizado | Organizacional | Média | Alto | Ciclos de 6 semanas, com revisão |

### 4. As 4 perguntas

| Pergunta | Hipótese | Como saberemos |
|---|---|---|
| O problema existe? | As faltas são esquecimento | [40%] de 20 ligações citam esquecimento |
| A solução resolve? | O app (ou um lembrete simples) reduz as faltas | Piloto com lembrete por WhatsApp: [6] pontos a menos que o controle |
| É economicamente viável? | Cada falta custa [R$ 120] | O retorno anual por clínica precisa superar o custo de construir e manter |
| É tecnicamente viável? | Dá para fazer sem app | Integração com a agenda atual em [2 semanas] |

### 5. Experimento mais barato e decisão

**Experimento:** piloto de lembrete manual por WhatsApp em 2 clínicas por 7 semanas, com grupo de controle. **Critério:** queda de pelo menos 6 pontos percentuais na taxa de faltas. **Regra:** se atingir, a primeira fatia do produto é o lembrete (e só depois se discute o app); se não atingir, ajustar a causa ou enterrar a ideia do app com uma festa, porque poupamos seis meses de quatro pessoas.

### 6. Perguntas e suposições

- Assumi que não há dados de uso do canal web. Se houver, a nota de evidência pode subir.
- Os números entre colchetes são suposições minhas.
