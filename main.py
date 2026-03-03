import streamlit as st
import pandas as pd

st.set_page_config(page_title="Hub de Inteligência Contábil", layout="wide")

# --- CSS Customizado Atualizado (Borda Azul e Cards Clicáveis) ---
st.markdown("""
<style>
    /* Estilo para a fonte principal */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap');
    
    html, body, {
        font-family: 'Poppins', sans-serif;
    }

    .main { background-color: #0e1117; }
    
    .hero-title {
        text-align: center;
        font-size: 3rem !important;
        font-weight: 800;
        background: linear-gradient(90deg, #ffffff, #4facfe, #00f2fe);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    
    .hero-subtitle {
        text-align: center;
        color: #a0a0a0;
        font-size: 1.2rem;
        margin-bottom: 3rem;
    }

    /* Estilo para o link que envolve o card */
    {
        text-decoration: none;
        color: inherit;
        display: block;
        margin-bottom: 20px;
    }

    /* Estilo do Card com Borda Azul Forte e Brilho Neon */
    {
        background-color: #1c1e26;
        border: 2px solid #0000FF; /* Azul forte (Pure Blue) */
        border-radius: 15px;
        padding: 20px;
        transition: 0.3s ease-in-out;
        height: 160px;
        box-shadow: 0 0 15px rgba(0, 0, 255, 0.4); /* Efeito neon azul */
    }
    
    /* Efeito de hover (passar o mouse) */
    {
        transform: translateY(-5px);
        border-color: #0080FF; /* Azul mais claro no hover */
        box-shadow: 0 0 25px rgba(0, 128, 255, 0.7); /* Brilho neon azul mais forte */
    }

    .card-title-row {
        display: flex;
        align-items: center;
        margin-bottom: 15px;
    }

    .card-icon {
        font-size: 2rem;
        margin-right: 15px;
    }

    .card-title {
        color: #ffffff;
        font-size: 1.3rem;
        font-weight: 600;
        margin: 0;
    }

    {
        color: #a0a0a0;
        font-size: 0.95rem;
        margin: 0;
    }
    
    {
        color: #00ff88; /* Verde neon para o status */
        font-weight: 600;
    }

</style>
""", unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown('<p class="hero-title">HUB DE INTELIGÊNCIA CONTÁBIL QUE TRANSFORMAM NEGÓCIOS</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">Soluções tecnológicas para o fechamento de hoje. Pra sempre.</p>', unsafe_allow_html=True)

st.divider()
st.markdown("### 🛠️ Seus Projetos em Andamento")

# --- GRID DE CARDS CLICÁVEIS (3 colunas) ---
row1_col1, row1_col2, row1_col3 = st.columns(3)

# Card 1: Dashboard
with row1_col1:
    st.markdown(f"""
    <a href="{st.secretsCite:["urls"]["dashboard"]}" target="_blank" class="card-link">
        <div class="card">
            <div class="card-title-row">
                <span class="card-icon">📊</span>
                <p class="card-title">Dashboard</p>
            </div>
            <p class="card-status">Status: <span class="status-value">Automação de Folha Concluída</span></p>
        </div>
    </a>
    """, unsafe_allow_html=True)

# Card 2: Zoox Tecnologia
with row1_col2:
    st.markdown(f"""
    <a href="{st.secretsCite:["urls"]["zoox"]}" target="_blank" class="card-link">
        <div class="card">
            <div class="card-title-row">
                <span class="card-icon">🧬</span>
                <p class="card-title">Zoox Tecnologia</p>
            </div>
            <p class="card-status">Status: <span class="status-value">Automação de Folha Concluída</span></p>
        </div>
    </a>
    """, unsafe_allow_html=True)

# Card 3: Estante Mágica
with row1_col3:
    st.markdown(f"""
    <a href="{st.secretsCite:["urls"]["estante"]}" target="_blank" class="card-link">
        <div class="card">
            <div class="card-title-row">
                <span class="card-icon">📚</span>
                <p class="card-title">Estante Mágica</p>
            </div>
            <p class="card-status">Status: <span class="status-value">Automação de Folha Contábil</span></p>
        </div>
    </a>
    """, unsafe_allow_html=True)

row2_col1, row2_col2, row2_col3 = st.columns(3)

# Card 4: Grupo Trigo
with row2_col1:
    st.markdown(f"""
    <a href="{st.secretsCite:["urls"]["trigo"]}" target="_blank" class="card-link">
        <div class="card">
            <div class="card-title-row">
                <span class="card-icon">🌾</span>
                <p class="card-title">Grupo Trigo</p>
            </div>
            <p class="card-status">Status: <span class="status-value">Automação Etapa de Folha OK</span></p>
        </div>
    </a>
    """, unsafe_allow_html=True)

# Card 5: TAGME
with row2_col2:
    st.markdown(f"""
    <a href="{st.secretsCite:["urls"]["tagme"]}" target="_blank" class="card-link">
        <div class="card">
            <div class="card-title-row">
                <span class="card-icon">🏷️</span>
                <p class="card-title">TAGME</p>
            </div>
            <p class="card-status">Status: <span class="status-value">Rotina Automática Configurada</span></p>
        </div>
    </a>
    """, unsafe_allow_html=True)

# Card 6: Próximos Passos
with row2_col3:
    st.markdown(f"""
    <a href="#" class="card-link"> <div class="card">
            <div class="card-title-row">
                <span class="card-icon">📈</span>
                <p class="card-title">Próximos Passos</p>
            </div>
            <p class="card-status">Próxima Etapa: <b>Livro Contábil</b></p>
        </div>
    </a>
    """, unsafe_allow_html=True)

# --- Barra Lateral (Navegação Padrão) ---
st.sidebar.title("Navegação")
# ... mantenha o código original da sua barra lateral aqui se necessário ...
