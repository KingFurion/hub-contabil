import os, sys, re, yaml, pandas as pd
from pandas.tseries.offsets import MonthEnd, DateOffset

# ----------------- Funções utilitárias -----------------

def as_text(x):
    if x is None or (isinstance(x, float) and pd.isna(x)):
        return ''
    return str(x).strip()

def to_float(v):
    s = as_text(v)
    if not s:
        return 0.0
    try:
        if ',' in s and '.' in s:
            s = s.replace('.', '').replace(',', '.')
        elif ',' in s and '.' not in s:
            s = s.replace(',', '.')
        return float(s)
    except:
        try:
            return float(s)
        except:
            return 0.0

def limpa_rubrica(v):
    s = as_text(v)
    if not s:
        return ''
    try:
        return str(int(float(s)))
    except:
        return s

def data_competencia_auto(df):
    for i in range(min(10, len(df))):
        row = df.iloc[i]
        for j in range(min(10, len(row.index))):
            if 'Competência:' in as_text(row.get(j, '')):
                for k in range(j+1, min(j+15, len(row.index))):
                    dt = as_text(row.get(k, ''))
                    if '-' in dt:
                        try:
                            base = pd.to_datetime(dt, format='%Y-%m-%d')
                            return (base + MonthEnd(0)).strftime('%d/%m/%Y')
                        except:
                            pass
    return '31/10/2025'

def parse_date_flex(txt):
    if not txt:
        return None
    try:
        dt = pd.to_datetime(txt, dayfirst=True, errors='coerce')
        if pd.isna(dt):
            dt = pd.to_datetime(txt, errors='coerce')
        return dt if not pd.isna(dt) else None
    except:
        return None

def resolve_data(cfg, df):
    data_cfg = cfg.get('data', {})
    modo = as_text(data_cfg.get('modo', 'auto')).lower()
    fmt = data_cfg.get('formato_saida', '%d/%m/%Y')
    desloc = int(data_cfg.get('deslocamento_meses', 0))

    if modo == 'fixa':
        dt = parse_date_flex(as_text(data_cfg.get('fixa')))
        if dt is None:
            raise ValueError("Config 'data.fixa' inválida. Use DD/MM/YYYY ou YYYY-MM-DD.")
    elif modo == 'competencia':
        comp = as_text(data_cfg.get('competencia'))
        if not comp:
            raise ValueError("Config 'data.competencia' ausente (YYYY-MM).")
        base = pd.to_datetime(f"{comp}-01", format='%Y-%m-%d', errors='coerce')
        if pd.isna(base):
            raise ValueError("Config 'data.competencia' inválida. Use YYYY-MM.")
        dt = base + MonthEnd(0)
    else:  # auto
        auto_str = data_competencia_auto(df)
        dt = parse_date_flex(auto_str)
        if dt is None:
            raise ValueError("Não foi possível detectar a data automaticamente no arquivo.")

    if desloc != 0:
        dt = dt + DateOffset(months=desloc)
        if modo in ('competencia', 'auto'):
            dt = dt + MonthEnd(0)

    return dt.strftime(fmt)

def extrai_cc_middle(s):
    # De "21 - 13.05 - PERFORMANCE GLOBAL" pega "13.05"
    s = as_text(s).replace('C.Custo:', '').strip()
    m = re.search(r'-\s*([^-]+?)\s*-', s)
    return m.group(1).strip() if m else s

# -------- Conversão de letras de coluna -> índice 0-based --------

def col_letter_to_index(col: str) -> int:
    s = col.strip().upper()
    if not re.fullmatch(r'[A-Z]+', s):
        raise ValueError(f"Coluna inválida: {col}")
    n = 0
    for ch in s:
        n = n * 26 + (ord(ch) - ord('A') + 1)
    return n - 1

def map_letters_to_indices(cols: dict) -> dict:
    out = {}
    for sec, m in cols.items():
        out[sec] = {}
        for k, v in m.items():
            out[sec][k] = col_letter_to_index(v) if isinstance(v, str) else int(v)
    return out

# ----------------- Pipeline principal -----------------

