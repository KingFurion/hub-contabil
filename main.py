import streamlit as st

# 1. Configuração da página - Mantendo o Layout Wide
st.set_page_config(page_title="Hub de Inteligência Contábil", layout="wide", initial_sidebar_state="collapsed")

# --- INICIALIZAÇÃO DO ESTADO DE NAVEGAÇÃO ---
if 'pagina_ativa' not in st.session_state:
    st.session_state.pagina_ativa = 'main'

# Funções de Navegação
def ir_para_zoox(): st.session_state.pagina_ativa = 'zoox'
def ir_para_estante(): st.session_state.pagina_ativa = 'estante'
def voltar_ao_hub(): st.session_state.pagina_ativa = 'main'

# --- CSS CUSTOMIZADO (Design Clean SaaS) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap');
    
    /* Esconde barra lateral e elementos padrão */
    [data-testid="stSidebar"], header { display: none; }
    .main { background-color: #0b0c0f; font-family: 'Poppins', sans-serif; }

    /* Estilo do Card */
    .card-container {
        background-color: #14161a;
        border: 1px solid #1c1f24;
        border-radius: 12px;
        padding: 24px;
        transition: 0.3s ease-in-out;
        margin-bottom: 10px;
    }
    .card-container:hover {
        border-color: #00C3FF;
        box-shadow: 0 0 20px rgba(0, 195, 255, 0.3);
    }
    .card-title { color: #ffffff; font-size: 1.2rem; font-weight: 600; margin-bottom: 8px; }
    .status-label { color: #8a8d91; font-size: 0.85rem; }
    .status-value { color: #00C3FF; font-weight: 600; }

    /* Deixar o botão do Streamlit invisível por cima do card */
    div.stButton > button {
        background-color: transparent;
        border: none;
        color: transparent;
        height: 140px;
        width: 100%;
        position: absolute;
        top: -150px; /* Ajuste dependendo do layout */
        z-index: 10;
    }
</style>
""", unsafe_allow_html=True)

# --- LÓGICA DE RENDERIZAÇÃO ---

# PÁGINA PRINCIPAL (HUB)
if st.session_state.pagina_ativa == 'main':
    st.markdown('<p style="text-align:center; font-size:2.8rem; font-weight:800; color:white; margin-top:2rem;">Hub de Inteligência Contábil que Transformam Negócios</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#8a8d91; font-size:1.1rem; margin-bottom:3rem;">Soluções tecnológicas integradas para o BPO de alta performance.</p>', unsafe_allow_html=True)
    
    st.divider()
    st.markdown("### 🛠️ Automação de Folha x Contábil")

    col1, col2 = st.columns(2)

    with col1:
        # Card Visual
        st.markdown(f"""
        <div class="card-container">
            <div class="card-title">Zoox Tecnologia</div>
            <p class="status-label">Status: <span class="status-value">Automação de Folha para CMFlex</span></p>
        </div>
        """, unsafe_allow_html=True)
        # Botão Invisível que captura o clique
        st.button("Acessar Zoox", key="btn_zoox", on_click=ir_para_zoox, use_container_width=True)

    with col2:
        st.markdown(f"""
        <div class="card-container">
            <div class="card-title">Estante Mágica</div>
            <p class="status-label">Status: <span class="status-value">Automação de Folha para MXM</span></p>
        </div>
        """, unsafe_allow_html=True)
        st.button("Acessar Estante", key="btn_estante", on_click=ir_para_estante, use_container_width=True)

# PÁGINA ZOOX
elif st.session_state.pagina_ativa == 'zoox':
    st.button("⬅️ Voltar ao Hub", on_click=voltar_ao_hub)
    st.title("🚀 Automação Zoox Tecnologia")
    st.subheader("Integração Folha x CMFlex")
    st.info("Área funcional para processamento de arquivos da Zoox.")
    # Coloque aqui o seu código de automação para a Zoox
    upload = st.file_uploader("Arraste o relatório CMFlex aqui", type=['xlsx', 'csv'])

# PÁGINA ESTANTE MÁGICA
elif st.session_state.pagina_ativa == 'estante':
    st.button("⬅️ Voltar ao Hub", on_click=voltar_ao_hub)
    st.title("📦 Automação Estante Mágica")
    st.subheader("Integração Folha x MXM")
    st.info("Área funcional para processamento de arquivos da Estante Mágica.")
    # Coloque aqui o seu código de automação para a Estante Mágica
    data = st.date_input("Selecione o período da competência")
    st.button("Executar Conciliação MXM")
