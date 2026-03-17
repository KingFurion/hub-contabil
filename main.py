import streamlit as st

# 1. Configuração da página (deve ser o primeiro comando)
st.set_page_config(
    page_title="Hub de Inteligência Contábil", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# 2. CSS Customizado - Removendo menus e estilizando o Hub
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap');
    
    /* Remove a barra lateral completamente */
    [data-testid="stSidebar"] {
        display: none;
    }

    /* Remove o cabeçalho padrão do Streamlit (botões de Deploy, Menu, etc) */
    header { visibility: hidden; }
    
    /* Estilização Geral */
    html, body, [data-testid="stAppViewBlockContainer"] {
        font-family: 'Poppins', sans-serif;
        background-color: #0b0c0f;
    }

    /* Container do conteúdo principal */
    .main { 
        background-color: #0b0c0f; 
    }
    
    /* Título e Subtítulo */
    .hero-title {
        text-align: center;
        font-size: 2.8rem !important;
        font-weight: 800;
        color: #ffffff;
        margin-top: 2rem;
        margin-bottom: 5px;
        letter-spacing: -1px;
    }
    
    .hero-subtitle {
        text-align: center;
        color: #8a8d91;
        font-size: 1.1rem;
        font-weight: 300;
        margin-bottom: 3rem;
    }

    /* Estilo do Card Clean SaaS */
    .card {
        background-color: #14161a;
        border: 1px solid #1c1f24;
        border-radius: 12px;
        padding: 30px;
        transition: all 0.4s ease-in-out;
        height: 160px;
        margin-bottom: 20px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        text-decoration: none !important;
    }
    
    /* Efeito de hover com Azul #00C3FF e Glow */
    .card:hover {
        transform: translateY(-5px);
        border-color: #00C3FF;
        box-shadow: 0 10px 30px rgba(0, 195, 255, 0.2);
        background-color: #1c1f24;
    }

    .card-title {
        color: #ffffff;
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 10px;
    }

    .status-label { 
        color: #8a8d91; 
        font-size: 0.9rem; 
        margin: 0;
    }
    
    .status-value { 
        color: #00C3FF; 
        font-weight: 600; 
    }
    
    /* Remove sublinhado de links */
    a { text-decoration: none !important; }

    /* Ajuste de espaçamento entre colunas */
    [data-testid="column"] {
        padding: 0 1rem !important;
    }
</style>
""", unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown('<p class="hero-title">Hub de Inteligência Contábil que Transformam Negócios</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">Soluções tecnológicas integradas para o BPO de alta performance.</p>', unsafe_allow_html=True)

# Linha divisória sutil
st.markdown("<hr style='border: 0.5px solid #1c1f24; margin-bottom: 2rem;'>", unsafe_allow_html=True)

st.markdown("### 🛠️ Automação de Folha x Contábil")
st.write("") # Espaçamento

# Função para criar o card clicável
def criar_card_clean(titulo, status, chave_url):
    # Tenta buscar a URL no secrets, senão usa um placeholder
    try:
        url = st.secrets["urls"][chave_url]
    except:
        url = "#"
    
    card_html = f"""
    <a href="{url}" target="_blank">
        <div class="card">
            <div class="card-title">{titulo}</div>
            <p class="status-label">Status: <span class="status-value">{status}</span></p>
        </div>
    </a>
    """
    return st.markdown(card_html, unsafe_allow_html=True)

# --- GRID DE CARDS ---
col1, col2 = st.columns(2)

with col1:
    criar_card_clean("Zoox Tecnologia", "Automação de Folha para CMFlex", "zoox")

with col2:
    criar_card_clean("Estante Mágica", "Automação de Folha para MXM", "estante")

# Espaçamento inferior
st.write("")
st.write("")
