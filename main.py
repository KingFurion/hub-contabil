import streamlit as st
import pandas as pd

st.set_page_config(page_title="Hub Contábil - João Comece", layout="wide")

st.sidebar.title("Navegação")
paginas = st.sidebar.radio("Selecione a ferramenta:", ["Início", "Conciliação Bancária", "Automações de Folha"])

if paginas == "Início":
    st.title("🚀 Hub de Automação Contábil")
    st.write("Bem-vindo ao sistema de automação desenvolvido para otimizar os processos de fechamento.")
    st.info("Utilize o menu lateral para acessar as ferramentas de conciliação e folha.")

elif paginas == "Conciliação Bancária":
    st.title("🏦 Conciliação de Clientes e Fornecedores")
    st.write("Faça o upload dos arquivos para identificar pendências ou duplicidades.")
    arquivo = st.file_uploader("Subir arquivo Excel", type=['xlsx'])
    if arquivo:
        st.success("Arquivo pronto para análise!")

elif paginas == "Automações de Folha":
    st.title("📄 Processamento de Folha de Pagamento")
    st.write("Selecione o cliente para rodar a automação específica.")
    cliente = st.selectbox("Cliente:", ["Zoox Tecnologia", "Estante Mágica", "Grupo Trigo", "TAGME"])
    st.button(f"Iniciar Processamento {cliente}")
