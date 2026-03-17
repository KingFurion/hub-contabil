import streamlit as st

# 1. Configuração da página
st.set_page_config(page_title="Hub de Inteligência Contábil", layout="wide", initial_sidebar_state="collapsed")

# --- INICIALIZAÇÃO DO ESTADO DE NAVEGAÇÃO ---
if 'pagina_ativa' not in st.session_state:
    st.session_state.pagina_ativa = 'main'

# Funções de Navegação
def mudar_pagina(nome):
    st.session_state.pagina_ativa = nome

# --- CSS CUSTOMIZADO (Design com Glow e Botões Invisíveis) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap');
    
    [data-testid="stSidebar"], header { display: none; }
    .main { background-color: #0b0c0f; font-family: 'Poppins', sans-serif; }

    /* Estilo do Card com Glow */
    .card-container {
        background-color: #14161a;
        border: 1px solid #1c1f24;
        border-radius: 12px;
        padding: 30px;
        transition: all 0.4s ease-in-out;
        position: relative;
        height: 160px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        z-index: 1;
    }
    
    .card-container:hover {
        border-color: #00C3FF;
        box-shadow: 0 0 25px rgba(0, 195, 255, 0.3);
        transform: translateY(-5px);
    }

    .card-title { color: #ffffff; font-size: 1.3rem; font-weight: 600; margin-bottom: 8px; }
    .status-label { color: #8a8d91; font-size: 0.9rem; }
    .status-value { color: #00C3FF; font-weight: 600; }

    /* BOTÃO INVISÍVEL POR CIMA DO CARD */
    .stButton > button {
        position: relative;
        margin-top: -175px; /* Sobrepõe o card */
        height: 160px;
        width: 100%;
        background: transparent !important;
        color: transparent !important;
        border: none !important;
        z-index: 2;
        cursor: pointer;
    }
    
    .stButton > button:hover {
        background: transparent !important;
        color: transparent !important;
        border: none !important;
    }

    /* Estilo do Botão de Voltar "Clean" */
    .btn-voltar > button {
        margin-top: 0px !important;
        height: auto !important;
        width: auto !important;
        background-color: #1c1f24 !important;
        color: #ffffff !important;
        border: 1px solid #30363d !important;
        padding: 10px 20px !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        margin-bottom: 2rem !important;
    }
    
    .btn-voltar > button:hover {
        border-color: #00C3FF !important;
        color: #00C3FF !important;
    }
</style>
""", unsafe_allow_html=True)

# --- LÓGICA DE NAVEGAÇÃO ---

if st.session_state.pagina_ativa == 'main':
    # CABEÇALHO DO HUB
    st.markdown('<p style="text-align:center; font-size:2.8rem; font-weight:800; color:white; margin-top:2rem;">Hub de Inteligência Contábil que Transformam Negócios</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#8a8d91; font-size:1.1rem; margin-bottom:3rem;">Soluções tecnológicas integradas para o BPO de alta performance.</p>', unsafe_allow_html=True)
    st.divider()
    
    st.markdown("### 🛠️ Automação de Folha x Contábil")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <div class="card-container">
                <div class="card-title">Zoox Tecnologia</div>
                <p class="status-label">Status: <span class="status-value">Automação de Folha para CMFlex</span></p>
            </div>
        """, unsafe_allow_html=True)
        st.button("Click Zoox", key="btn_zoox", on_click=mudar_pagina, args=('zoox',))

    with col2:
        st.markdown("""
            <div class="card-container">
                <div class="card-title">Estante Mágica</div>
                <p class="status-label">Status: <span class="status-value">Automação de Folha para MXM</span></p>
            </div>
        """, unsafe_allow_html=True)
        st.button("Click Estante", key="btn_estante", on_click=mudar_pagina, args=('estante',))

elif st.session_state.pagina_ativa == 'zoox':
    st.markdown('<div class="btn-voltar">', unsafe_allow_html=True)
    st.button("← Voltar ao Hub", on_click=mudar_pagina, args=('main',))
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('# 🚀 Automação Zoox Tecnologia')
    st.markdown('### Integração Folha x CMFlex')
    st.info("Área funcional para processamento de arquivos da Zoox.")
    
    # Aqui entra seu código de upload/processamento
    st.file_uploader("Arraste o relatório CMFlex aqui", type=['xlsx', 'csv'])

elif st.session_state.pagina_ativa == 'estante':
    st.markdown('<div class="btn-voltar">', unsafe_allow_html=True)
    st.button("← Voltar ao Hub", on_click=mudar_pagina, args=('main',))
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('# 📦 Automação Estante Mágica')
    st.markdown('### Integração Folha x MXM')
    st.info("Área funcional para processamento de arquivos da Estante Mágica.")
    
    st.date_input("Selecione o período")
