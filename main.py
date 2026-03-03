import streamlit as st

# Configuração da página para o estilo Clean SaaS
st.set_page_config(page_title="Hub de Inteligência Contábil", layout="wide")

# --- CSS Customizado (Estilo Puzzle com Glow Azul #00C3FF) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap');
    
    html, body, [data-testid="stSidebar"] {
        font-family: 'Poppins', sans-serif;
    }

    /* Fundo Grafite Profundo */
    .main { background-color: #0b0c0f; }
    
    /* Título Limpo */
    .hero-title {
        text-align: center;
        font-size: 2.8rem !important;
        font-weight: 800;
        color: #ffffff;
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

    /* Estilo do Card Clean */
    .card {
        background-color: #14161a;
        border: 1px solid #1c1f24;
        border-radius: 12px;
        padding: 24px;
        transition: 0.3s ease-in-out;
        height: 140px;
        margin-bottom: 10px;
        cursor: pointer;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    
    /* Efeito de hover com o Azul Solicitado #00C3FF */
    .card:hover {
        transform: translateY(-3px);
        border-color: #00C3FF; /* Azul sutil na borda */
        box-shadow: 0 0 20px rgba(0, 195, 255, 0.3); /* Glow azul sutil */
    }

    .card-title {
        color: #ffffff;
        font-size: 1.2rem;
        font-weight: 600;
        margin: 0;
    }

    .status-label { 
        color: #8a8d91; 
        font-size: 0.85rem; 
        margin: 0;
    }
    
    /* Azul para o valor do status */
    .status-value { 
        color: #00C3FF; 
        font-weight: 600; 
    }
    
    a { text-decoration: none !important; }
</style>
""", unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown('<p class="hero-title">Hub de Inteligência Contábil que Transformam Negócios</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">Soluções tecnológicas integradas para o BPO de alta performance.</p>', unsafe_allow_html=True)

st.divider()
st.markdown("### 🛠️ Seus Projetos em Andamento")

# Função para criar o card clicável corrigida
def criar_card_clean(titulo, status, chave_url):
    try:
        # Acessando os segredos de forma segura
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
col1, col2, col3 = st.columns(3)

with col1:
    criar_card_clean("📊 Dashboard", "Automação Concluída", "dashboard")
    criar_card_clean("🌾 Grupo Trigo", "Etapa de Folha OK", "trigo")

with col2:
    criar_card_clean("🧬 Zoox Tecnologia", "Automação Concluída", "zoox")
    criar_card_clean("🏷️ TAGME", "Rotina Configurada", "tagme")

with col3:
    criar_card_clean("📚 Estante Mágica", "Folha Contábil OK", "estante")
    criar_card_clean("📈 Próximos Passos", "Livro Contábil", "proximos")
