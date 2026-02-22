import streamlit as st
import pandas as pd

# Configuração da página para o estilo SaaS
st.set_page_config(page_title="Hub Contábil - Insigne", layout="wide")

# Estilização do Título Principal
st.markdown("<h1 style='text-align: center; color: #ff4d00;'>Hub de Inteligência Contábil</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Inovação tecnológica para o fechamento de hoje. Pra sempre.</p>", unsafe_allow_html=True)

st.divider()

# Menu Lateral
st.sidebar.title("Navegação")
paginas = st.sidebar.radio("Selecione a ferramenta:", ["Dashboard", "Conciliação Bancária", "Automações de Folha"])

if paginas == "Dashboard":
    # Cards de Resumo (Estilo SaaS)
    col1, col2, col3 = st.columns(3)
    col1.metric("Automações Ativas", "4", "Zoox & Estante")
    col2.metric("Eficiência", "+35%", "Fechamento Rápido")
    col3.metric("Status", "Ciclo Aberto", "Grupo Trigo")
    
    st.subheader("🚀 Meus Projetos na Insigne")
    st.info("**Zoox Tecnologia**: Automação de folha via Python concluída.")
    st.info("**Estante Mágica**: Processo de folha parametrizado.")
    st.warning("**Grupo Trigo**: Próxima etapa - Automação do livro contábil.")

elif paginas == "Conciliação Bancária":
    st.title("🏦 Conciliação de Clientes e Fornecedores")
    arquivo = st.file_uploader("Subir arquivo Excel para análise de duplicidade", type=['xlsx'])
    
    if arquivo:
        df = pd.read_excel(arquivo)
        st.success("Arquivo carregado com sucesso!")
        
        # Lógica de Duplicidade
        if 'ID_Fatura' in df.columns:
            duplicados = df[df.duplicated(subset=['ID_Fatura'], keep=False)]
            if not duplicados.empty:
                st.error(f"Alerta: Encontramos {len(duplicados)} possíveis duplicidades!")
                st.dataframe(duplicados)
            else:
                st.success("Nenhuma duplicidade encontrada por ID.")
        else:
            st.warning("Coluna 'ID_Fatura' não encontrada para análise automática.")

elif paginas == "Automações de Folha":
    st.title("📄 Processamento de Folha")
    cliente = st.selectbox("Selecione o Cliente:", ["Zoox Tecnologia", "Estante Mágica", "TAGME", "Grupo Trigo"])
    if st.button(f"Rodar Automação para {cliente}"):
        st.write(f"Iniciando scripts Python para {cliente}...")
