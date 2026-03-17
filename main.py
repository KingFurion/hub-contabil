import streamlit as st

# 1. Configuração da página
st.set_page_config(page_title="Hub de Inteligência Contábil", layout="wide", initial_sidebar_state="collapsed")

# --- ESTADO DE NAVEGAÇÃO ---
if 'pagina_ativa' not in st.session_state:
    st.session_state.pagina_ativa = 'main'

def mudar_pagina(nome):
    st.session_state.pagina_ativa = nome

# --- CSS REFINADO (Correção de Largura e Alinhamento) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap');
    
    [data-testid="stSidebar"], header { display: none; }
    .main { background-color: #0b0c0f; font-family: 'Poppins', sans-serif; }

    /* Forçar a coluna a não ter padding extra que esmague o card */
    [data-testid="column"] {
        width: 100% !important;
    }

    /* Container Principal do Card */
    .card-wrapper {
        position: relative;
        width: 100%;
        height: 180px;
        margin-bottom: 20px;
    }

    /* Conteúdo de texto sobreposto */
    .card-content {
        position: absolute;
        top: 25px;
        left: 25px;
        z-index: 5; /* Garante que fique acima de tudo */
        pointer-events: none;
    }

    .card-title { color: #ffffff; font-size: 1.3rem; font-weight: 600; margin: 0; }
    .status-label { color: #8a8d91; font-size: 0.85rem; margin-top: 5px; }
    .status-value { color: #00C3FF; font-weight: 600; }

    /* O BOTÃO QUE SE TORNA O CARD */
    div.stButton > button {
        background-color: #14161a !important;
        border: 1px solid #1c1f24 !important;
        border-radius: 12px !important;
        height: 180px !important;
        width: 100% !important; /* Ocupa toda a largura da coluna */
        transition: all 0.4s ease-in-out !important;
        display: flex !important;
        align-items: flex-end !important;
        justify-content: flex-start !important;
        padding: 25px !important;
        color: #00C3FF !important;
        font-weight: 600 !important;
        text-decoration: none !important;
    }

    div.stButton > button:hover {
        border-color: #00C3FF !important;
        box-shadow: 0 0 25px rgba(0, 195, 255, 0.2) !important;
        transform: translateY(-5px) !important;
        background-color: #1c1f24 !important;
    }

    /* Ajuste para o botão de voltar nas páginas internas */
    .btn-voltar div.stButton > button {
        height: auto !important;
        width: auto !important;
        background-color: transparent !important;
        padding: 10px 20px !important;
        margin-bottom: 20px !important;
        align-items: center !important;
    }
</style>
""", unsafe_allow_html=True)

# --- ROTEADOR ---

if st.session_state.pagina_ativa == 'main':
    st.markdown('<p style="text-align:center; font-size:2.8rem; font-weight:800; color:white; margin-top:2rem;">Hub de Inteligência Contábil</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#8a8d91; font-size:1.1rem; margin-bottom:3rem;">Soluções integradas para o BPO de alta performance.</p>', unsafe_allow_html=True)
    st.divider()
    
    st.markdown("### 🛠️ Automação de Folha x Contábil")
    
    # Grid de 2 colunas
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="card-wrapper">', unsafe_allow_html=True)
        st.markdown("""
            <div class="card-content">
                <div class="card-title">Zoox Tecnologia</div>
                <p class="status-label">Status: <span class="status-value">Folha para CMFlex</span></p>
            </div>
        """, unsafe_allow_html=True)
        st.button("Acessar Automação →", key="btn_zoox", on_click=mudar_pagina, args=('zoox',))
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card-wrapper">', unsafe_allow_html=True)
        st.markdown("""
            <div class="card-content">
                <div class="card-title">Estante Mágica</div>
                <p class="status-label">Status: <span class="status-value">Folha para MXM</span></p>
            </div>
        """, unsafe_allow_html=True)
        st.button("Acessar Automação →", key="btn_estante", on_click=mudar_pagina, args=('estante',))
        st.markdown('</div>', unsafe_allow_html=True)

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
