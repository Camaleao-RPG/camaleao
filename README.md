# Análise de Probabilidades — Comparação entre **Maior d20 + Bônus vs DT** (sistema atual) e **Resolução por Sucessos** (proposta)

Este projeto mede e compara probabilidades entre:

1. **Sistema atual (baseline)** — rola-se uma quantidade de **d20**, escolhe-se o **maior resultado** (ou menor em casos de penalidade), soma-se **bônus** e compara-se com **DT fixa**.
2. **Proposta alternativa** — **resolução por número de sucessos**: cada d20 pode gerar **+2** (crítico), **+1** (sucesso), **0** (falha) ou **−1** (falha crítica) sucessos, e analisamos a probabilidade de atingir **pelo menos `k` sucessos** (e **exatamente `k`**).

O objetivo é tornar a progressão **mais coerente** e evitar casos onde **atributos maiores** ou **mais dados** possam resultar em **menor chance** de sucesso quando comparados a menos dados mas bônus maiores (facilmente acumulados).

---

## Objetivo

- **Medir** o comportamento probabilístico do sistema atual (**Maior d20 + Bônus vs DT**).
- **Comparar** com a proposta baseada em **sucessos**, mostrando como ela é mais **equilibrada** (equilíbrio entre o crescimento da chance de sucesso com o aumento de atributos e o aumento de bônus).
- **Evitar paradoxos**, como personagens excepcionais tendo chances menores que personagens medianos em determinados cenários (apenas um treinamento regular já é o suficiente).

---

## Sistemas modelados

### 1) Sistema atual — **Maior d20 + Bônus vs DT**

- Passos:
  1. Rola-se `n` d20 (com `n` podendo ser negativo para representar rolar mais dados e escolher o **menor**: `n=0` → 2 dados, `n=-1` → 3 dados, etc.).
  2. Escolhe-se **o maior** (se `n > 0`) ou **o menor** (se `n ≤ 0`).
  3. Soma-se o **bônus total**.
  4. Compara-se com uma **DT fixa** (5, 10, 15, …, 35).

- Bônus possíveis: combinações de **±2**, **±5**, **+10**, **+15** (em alguns casos é possível obter -10, mas já foge um pouco do foco da comparação).
- A tabela gerada mostra `P(sucesso)` para todas as combinações de `n` e bônus.

**Arquivo gerado:** `prob_sistema_atual.csv`
**Script:** `sistema_atual.py`

---

### 2) Proposta — **Resolução por Sucessos**

- Cada d20 gera:
  - **20** → **+2 sucessos** (_crítico_);
  - **\[DT, 19]** → **+1 sucesso**;
  - **2..(DT−1)** → **0**;
  - **1** → **−1** (_falha crítica_).

- Soma-se o total de sucessos dos `n` dados.
- A tabela mostra `P(≥k)` e `P(=k)` para `n` de 1 a 18 e `k` de 1 a 10.
- DTs pares e ímpares são apresentadas em blocos verticais separados.

**Arquivo gerado:** `prob_dice_pool_d20.csv`
**Script:** `dice_pool_d20.py`

---

## Por que a proposta de **sucessos**?

O sistema atual funciona bem para medir a performance média, mas pode apresentar distorções em DTs muito altas, pois o **ganho de mais dados** não necessariamente escala de forma equilibrada e comparável com o aumento de bônus.
A proposta por sucessos:
- Aumento do número de dados tem um impacto equilibrado com o ganho de bônus (pouco menor, equivalente, pouco maior, dependendo do contexto).
- Permite calibrar **metas de k sucessos** para diferentes categorias de dificuldade, o que incentiva jogadores a fazer testes em conjunto.
- Integra críticos e falhas de forma natural no cálculo.

---
