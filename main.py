import streamlit as st

# 1. Configuração da página
st.set_page_config(page_title="Hub de Inteligência Contábil", layout="wide", initial_sidebar_state="collapsed")

# --- LÓGICA DE NAVEGAÇÃO ---
if 'pagina_ativa' not in st.session_state:
    st.session_state.pagina_ativa = 'main'

def ir_para(nome_pagina):
    st.session_state.pagina_ativa = nome_pagina

# --- CSS COM CORREÇÃO DE CLIQUE (Z-INDEX) ---
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
        padding: 30px;
        height: 160px;
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

    .card-title { color: #ffffff; font-size: 1.3rem; font-weight: 600; margin-bottom: 8px; }
    .status-label { color: #8a8d91; font-size: 0.9rem; }
    .status-value { color: #00C3FF; font-weight: 600; }

    /* BOTÃO INVISÍVEL - O SEGREDO DO CLIQUE */
    /* Usamos margin-top negativa para puxar o botão exatamente para cima do card anterior */
    div.stButton > button {
        position: relative;
        width: 100%;
        height: 160px !important;
        margin-top: -160px; /* Alinha o botão com o topo do card */
        background-color: transparent !important;
        color: transparent !important;
        border: none !important;
        z-index: 9999 !important; /* Força o botão a ficar na frente de tudo */
        cursor: pointer;
    }

    /* Botão de Voltar (Página Interna) */
    .btn-voltar div.stButton > button {
        margin-top: 0 !important;
        height: auto !important;
        width: auto !important;
        background-color: #1c1f24 !important;
        color: #ffffff !important;
        border: 1px solid #30363d !important;
        padding: 10px 20px !important;
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
        # 1. Primeiro desenha o card
        st.markdown("""
            <div class="card-container">
                <div class="card-title">Zoox Tecnologia</div>
                <p class="status-label">Status: <span class="status-value">Folha para CMFlex</span></p>
            </div>
        """, unsafe_allow_html=True)
        # 2. Depois coloca o botão (o CSS vai "puxar" ele para cima do card)
        st.button("Abrir Zoox", key="btn_zoox", on_click=ir_para, args=('zoox',))

    with col2:
        st.markdown("""
            <div class="card-container">
                <div class="card-title">Estante Mágica</div>
                <p class="status-label">Status: <span class="status-value">Folha para MXM</span></p>
            </div>
        """, unsafe_allow_html=True)
        st.button("Abrir Estante", key="btn_estante", on_click=ir_para, args=('estante',))

elif st.session_state.pagina_ativa == 'zoox':
    st.markdown('<div class="btn-voltar">', unsafe_allow_html=True)
    st.button("← Voltar ao Hub", on_click=ir_para, args=('main',))
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.title("🚀 Automação Zoox Tecnologia")
    st.info("Configuração pronta para processar arquivos CMFlex.")
    st.file_uploader("Upload do arquivo", type=['xlsx', 'csv'])

elif st.session_state.pagina_ativa == 'estante':
    st.markdown('<div class="btn-voltar">', unsafe_allow_html=True)
    st.button("← Voltar ao Hub", on_click=ir_para, args=('main',))
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.title("📦 Automação Estante Mágica")
    st.info("Configuração pronta para processar arquivos MXM.")
    st.date_input("Mês da Competência")