def main(cfg_path='config.yaml'):
    # Lê config.yaml (como dict, sem [0])
    with open(cfg_path, 'r', encoding='utf-8') as f:
        cfg = yaml.safe_load(f)

    arq_in  = cfg.get('arquivo_entrada', 'Extrato_Mensal.xlsx')
    arq_out = cfg.get('arquivo_saida', 'Tabela_Completa_Unica.xlsx')

    # Converte letras (B, I, AD...) para índices 0-based
    cols_letters = cfg['colunas']
    cols = map_letters_to_indices(cols_letters)

    ordem_map = {t: i for i, t in enumerate(cfg.get('ordenacao', ['PROVENTOS', 'DESCONTOS', 'INFORMATIVA']))}
    dedup   = cfg.get('deduplicacao', {})
    captura = cfg.get('captura', {})
    only_first_resumo = bool(captura.get('apenas_primeiro_resumo_por_cc', True))

    if not os.path.exists(arq_in):
        print(f"Arquivo não encontrado: {arq_in}", file=sys.stderr)
        sys.exit(1)

    df = pd.read_excel(arq_in, header=None, engine='openpyxl')
    df = df.dropna(axis=0, how='all').reset_index(drop=True)

    data_ref = resolve_data(cfg, df)

    resultados = []
    cc_atual = None
    capturar = False
    processados = set()

    for _, row in df.iterrows():
        col0 = as_text(row.get(0, ''))

        # linha de início de centro de custo
        if col0.startswith('C.Custo'):
            cc_atual = col0
            capturar = False
            continue

        # linha "Resumo por Rubricas..."
        if 'Resumo por Rubricas do Centro de Custo' in col0:
            if not cc_atual:
                continue
            cc_key = extrai_cc_middle(cc_atual)
            if only_first_resumo and cc_key in processados:
                capturar = False
            else:
                capturar = True
                processados.add(cc_key)
            continue

        if not capturar or not cc_atual:
            continue

        # INFORMATIVA (FGTS)
        inf_desc_idx = cols['informativa']['descricao']
        inf_val_idx  = cols['informativa']['valor']
        desc_fgts = as_text(row.get(inf_desc_idx, '')).upper()
        if 'VALOR DO FGTS' in desc_fgts or 'FGTS DO MES' in desc_fgts or 'FGTS DO MÊS' in desc_fgts:
            v_fgts = to_float(row.get(inf_val_idx, ''))
            if v_fgts > 0:
                resultados.append({
                    'Data': data_ref,
                    'C.Custo': cc_atual,
                    'Tipo': 'INFORMATIVA',
                    'Rubrica': '996',
                    'Descrição': as_text(row.get(inf_desc_idx, '')),
                    'Valor': v_fgts
                })

        # PROVENTOS
        p = cols['proventos']
        rub_p = limpa_rubrica(row.get(p['rubrica'], ''))
        des_p = as_text(row.get(p['descricao'], ''))
        val_p = to_float(row.get(p['valor'], ''))
        if val_p > 0 and (rub_p or des_p):
            resultados.append({
                'Data': data_ref,
                'C.Custo': cc_atual,
                'Tipo': 'PROVENTOS',
                'Rubrica': rub_p,
                'Descrição': des_p,
                'Valor': val_p
            })

        # DESCONTOS
        d = cols['descontos']
        rub_d = limpa_rubrica(row.get(d['rubrica'], ''))
        des_d = as_text(row.get(d['descricao'], ''))
        val_d = to_float(row.get(d['valor'], ''))
        if val_d > 0 and (rub_d or des_d):
            resultados.append({
                'Data': data_ref,
                'C.Custo': cc_atual,
                'Tipo': 'DESCONTOS',
                'Rubrica': rub_d,
                'Descrição': des_d,
                'Valor': val_d
            })

    if not resultados:
        print('Nenhum registro identificado.')
        sys.exit(0)

    df_out = pd.DataFrame(resultados, columns=['Data', 'C.Custo', 'Tipo', 'Rubrica', 'Descrição', 'Valor'])

    # Normalizações
    df_out['C.Custo']   = df_out['C.Custo'].apply(extrai_cc_middle)
    df_out['Descrição'] = df_out['Descrição'].astype(str).str.strip().str.replace(r'\s+', ' ', regex=True)
    df_out['Rubrica']   = df_out['Rubrica'].astype(str).str.strip()
    df_out['Valor']     = df_out['Valor'].astype(float).round(dedup.get('arredondar_valor', 2))

    # Consolidação: junta seções do mesmo C.Custo somando valores
    df_out = (
        df_out
        .groupby(['Data', 'C.Custo', 'Tipo', 'Rubrica', 'Descrição'], as_index=False, sort=False)['Valor']
        .sum()
    )

    # Ordenação final
    df_out['__ord'] = df_out['Tipo'].map(ordem_map)
    df_out = df_out.sort_values(['C.Custo', '__ord'], kind='stable').drop(columns='__ord')

    df_out.to_excel(arq_out, index=False)
    print(f"OK! Gerado {arq_out} com {len(df_out)} linhas.")
    print(df_out.head(10))

if __name__ == '__main__':
    cfg_file = sys.argv[1] if len(sys.argv) > 1 else 'config.yaml'
    main(cfg_file)
