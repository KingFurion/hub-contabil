import streamlit as st

# Configuração da página para o estilo Clean/SaaS Moderno
st.set_page_config(page_title="Hub de Inteligência Contábil", layout="wide")

# --- CSS Customizado (Baseado na Referência Clean/Puzzle) ---
st.markdown("""
<style>
    /* Importando uma fonte mais clean (Poppins) */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap');
    
    html, body, {
        font-family: 'Poppins', sans-serif;
    }

    /* Fundo Grafite Super Escuro (Clean Dark) */
    .main { background-color: #0b0c0f; }
    
    /* Título Limpo e Moderno */
    .hero-title {
        text-align: center;
        font-size: 2.8rem !important;
        font-weight: 800;
        color: #ffffff; /* Texto branco puro no título */
        margin-bottom: 0px;
        letter-spacing: -1px;
    }
    
    /* Subtítulo em Cinza Claro */
    .hero-subtitle {
        text-align: center;
        color: #8a8d91;
        font-size: 1.1rem;
        font-weight: 300;
        margin-bottom: 3rem;
    }

    /* Estilo do Card com Borda Sutil e Glow Verde-Menta ao passar o mouse */
    .card {
        background-color: #14161a; /* Fundo do Card levemente mais claro */
        border: 1px solid #1c1f24; /* Borda inicial quase invisível */
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
    
    /* Efeito de hover (Glow Verde-Menta Suave) */
    .card:hover {
        transform: translateY(-3px);
        border-color: #00e676; /* Verde-menta sutil na borda */
        box-shadow: 0 0 20px rgba(0, 230, 118, 0.3); /* Glow verde sutil */
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
        font-weight: 300;
        margin: 0;
    }
    
    /* Verde-menta suave para o status concluído */
    .status-value { 
        color: #00e676; 
        font-weight: 600; 
    }
    
    /* Remove sublinhado dos links */
    a { text-decoration: none !important; }
    
    /* Estilizando a barra lateral para combinar */
    {
        background-color: #14161a;
        border-right: 1px solid #1c1f24;
    }
</style>
""", unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown('<p class="hero-title">Hub de Inteligência Contábil que Transformam Negócios</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">Soluções tecnológicas integradas para o BPO de alta performance.</p>', unsafe_allow_html=True)

st.divider()
st.markdown("### 🛠️ Seus Projetos em Andamento")

# Função para criar o card clicável com tratamento de erro para os segredos
def criar_card_clean(titulo, status, chave_url):
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

# --- GRID DE CARDS CLEAN ---
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
