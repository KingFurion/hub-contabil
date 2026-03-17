import streamlit as st

# 1. Configuração da página
st.set_page_config(page_title="Hub de Inteligência Contábil", layout="wide", initial_sidebar_state="collapsed")

# --- ESTADO DE NAVEGAÇÃO ---
if 'pagina_ativa' not in st.session_state:
    st.session_state.pagina_ativa = 'main'

def mudar_pagina(nome):
    st.session_state.pagina_ativa = nome

# --- CSS PARA INTEGRAR BOTÃO DENTRO DO CARD ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap');
    
    [data-testid="stSidebar"], header { display: none; }
    .main { background-color: #0b0c0f; font-family: 'Poppins', sans-serif; }

    /* Estilização do Container que vira o Card */
    div[data-testid="stVerticalBlock"] > div:has(div.card-hook) {
        background-color: #14161a;
        border: 1px solid #1c1f24;
        border-radius: 12px;
        padding: 25px;
        transition: all 0.4s ease-in-out;
    }
    
    div[data-testid="stVerticalBlock"] > div:has(div.card-hook):hover {
        border-color: #00C3FF;
        box-shadow: 0 0 25px rgba(0, 195, 255, 0.2);
    }

    /* Textos dentro do Card */
    .card-title { color: #ffffff; font-size: 1.3rem; font-weight: 600; margin-bottom: 5px; }
    .status-label { color: #8a8d91; font-size: 0.85rem; margin-bottom: 15px; }
    .status-value { color: #00C3FF; font-weight: 600; }

    /* Botão customizado para dentro do Card */
    div.stButton > button {
        background-color: transparent !important;
        color: #00C3FF !important;
        border: 1px solid #00C3FF !important;
        width: 100% !important;
        transition: 0.3s !important;
    }
    div.stButton > button:hover {
        background-color: #00C3FF !important;
        color: #000000 !important;
    }

    /* Botão de Voltar Lateral */
    .btn-voltar div.stButton > button {
        width: auto !important;
        border: 1px solid #30363d !important;
        color: #8a8d91 !important;
    }
</style>
""", unsafe_allow_html=True)

# --- NAVEGAÇÃO ---

if st.session_state.pagina_ativa == 'main':
    st.markdown('<p style="text-align:center; font-size:2.8rem; font-weight:800; color:white; margin-top:2rem;">Hub de Inteligência Contábil</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#8a8d91; font-size:1.1rem; margin-bottom:3rem;">Soluções integradas para o BPO de alta performance.</p>', unsafe_allow_html=True)
    st.divider()
    
    st.markdown("### 🛠️ Automação de Folha x Contábil")
    col1, col2 = st.columns(2)

    with col1:
        # Iniciamos um container que o CSS vai identificar como "Card"
        with st.container():
            st.markdown('<div class="card-hook"></div>', unsafe_allow_html=True) # Gancho para o CSS
            st.markdown('<div class="card-title">Zoox Tecnologia</div>', unsafe_allow_html=True)
            st.markdown('<p class="status-label">Status: <span class="status-value">Folha para CMFlex</span></p>', unsafe_allow_html=True)
            st.button("Acessar Automação", key="btn_zoox", on_click=mudar_pagina, args=('zoox',))

    with col2:
        with st.container():
            st.markdown('<div class="card-hook"></div>', unsafe_allow_html=True)
            st.markdown('<div class="card-title">Estante Mágica</div>', unsafe_allow_html=True)
            st.markdown('<p class="status-label">Status: <span class="status-value">Folha para MXM</span></p>', unsafe_allow_html=True)
            st.button("Acessar Automação", key="btn_estante", on_click=mudar_pagina, args=('estante',))

elif st.session_state.pagina_ativa == 'zoox':
    st.markdown('<div class="btn-voltar">', unsafe_allow_html=True)
    st.button("← Voltar ao Hub", on_click=mudar_pagina, args=('main',))
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.title("🚀 Automação Zoox Tecnologia")
    st.info("Área de processamento Zoox.")
    st.file_uploader("Upload do arquivo", type=['xlsx', 'csv'])

elif st.session_state.pagina_ativa == 'estante':
    st.markdown('<div class="btn-voltar">', unsafe_allow_html=True)
    st.button("← Voltar ao Hub", on_click=mudar_pagina, args=('main',))
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.title("📦 Automação Estante Mágica")
    st.info("Área de processamento Estante Mágica.")
