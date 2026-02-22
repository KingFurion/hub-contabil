import streamlit as st
import pandas as pd

st.set_page_config(page_title="Hub de Inteligência Contábil", layout="wide")

# CSS customizado para os Cards e Título Neon
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
        margin-bottom: 0px;
    }
    
    .hero-subtitle {
        text-align: center;
        color: #a0a0a0;
        font-size: 1.5rem;
        margin-bottom: 2rem;
    }

    .card {
        background-color: #1c1e26;
        border: 1px solid #2d2e3a;
        border-radius: 15px;
        padding: 20px;
        transition: 0.3s;
        height: 180px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    
    .card:hover {
        border-color: #ff4d00;
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(255, 77, 0, 0.2);
    }

    .card-title {
        color: #ffffff;
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
    }

    .card-status {
        color: #00ff88;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown('<p class="hero-title">HUB DE INTELIGÊNCIA CONTÁBIL QUE TRANSFORMAM NEGÓCIOS</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">Soluções que transformam negócios.</p>', unsafe_allow_html=True)

# Botão centralizado (Simulando o Saiba Mais)
col_btn1, col_btn2, col_btn3 = st.columns([1, 0.4, 1])
with col_btn2:
    st.button("SAIBA MAIS ↗", use_container_width=True)

st.write("---")
st.markdown("### 🛠️ Seus Projetos em Andamento")

# --- GRID DE CARDS (3 colunas) ---
row1_col1, row1_col2, row1_col3 = st.columns(3)

with row1_col1:
    st.markdown("""
    <div class="card">
        <div class="card-title">📊 Dashboard</div>
        <p>Status: <span class="card-status">Automação de Folha Concluída</span></p>
    </div>
    """, unsafe_allow_html=True)

with row1_col2:
    st.markdown("""
    <div class="card">
        <div class="card-title">🧬 Zoox Tecnologia</div>
        <p>Status: <span class="card-status">Automação de Folha Concluída</span></p>
    </div>
    """, unsafe_allow_html=True)

with row1_col3:
    st.markdown("""
    <div class="card">
        <div class="card-title">📚 Estante Mágica</div>
        <p>Status: <span class="card-status">Automação de Folha Contábil</span></p>
    </div>
    """, unsafe_allow_html=True)

row2_col1, row2_col2, row2_col3 = st.columns(3)

with row2_col1:
    st.markdown("""
    <div class="card">
        <div class="card-title">🌾 Grupo Trigo</div>
        <p>Status: <span class="card-status">Automação Etapa de Folha OK</span></p>
    </div>
    """, unsafe_allow_html=True)

with row2_col2:
    st.markdown("""
    <div class="card">
        <div class="card-title">🏷️ TAGME</div>
        <p>Status: <span class="card-status">Rotina Automática Configurada</span></p>
    </div>
    """, unsafe_allow_html=True)

with row2_col3:
    st.markdown("""
    <div class="card">
        <div class="card-title">📈 Próximos Passos</div>
        <p>Próxima Etapa: <b>Livro Contábil</b></p>
    </div>
    """, unsafe_allow_html=True)
