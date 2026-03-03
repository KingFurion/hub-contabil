import streamlit as st

st.set_page_config(page_title="Hub de Inteligência Contábil", layout="wide")

# --- CSS Customizado (Borda Azul e Efeito Clicável) ---
st.markdown("""
<style>
    .main { background-color: #0e1117; }
    
    .hero-title {
        text-align: center;
        font-size: 3rem !important;
        font-weight: 800;
        background: linear-gradient(90deg, #ffffff, #4facfe, #00f2fe);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .hero-subtitle {
        text-align: center;
        color: #a0a0a0;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }

    /* Estilo do Card com Borda Azul Forte */
    .card {
        background-color: #1c1e26;
        border: 2px solid #004dff; /* Azul Forte */
        border-radius: 15px;
        padding: 20px;
        transition: 0.3s;
        height: 150px;
        margin-bottom: 10px;
        cursor: pointer;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 0 20px rgba(0, 77, 255, 0.6);
        border-color: #0080ff;
    }

    .card-title {
        color: #ffffff;
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 10px;
    }

    .status-label { color: #a0a0a0; font-size: 0.9rem; }
    .status-value { color: #00ff88; font-weight: 600; }
    
    /* Remove sublinhado dos links */
    a { text-decoration: none !important; }
</style>
""", unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown('<p class="hero-title">HUB DE INTELIGÊNCIA CONTÁBIL QUE TRANSFORMAM NEGÓCIOS</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">Soluções tecnológicas para o fechamento de hoje. Pra sempre.</p>', unsafe_allow_html=True)

st.divider()
st.markdown("### 🛠️ Seus Projetos em Andamento")

# Função para criar o card clicável com tratamento de erro para os segredos
def criar_card(titulo, status, chave_url):
    # Tenta buscar a URL nos segredos, se não existir, usa um link padrão
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
col1, col2, col3 = st.columns(3)

with col1:
    criar_card("📊 Dashboard", "Automação Concluída", "dashboard")
    criar_card("🌾 Grupo Trigo", "Etapa de Folha OK", "trigo")

with col2:
    criar_card("🧬 Zoox Tecnologia", "Automação Concluída", "zoox")
    criar_card("🏷️ TAGME", "Rotina Configurada", "tagme")

with col3:
    criar_card("📚 Estante Mágica", "Folha Contábil OK", "estante")
    criar_card("📈 Próximos Passos", "Livro Contábil", "proximos")
