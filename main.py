from math import comb
import csv
from typing import List, Tuple

# ====================== PARÂMETROS ======================
N_MAX = 18  # numero_de_dados: 1..N_MAX
K_MAX = 10  # colunas de k: 1..K_MAX
OUTPUT_PATH = "prob_dice_pool_d20.csv"
# ========================================================


def format_prob_pair(prob_ge: float, prob_eq: float) -> str:
    """Formata como 'xx.xx% (yy.yy%)', com zero à esquerda e vazio se arredondar a zero."""
    ge_fmt = f"{(prob_ge * 100):05.2f}"
    eq_fmt = f"{(prob_eq * 100):05.2f}"
    if ge_fmt == "00.00" and eq_fmt == "00.00":
        return ""
    return f"{ge_fmt}% ({eq_fmt}%)"


def probs(dt: int) -> Tuple[float, float, float, float]:
    """Retorna (p_n, p_c, p_f0, p_cf) para um d20 com críticos e falhas críticas."""
    dt = max(1, min(20, dt))
    p_cf = 1.0 / 20.0  # falha crítica (1)
    p_c = 1.0 / 20.0  # crítico (20)
    n_normais = max(20 - max(dt, 2), 0)  # dt..19 (>= 2)
    p_n = n_normais / 20.0
    n_falhas = max(dt - 2, 0)  # 2..dt-1
    p_f0 = n_falhas / 20.0
    return p_n, p_c, p_f0, p_cf


def pmf_sum_n(n: int, dt: int) -> List[float]:
    """PMF da soma de n dados (suporte [-n..2n]), indexada por (soma + n)."""
    p_n, p_c, p_f0, p_cf = probs(dt)
    base = {-1: p_cf, 0: p_f0, 1: p_n, 2: p_c}
    dist = {0: 1.0}
    for _ in range(n):
        nxt = {}
        for s, ps in dist.items():
            for val, pv in base.items():
                nxt[s + val] = nxt.get(s + val, 0.0) + ps * pv
        dist = nxt
    size = 3 * n + 1
    offset = n
    pmf = [0.0] * size
    for s, p in dist.items():
        pmf[s + offset] = p
    return pmf


def prob_ge_k_from_pmf(pmf: List[float], n: int, k: int) -> float:
    """Probabilidade de soma >= k."""
    offset = n
    start = max(k, -n)
    end = 2 * n
    return sum(pmf[i + offset] for i in range(start, end + 1))


def prob_eq_k_from_pmf(pmf: List[float], n: int, k: int) -> float:
    """Probabilidade de soma = k."""
    offset = n
    if k < -n or k > 2 * n:
        return 0.0
    return pmf[k + offset]


def gerar_csv_blocos_verticais(
    path: str = OUTPUT_PATH, n_max: int = N_MAX, k_max: int = K_MAX
) -> None:
    even_dts = list(range(20, 3, -2))  # 20,18,...,4
    odd_dts = list(range(19, 2, -2))  # 19,17,...,3

    # Linha 1: rótulos dos blocos
    header1 = (
        ["", "", "Número de sucessos"]
        + [""] * (k_max - 1)
        + ["Número de sucessos"]
        + [""] * (k_max - 1)
    )
    # Linha 2: nomes das colunas
    rot_k = [f"≥{k} (={k})" for k in range(1, k_max + 1)]
    header2 = ["Número de d20", "DT do dado"] + rot_k + ["DT do dado"] + rot_k

    rows = [header1, header2]

    # Gerar blocos
    for dt_par, dt_impar in zip(even_dts, odd_dts):
        for n in range(1, n_max + 1):
            pmf_par = pmf_sum_n(n, dt_par)
            pmf_impar = pmf_sum_n(n, dt_impar)
            vals_par = [
                format_prob_pair(
                    prob_ge_k_from_pmf(pmf_par, n, k), prob_eq_k_from_pmf(pmf_par, n, k)
                )
                for k in range(1, k_max + 1)
            ]
            vals_impar = [
                format_prob_pair(
                    prob_ge_k_from_pmf(pmf_impar, n, k),
                    prob_eq_k_from_pmf(pmf_impar, n, k),
                )
                for k in range(1, k_max + 1)
            ]
            linha = (
                [n, dt_par if n == 1 else ""]
                + vals_par
                + [dt_impar if n == 1 else ""]
                + vals_impar
            )
            rows.append(linha)

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


if __name__ == "__main__":
    gerar_csv_blocos_verticais()
    print(f"CSV gerado em: {OUTPUT_PATH}")
