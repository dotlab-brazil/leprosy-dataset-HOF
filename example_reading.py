import pandas as pd

# =========================
# 1. LOAD
# =========================
def load_data(paths):
    return {name: pd.read_csv(path) for name, path in paths.items()}


# =========================
# 2. NORMALIZAÇÃO
# =========================
def normalize_dates(df):
    if 'data_avaliacao' in df.columns:
        df['data_avaliacao'] = pd.to_datetime(df['data_avaliacao'], errors='coerce')
    return df


# =========================
# 3. PIVOT (lado → colunas)
# =========================
def pivot_lado(df, prefix):
    if 'lado' not in df.columns:
        return df

    id_cols = ['id_ficha', 'data_avaliacao']
    value_cols = [c for c in df.columns if c not in id_cols + ['lado']]

    df_pivot = df.pivot_table(
        index=id_cols,
        columns='lado',
        values=value_cols,
        aggfunc='first'
    )

    df_pivot.columns = [
        f"{prefix}_{col}_{lado}".lower()
        for col, lado in df_pivot.columns
    ]

    return df_pivot.reset_index()


# =========================
# 4. PROCESSAMENTO
# =========================
def build_dataset(data):

    # ---------
    # Base temporal (define o acompanhamento)
    # ---------
    base = normalize_dates(data['pontuacao']).copy()

    # garantir granularidade única
    base = base.drop_duplicates(subset=['id_ficha', 'data_avaliacao'])

    # ---------
    # Tabelas temporais (com data_avaliacao)
    # ---------
    face = pivot_lado(normalize_dates(data['face']), 'face')
    ms = pivot_lado(normalize_dates(data['membro_superior']), 'ms')
    mi = pivot_lado(normalize_dates(data['membro_inferior']), 'mi')
    mao = pivot_lado(normalize_dates(data['avaliacao_sensitiva_mao']), 'mao')
    pe = pivot_lado(normalize_dates(data['avaliacao_sensitiva_pe']), 'pe')
    queixas = normalize_dates(data['queixas'])

    # remover PKs desnecessárias
    queixas = queixas.drop(columns=['id_queixas'], errors='ignore')

    temporais = [face, ms, mi, mao, pe, queixas]

    # ---------
    # Merge temporal (CORRETO)
    # ---------
    df = base.copy()

    for temp_df in temporais:
        df = pd.merge(
            df,
            temp_df,
            on=['id_ficha', 'data_avaliacao'],
            how='left'
        )

    # ---------
    # Dimensões (sem data)
    # ---------
    ficha = data['ficha']
    paciente = data['paciente']

    df = df.merge(ficha, on='id_ficha', how='left')
    df = df.merge(paciente, on='id_paciente', how='left')

    return df


# =========================
# 5. EXECUÇÃO
# =========================
paths = {
    "paciente": "dataset/dataset-hof-2026 - Paciente.csv",
    "ficha": "dataset/dataset-hof-2026 - Ficha.csv",
    "face": "dataset/dataset-hof-2026 - Face.csv",
    "membro_superior": "dataset/dataset-hof-2026 - Membro superior.csv",
    "membro_inferior": "dataset/dataset-hof-2026 - Membro inferior.csv",
    "avaliacao_sensitiva_mao": "dataset/dataset-hof-2026 - Avaliação sensitiva mão.csv",
    "avaliacao_sensitiva_pe": "dataset/dataset-hof-2026 - Avaliação sensitiva pé.csv",
    "queixas": "dataset/dataset-hof-2026 - Queixas.csv",
    "pontuacao": "dataset/dataset-hof-2026 - Pontuação.csv"
}

data = load_data(paths)

df_final = build_dataset(data)

print(df_final.shape)
df_final.head()