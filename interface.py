import streamlit as st
import requests

# Configuração da Página
st.set_page_config(page_title="Roteirizador de Suporte Inteligente", page_icon="🤖")

st.title("🤖 Roteirizador de Suporte IA")
st.markdown("Sistema inteligente para classificação e triagem de tickets do iFood.")

# Área de Entrada
st.subheader("Novo Ticket")
descricao_ticket = st.text_area("Descreva o problema do cliente:", height=150, placeholder="Ex: O cliente reclamou que a entrega atrasou e a comida chegou fria...")

# Configuração da API (Apontando para o seu Docker)
URL_API = "http://localhost:5000"

# Botões de Ação
col1, col2 = st.columns(2)

with col1:
    if st.button("🔍 Prever Prioridade (ML Clássico)"):
        if descricao_ticket:
            try:
                # ROTA CORRIGIDA AQUI
                response = requests.post(f"{URL_API}/prever-prioridade", json={"texto": descricao_ticket})
                
                if response.status_code == 200:
                    dados = response.json()
                    prioridade = dados.get('prioridade_ml', 'Desconhecida')
                    st.success(f"Prioridade Prevista: {prioridade}")
                else:
                    st.error(f"Erro do Servidor: {response.status_code}")
            except Exception as e:
                st.error(f"Erro de conexão: {e}")
        else:
            st.warning("Por favor, digite um ticket.")

with col2:
    if st.button("🧠 Análise Profunda (GenAI)"):
        if descricao_ticket:
            try:
                with st.spinner('O Gemini está analisando...'):
                    # ROTA CORRIGIDA AQUI
                    response = requests.post(f"{URL_API}/analisar-ticket", json={"texto": descricao_ticket})
                    
                if response.status_code == 200:
                    dados = response.json()
                    st.markdown("### Análise da IA Generativa")
                    st.write(dados.get('analise_ia', 'Sem resposta'))
                else:
                    st.error(f"Erro do Servidor: {response.status_code}")
            except Exception as e:
                st.error(f"Erro de conexão: {e}")
        else:
            st.warning("Por favor, digite um ticket.")

st.markdown("---")
st.caption("Sistema rodando em Arquitetura de Microsserviços: Streamlit (Front) -> Docker (Back) -> Modelos/Gemini")
