import streamlit as st

# 1. Configuração da página
st.set_page_config(page_title="Hub de Inteligência Contábil", layout="wide", initial_sidebar_state="collapsed")

# --- ESTADO DE NAVEGAÇÃO ---
if 'pagina_ativa' not in st.session_state:
    st.session_state.pagina_ativa = 'main'

def mudar_pagina(nome):
    st.session_state.pagina_ativa = nome

# --- CSS PARA MANTER O DESIGN ORIGINAL E TORNAR CLICÁVEL ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap');
    
    [data-testid="stSidebar"], header { display: none; }
    .main { background-color: #0b0c0f; font-family: 'Poppins', sans-serif; }

    /* Estilo do Card Original */
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
    }
    
    .card-container:hover {
        border-color: #00C3FF;
        box-shadow: 0 0 25px rgba(0, 195, 255, 0.2);
        transform: translateY(-5px);
    }

    .card-title { color: #ffffff; font-size: 1.3rem; font-weight: 600; margin-bottom: 8px; }
    .status-label { color: #8a8d91; font-size: 0.9rem; }
    .status-value { color: #00C3FF; font-weight: 600; }

    /* BOTÃO INVISÍVEL QUE COBRE O CARD INTEIRO */
    .stButton > button {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 160px; /* Mesma altura do card */
        background: transparent !important;
        color: transparent !important;
        border: none !important;
        z-index: 10;
        cursor: pointer;
    }
    
    .stButton > button:hover {
        background: transparent !important;
        color: transparent !important;
        border: none !important;
    }

    /* Botão de Voltar para as páginas internas */
    .btn-voltar div.stButton > button {
        position: relative;
        height: auto;
        width: auto;
        background-color: #1c1f24 !important;
        color: #ffffff !important;
        border: 1px solid #30363d !important;
        padding: 10px 20px !important;
        margin-bottom: 2rem !important;
    }
</style>
""", unsafe_allow_html=True)

# --- ROTEADOR ---

if st.session_state.pagina_ativa == 'main':
    st.markdown('<p style="text-align:center; font-size:2.8rem; font-weight:800; color:white; margin-top:2rem;">Hub de Inteligência Contábil</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#8a8d91; font-size:1.1rem; margin-bottom:3rem;">Soluções integradas para o BPO de alta performance.</p>', unsafe_allow_html=True)
    st.divider()
    
    st.markdown("### 🛠️ Automação de Folha x Contábil")
    col1, col2 = st.columns(2)

    with col1:
        # Card Visual (Exatamente como o seu original)
        st.markdown("""
            <div class="card-container">
                <div class="card-title">Zoox Tecnologia</div>
                <p class="status-label">Status: <span class="status-value">Folha para CMFlex</span></p>
            </div>
        """, unsafe_allow_html=True)
        # Botão invisível posicionado exatamente sobre o card acima
        st.button("Ir para Zoox", key="btn_zoox", on_click=mudar_pagina, args=('zoox',))

    with col2:
        st.markdown("""
            <div class="card-container">
                <div class="card-title">Estante Mágica</div>
                <p class="status-label">Status: <span class="status-value">Folha para MXM</span></p>
            </div>
        """, unsafe_allow_html=True)
        st.button("Ir para Estante", key="btn_estante", on_click=mudar_pagina, args=('estante',))

elif st.session_state.pagina_ativa == 'zoox':
    st.markdown('<div class="btn-voltar">', unsafe_allow_html=True)
    st.button("← Voltar ao Hub", on_click=mudar_pagina, args=('main',))
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.title("🚀 Automação Zoox Tecnologia")
    st.info("Área funcional para o processamento de folha CMFlex.")
    st.file_uploader("Upload do relatório", type=['xlsx', 'csv'])

elif st.session_state.pagina_ativa == 'estante':
    st.markdown('<div class="btn-voltar">', unsafe_allow_html=True)
    st.button("← Voltar ao Hub", on_click=mudar_pagina, args=('main',))
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.title("📦 Automação Estante Mágica")
    st.info("Área funcional para o processamento de folha MXM.")
    st.date_input("Selecione a competência")
