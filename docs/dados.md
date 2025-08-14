# Sistema Adaptado de Rolagem de Dados

## Motivação

O sistema atual tenta mesclar dois métodos distintos de rolagem de dados em RPG:

1. **Dice pool** – rolar vários dados e contar sucessos/escolher o resultado.
2. **D20 clássico** – rolar 1d20, somar atributos e tentar bater uma DT/CD.

Esse híbrido gera situações incoerentes, como:

* Um agente um pouco **acima da média** (2 pontos de atributo), com apenas um **treinamento básico** (+5 de bônus) em uma perícia, tem **o dobro** (51% x 26%) de chances de passar em um teste **"muito difícil"** (DT 20) que **"indivíduos extraordinários — um medalhista olímpico ou vencedor do Nobel"** (4-5 pontos) com alguma **maldição que aumente um atributo** (muito raro e difícil de se conseguir) em 1 ponto (6 pontos totais; se 4-5 é um prêmio Nobel, o que seriam 6?).
* Nessa perspectiva, qual a motivação de se tornar "extraordinário" em alguma coisa, quando essa especialidade não se traduz dentro do jogo? Quando acumular bônus (vestimentas, utensílios, treinamentos, poderes...) valem muito mais a pena?

---

## Nova Mecânica de Rolagem

### Alteração principal

* **Antes:**
  Rola-se 1d20 para cada ponto de atributo, escolhe-se o maior resultado, soma-se os bônus e compara-se com a DT.

* **Agora:**
  Rola-se 1d20 para cada ponto de atributo e **conta-se o número de sucessos**, ou seja, dados cujo valor seja igual ou superior a uma DT ajustada pelo bônus do personagem.

---

## Bônus

Os bônus serão reescalonados:

| Antigo | Novo | Efeito na DT |
| ------ | ---- | ------------ |
| +2     | +1   | -1 na DT     |
| +5     | +2   | -2 na DT     |
| +10    | +4   | -4 na DT     |
| +15    | +6   | -6 na DT     |

*Obs.: para modificadores negativos (-2, -5...) segue-se a mesma lógica númerica, apenas alternando o sinal.*

---

## Resultados por Dado

Ao rolar cada dado individualmente, temos 4 possíveis resultados:

* **Falha Crítica:**
  Resultado **1** → `-1 sucesso`
* **Falha:**
  Resultado **entre 2 e (DT - 1)** → `0 sucessos`
* **Sucesso:**
  Resultado **entre DT e 19** → `+1 sucesso`
* **Sucesso Crítico:**
  Resultado **20** → `+2 sucessos`

---

## Vantagem e Desvantagem

* Funcionam da mesma forma que no sistema base: cada vantagem fornece **+1d20** e cada desvantagem fornece **-1d20**.

*Obs.: no caso de 0d20, -1d20, -2d20..., rolam-se 2, 3, 4... d20s e conta-se apenas o pior resultado.*

---

## Ajuda entre Agentes

Ações em conjunto, no sistema atual, é quase inútil. Somar o resultado / 10 de bônus, na maioria dos casos, vai resultar em um +2. Quando comparamos que um grau de treinamento é +5, uma vestimenta já é +2, uma vestimenta aprimorada é +5, é mais produtivo cada um dos agentes realizar um teste separado com seus respectivos bônus acumulados do que tentar realizar alguma ação em conjunto.

No novo sistema, quando agentes realizam ações em conjunto, para cada agente ajudando:

1. **Diminua a DT em 2, caso o agente seja treinado/conheça o ritual, ou em 1, caso contrário**.
2. **Aumente o número de sucessos necessários em 1**

Exemplo:

* 1 agente solo treinado: DT 18, objetivo de 1 sucesso, com 2–3 dados → **26% a 36% de chance de sucesso**.
* 3 agentes juntos, 2 treinados e 1 não: DT 15, objetivo de 3 sucessos, 3 agentes com 2–3 dados → **31% a 52% de chance**.

Isso é coerente, pois:

* Em média, um grupo tem 5–6 agentes, e se metade ou mais for especializada (múltiplos pontos), a chance de sucesso deve subir.
* Não há o risco de acumular agentes no mesmo teste pois em cenas de investigação ou ações complexas, há múltiplos pontos de interesse, então nem todos estarão focados na mesma tarefa.

Não é considerado bônus dos personagens no cálculo da DT de referência para um teste pois personagens especializados devem, sim, ter mais chances de passar do que personagens não especializados. Isso recompensa os personagens, mas de uma forma equilibrada, a procurar treinamentos ou outras formas de bônus, pois possuem mais chances do que um agente que só irá rolar os dados, sem somar nada.

O ponto todo é o equilíbrio. Um bônus simples, de +1 ou +2, não desequilibra completamente as probabilidades de sucesso, como acontece no sistema atual, em que um **treinamento básico** para um **agente um pouco acima da média** se traduz em **mais de 40%** de aumento na chance de passar em testes **muito difíceis** (9,75% -> 51%).
