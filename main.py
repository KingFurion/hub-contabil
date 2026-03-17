import streamlit as st

# 1. Configuração da página (sempre o primeiro comando)
st.set_page_config(page_title="Hub de Inteligência Contábil", layout="wide", initial_sidebar_state="collapsed")

# --- LÓGICA DE NAVEGAÇÃO ---
# Inicializa a variável que controla qual página mostrar
if 'pagina_ativa' not in st.session_state:
    st.session_state.pagina_ativa = 'main'

def ir_para(nome_pagina):
    st.session_state.pagina_ativa = nome_pagina

# --- CSS PARA DESIGN PREMIUM E CLIQUE TOTAL ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap');
    
    /* Esconder elementos nativos para look de App */
    [data-testid="stSidebar"], header { display: none; }
    .main { background-color: #0b0c0f; font-family: 'Poppins', sans-serif; }

    /* Card Original (Visual) */
    .card-container {
        background-color: #14161a;
        border: 1px solid #1c1f24;
        border-radius: 12px;
        padding: 30px;
        transition: all 0.4s ease-in-out;
        height: 160px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        position: relative;
        z-index: 1;
    }
    
    .card-container:hover {
        border-color: #00C3FF;
        box-shadow: 0 0 25px rgba(0, 195, 255, 0.2);
        transform: translateY(-5px);
    }

    .card-title { color: #ffffff; font-size: 1.3rem; font-weight: 600; margin-bottom: 8px; }
    .status-label { color: #8a8d91; font-size: 0.9rem; }
    .status-value { color: #00C3FF; font-weight: 600; }

    /* CAMADA DE CLIQUE (Botão Invisível) */
    .stButton > button {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 160px;
        background: transparent !important;
        color: transparent !important;
        border: none !important;
        z-index: 10; /* Fica por cima do card para captar o clique */
        cursor: pointer;
    }

    /* Botão de Voltar (Páginas Internas) */
    .btn-voltar div.stButton > button {
        position: relative;
        height: auto;
        width: auto;
        background-color: #1c1f24 !important;
        color: #ffffff !important;
        border: 1px solid #30363d !important;
        padding: 10px 20px !important;
        margin-bottom: 2rem !important;
        z-index: 11;
    }
    .btn-voltar div.stButton > button:hover {
        border-color: #00C3FF !important;
        color: #00C3FF !important;
    }
</style>
""", unsafe_allow_html=True)

# --- RENDERIZAÇÃO DAS PÁGINAS ---

if st.session_state.pagina_ativa == 'main':
    # --- HOME / HUB ---
    st.markdown('<p style="text-align:center; font-size:2.8rem; font-weight:800; color:white; margin-top:2rem;">Hub de Inteligência Contábil</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#8a8d91; font-size:1.1rem; margin-bottom:3rem;">Soluções integradas para o BPO de alta performance.</p>', unsafe_allow_html=True)
    
    st.divider()
    st.markdown("### 🛠️ Automação de Folha x Contábil")
    
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <div class="card-container">
                <div class="card-title">Zoox Tecnologia</div>
                <p class="status-label">Status: <span class="status-value">Folha para CMFlex</span></p>
            </div>
        """, unsafe_allow_html=True)
        # O botão invisível captura o clique e executa a função
        st.button("Click Zoox", key="btn_zoox", on_click=ir_para, args=('zoox',))

    with col2:
        st.markdown("""
            <div class="card-container">
                <div class="card-title">Estante Mágica</div>
                <p class="status-label">Status: <span class="status-value">Folha para MXM</span></p>
            </div>
        """, unsafe_allow_html=True)
        st.button("Click Estante", key="btn_estante", on_click=ir_para, args=('estante',))

elif st.session_state.pagina_ativa == 'zoox':
    # --- PÁGINA ZOOX ---
    st.markdown('<div class="btn-voltar">', unsafe_allow_html=True)
    st.button("← Voltar ao Hub", on_click=ir_para, args=('main',))
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.title("🚀 Automação Zoox Tecnologia")
    st.subheader("Processamento de Folha → CMFlex")
    st.info("Utilize o campo abaixo para subir o relatório da Zoox.")
    
    arquivo_zoox = st.file_uploader("Upload do arquivo Zoox (XLSX/CSV)", type=['xlsx', 'csv'])
    if arquivo_zoox:
        st.success("Arquivo recebido! Pronto para processar.")

elif st.session_state.pagina_ativa == 'estante':
    # --- PÁGINA ESTANTE MÁGICA ---
    st.markdown('<div class="btn-voltar">', unsafe_allow_html=True)
    st.button("← Voltar ao Hub", on_click=ir_para, args=('main',))
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.title("📦 Automação Estante Mágica")
    st.subheader("Processamento de Folha → MXM")
    
    competencia = st.date_input("Mês de competência")
    st.button("Gerar Lançamentos MXM")
