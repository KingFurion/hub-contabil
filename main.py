import streamlit as st

# 1. Configuração da página
st.set_page_config(page_title="Hub de Inteligência Contábil", layout="wide", initial_sidebar_state="collapsed")

# --- LÓGICA DE NAVEGAÇÃO ---
if 'pagina_ativa' not in st.session_state:
    st.session_state.pagina_ativa = 'main'

def mudar_pagina(nome):
    st.session_state.pagina_ativa = nome

# --- CSS REFINADO (Altura reduzida e clique total) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap');
    
    [data-testid="stSidebar"], header { display: none; }
    .main { background-color: #0b0c0f; font-family: 'Poppins', sans-serif; }

    /* Card Visual com Altura Reduzida */
    .card-container {
        background-color: #14161a;
        border: 1px solid #1c1f24;
        border-radius: 12px;
        padding: 25px;
        height: 140px; /* Altura menor para cobrir apenas o texto */
        display: flex;
        flex-direction: column;
        justify-content: center;
        position: relative;
        transition: all 0.4s ease-in-out;
    }
    .card-container:hover {
        border-color: #00C3FF;
        box-shadow: 0 0 25px rgba(0, 195, 255, 0.2);
        transform: translateY(-5px);
    }
    .card-title { color: #ffffff; font-size: 1.3rem; font-weight: 600; margin-bottom: 5px; }
    .status-label { color: #8a8d91; font-size: 0.9rem; margin: 0; }
    .status-value { color: #00C3FF; font-weight: 600; }

    /* BOTÃO INVISÍVEL (Apenas Home) */
    .home-card-btn div.stButton > button {
        position: relative;
        width: 100%;
        height: 140px !important; /* Casando com a nova altura do card */
        margin-top: -140px; 
        background-color: transparent !important;
        color: transparent !important;
        border: none !important;
        z-index: 999 !important;
        cursor: pointer;
    }

    /* BOTÃO DE VOLTAR (Páginas Internas) */
    .btn-voltar-container div.stButton > button {
        background-color: #1c1f24 !important;
        color: #ffffff !important;
        border: 1px solid #30363d !important;
        padding: 8px 20px !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        margin-bottom: 20px !important;
        width: auto !important;
        height: auto !important;
        display: flex !important;
    }
    .btn-voltar-container div.stButton > button:hover {
        border-color: #00C3FF !important;
        color: #00C3FF !important;
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
        st.markdown('<div class="home-card-btn">', unsafe_allow_html=True)
        st.button("Abrir Zoox", key="btn_zoox", on_click=mudar_pagina, args=('zoox',))
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="card-container">
                <div class="card-title">Estante Mágica</div>
                <p class="status-label">Status: <span class="status-value">Folha para MXM</span></p>
            </div>
        """, unsafe_allow_html=True)
        st.markdown('<div class="home-card-btn">', unsafe_allow_html=True)
        st.button("Abrir Estante", key="btn_estante", on_click=mudar_pagina, args=('estante',))
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.pagina_ativa == 'zoox':
    st.markdown('<div class="btn-voltar-container">', unsafe_allow_html=True)
    st.button("← Voltar ao Hub", on_click=mudar_pagina, args=('main',))
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.title("🚀 Automação Zoox Tecnologia")
    st.subheader("Integração Folha x CMFlex")
    st.file_uploader("Arraste o relatório aqui", type=['xlsx', 'csv'])

elif st.session_state.pagina_ativa == 'estante':
    st.markdown('<div class="btn-voltar-container">', unsafe_allow_html=True)
    st.button("← Voltar ao Hub", on_click=mudar_pagina, args=('main',))
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.title("📦 Automação Estante Mágica")
    st.subheader("Integração Folha x MXM")
    st.date_input("Selecione o período")
