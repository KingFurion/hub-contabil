import streamlit as st

# 1. Configuração da página
st.set_page_config(page_title="Hub de Inteligência Contábil", layout="wide", initial_sidebar_state="collapsed")

# --- ESTADO DE NAVEGAÇÃO ---
if 'pagina_ativa' not in st.session_state:
    st.session_state.pagina_ativa = 'main'

def mudar_pagina(nome):
    st.session_state.pagina_ativa = nome

# --- CSS DEFINITIVO (Glow + Botão de Ação) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap');
    
    [data-testid="stSidebar"], header { display: none; }
    .main { background-color: #0b0c0f; font-family: 'Poppins', sans-serif; }

    /* Container do Card */
    .card-container {
        background-color: #14161a;
        border: 1px solid #1c1f24;
        border-radius: 12px;
        padding: 25px;
        transition: all 0.4s ease-in-out;
        height: 180px;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        position: relative;
    }
    
    .card-container:hover {
        border-color: #00C3FF;
        box-shadow: 0 0 25px rgba(0, 195, 255, 0.2);
    }

    .card-title { color: #ffffff; font-size: 1.3rem; font-weight: 600; margin-bottom: 5px; }
    .status-label { color: #8a8d91; font-size: 0.85rem; margin-bottom: 20px; }
    .status-value { color: #00C3FF; font-weight: 600; }

    /* Estilização do Botão Nativo do Streamlit para parecer parte do Card */
    div.stButton > button {
        background-color: #1c1f24 !important;
        color: #00C3FF !important;
        border: 1px solid #00C3FF !important;
        border-radius: 8px !important;
        width: 100% !important;
        font-weight: 600 !important;
        transition: 0.3s !important;
    }

    div.stButton > button:hover {
        background-color: #00C3FF !important;
        color: #000000 !important;
        box-shadow: 0 0 15px rgba(0, 195, 255, 0.4) !important;
    }

    /* Botão de Voltar (Destaque Vermelho/Cinza) */
    .btn-voltar div.stButton > button {
        width: auto !important;
        background-color: transparent !important;
        color: #8a8d91 !important;
        border: 1px solid #30363d !important;
        margin-bottom: 2rem !important;
    }
    
    .btn-voltar div.stButton > button:hover {
        color: #ffffff !important;
        border-color: #ffffff !important;
        background-color: transparent !important;
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
        st.markdown("""
            <div class="card-container">
                <div class="card-title">Zoox Tecnologia</div>
                <p class="status-label">Status: <span class="status-value">Folha para CMFlex</span></p>
            </div>
        """, unsafe_allow_html=True)
        # O botão agora fica visível logo abaixo do texto, indicando a ação
        st.button("Abrir Automação Zoox", key="btn_zoox", on_click=mudar_pagina, args=('zoox',))

    with col2:
        st.markdown("""
            <div class="card-container">
                <div class="card-title">Estante Mágica</div>
                <p class="status-label">Status: <span class="status-value">Folha para MXM</span></p>
            </div>
        """, unsafe_allow_html=True)
        st.button("Abrir Automação Estante", key="btn_estante", on_click=mudar_pagina, args=('estante',))

elif st.session_state.pagina_ativa == 'zoox':
    st.markdown('<div class="btn-voltar">', unsafe_allow_html=True)
    st.button("← Voltar para o Hub Principal", on_click=mudar_pagina, args=('main',))
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.title("🚀 Automação Zoox Tecnologia")
    st.info("Otimização de processos para CMFlex.")
    st.file_uploader("Upload do arquivo Zoox", type=['xlsx', 'csv'])

elif st.session_state.pagina_ativa == 'estante':
    st.markdown('<div class="btn-voltar">', unsafe_allow_html=True)
    st.button("← Voltar para o Hub Principal", on_click=mudar_pagina, args=('main',))
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.title("📦 Automação Estante Mágica")
    st.info("Otimização de processos para MXM.")
    st.date_input("Data da Competência")
