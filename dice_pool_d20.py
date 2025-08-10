import csv
from typing import List, Tuple

# ====================== PARÂMETROS ======================
N_DADOS_MAX = 18  # quantidade de d20 na pool (1..N_DADOS_MAX)
SUCESSOS_MAX = 10  # colunas de k (1..SUCESSOS_MAX)
ARQUIVO_SAIDA = "prob_dice_pool_d20.csv"
# =======================================================


def formatar_probabilidade(p_maior_ou_igual: float, p_igual: float) -> str:
    """Retorna 'xx.xx (yy.yy)' ou vazio se ambas arredondarem a 0."""
    maior_ou_igual_fmt = f"{(p_maior_ou_igual * 100):05.2f}"
    igual_fmt = f"{(p_igual * 100):05.2f}"
    if maior_ou_igual_fmt == "00.00" and igual_fmt == "00.00":
        return ""
    return f"{maior_ou_igual_fmt} ({igual_fmt})"


def probabilidades_d20(dificuldade: int) -> Tuple[float, float, float, float]:
    """
    Probabilidades por resultado individual do d20 com crítico (20) e falha crítica (1).
    Retorna (p_sucesso_critico, p_sucesso, p_falha, p_falha_critica) conforme a dificuldade.
    """
    dt = max(1, min(20, dificuldade))
    p_falha_crit = 1.0 / 20.0  # resultado 1
    p_sucesso_crit = 1.0 / 20.0  # resultado 20
    n_sucessos = max(20 - max(dt, 2), 0)  # valores dt..19 (≥2)
    p_sucesso = n_sucessos / 20.0
    n_falhas = max(dt - 2, 0)  # valores 2..(dt-1)
    p_falha = n_falhas / 20.0
    return p_sucesso_crit, p_sucesso, p_falha, p_falha_crit


def fmp_da_soma(n_dados: int, dificuldade: int) -> List[float]:
    """
    FMP (função massa de probabilidade) da soma de n_dados, onde cada d20 assume valores {-1,0,1,2}.
    Suporte da soma em [-n..2n]; vetor indexado por (soma + n).
    """
    p_sucesso_crit, p_sucesso, p_falha, p_falha_crit = probabilidades_d20(dificuldade)
    resultados_dado = {2: p_sucesso_crit, 1: p_sucesso, 0: p_falha, -1: p_falha_crit}

    distribuicao = {0: 1.0}
    for _ in range(n_dados):
        distribuicao_atualizada = {}
        for sucessos, p_sucessos in distribuicao.items():
            for n_sucessos, p_n_sucessos in resultados_dado.items():
                distribuicao_atualizada[sucessos + n_sucessos] = distribuicao_atualizada.get(sucessos + n_sucessos, 0.0) + p_sucessos * p_n_sucessos
        distribuicao = distribuicao_atualizada

    tamanho = 3 * n_dados + 1
    deslocamento = n_dados
    fmp = [0.0] * tamanho
    for sucessos, p_sucessos in distribuicao.items():
        fmp[sucessos + deslocamento] = p_sucessos
    return fmp


def prob_soma_maior_ou_igual(fmp: List[float], n_dados: int, sucessos: int) -> float:
    """P(soma ≥ sucessos)."""
    deslocamento = n_dados
    inicio = max(sucessos, -n_dados)
    fim = 2 * n_dados
    return sum(fmp[i + deslocamento] for i in range(inicio, fim + 1))


def prob_soma_igual(fmp: List[float], n_dados: int, sucessos: int) -> float:
    """P(soma = sucessos)."""
    if sucessos < -n_dados or sucessos > 2 * n_dados:
        return 0.0
    return fmp[sucessos + n_dados]


def gerar_csv(
    caminho: str = ARQUIVO_SAIDA, n_max: int = N_DADOS_MAX, sucessos_max: int = SUCESSOS_MAX
) -> None:
    """Gera CSV com blocos para DT pares (20..4) e ímpares (19..3), lado a lado."""
    dts_pares = list(range(20, 3, -2))  # 20,18,...,4
    dts_impares = list(range(19, 2, -2))  # 19,17,...,3

    # Cabeçalho em duas linhas (títulos dos blocos + colunas):
    cabecalho1 = (
        ["", "", "Número de sucessos"]
        + [""] * sucessos_max
        + ["Número de sucessos"]
        + [""] * sucessos_max
    )
    cabecalho_sucesso = [f"≥{sucesso} (={sucesso})" for sucesso in range(1, sucessos_max + 1)]
    cabecalho2 = ["Qtd. de d20", "DT do dado"] + cabecalho_sucesso + ["DT do dado"] + cabecalho_sucesso

    linhas = [cabecalho1, cabecalho2]

    for dt_par, dt_impar in zip(dts_pares, dts_impares):
        for n in range(1, n_max + 1):
            fmp_par = fmp_da_soma(n, dt_par)
            fmp_impar = fmp_da_soma(n, dt_impar)

            probabilidades_par = [
                formatar_probabilidade(
                    prob_soma_maior_ou_igual(fmp_par, n, sucesso),
                    prob_soma_igual(fmp_par, n, sucesso),
                )
                for sucesso in range(1, sucessos_max + 1)
            ]

            probabilidades_impar = [
                formatar_probabilidade(
                    prob_soma_maior_ou_igual(fmp_impar, n, sucesso),
                    prob_soma_igual(fmp_impar, n, sucesso),
                )
                for sucesso in range(1, sucessos_max + 1)
            ]

            linha = (
                [n, dt_par if n == 1 else ""]
                + probabilidades_par
                + [dt_impar if n == 1 else ""]
                + probabilidades_impar
            )
            linhas.append(linha)

    with open(caminho, "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(linhas)


if __name__ == "__main__":
    gerar_csv()
    print(f"CSV gerado em: {ARQUIVO_SAIDA}")
