import csv
from typing import List

# ====================== PARÂMETROS ======================
N_DADOS_MIN = -2
N_DADOS_MAX = 6
DTS = list(range(5, 36, 5))  # 5,10,15,20,25,30,35
ARQUIVO_SAIDA = "prob_sistema_atual.csv"
# =======================================================


def formatar_probabilidade(p: float) -> str:
    """Retorna 'xx.xx' ou vazio se arredondar a 0."""
    pct = f"{p * 100:05.2f}"
    return "" if pct == "00.00" else pct


def gerar_bonus_possiveis() -> List[int]:
    """Gera os bônus totais permitidos: combinações de ±2, ±5, +10, +15."""
    op2 = [-2, 0, 2]
    op5 = [-5, 0, 5]
    op10 = [0, 10]
    op15 = [0, 15]
    bonus = set()
    for b2 in op2:
        for b5 in op5:
            for b10 in op10:
                for b15 in op15:
                    bonus.add(b2 + b5 + b10 + b15)
    return sorted(bonus)


def prob_sucesso(n_dados: int, dt: int, bonus_total: int) -> float:
    """
    Probabilidade de sucesso ao comparar (resultado_escolhido + bônus) ≥ DT.
    Se n_dados > 0: rola n_dados e pega o maior.
    Se n_dados ≤ 0: rola (2 - n_dados) e pega o menor (ex.: 0→2 dados, -1→3 dados, -2→4 dados).
    """
    t = dt - bonus_total  # limiar no dado antes do bônus
    if t <= 1:
        return 1.0
    if t > 21:
        return 0.0

    if n_dados > 0:
        # P(max ≥ t) = 1 - P(todos ≤ t-1)
        return 1.0 - ((t - 1) / 20.0) ** n_dados
    else:
        m = 2 - n_dados  # n_dados = 0→2; -1→3; -2→4
        # P(min ≥ t) = P(cada ≥ t)
        return ((21 - t) / 20.0) ** m


def gerar_csv(caminho: str = ARQUIVO_SAIDA) -> None:
    bonus_possiveis = gerar_bonus_possiveis()
    cabecalho = ["Qtd. de d20", "Bônus total"] + [f"DT {dt}" for dt in DTS]
    linhas = [cabecalho]

    for n in range(N_DADOS_MIN, N_DADOS_MAX + 1):
        for i, b in enumerate(bonus_possiveis):
            probs = [formatar_probabilidade(prob_sucesso(n, dt, b)) for dt in DTS]
            linhas.append([n if i == 0 else "", b] + probs)

    with open(caminho, "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(linhas)


if __name__ == "__main__":
    gerar_csv()
    print(f"CSV gerado em: {ARQUIVO_SAIDA}")
