import streamlit as st
import joblib
import os
import google.generativeai as genai
# A biblioteca dotenv é usada localmente. Na nuvem, usamos st.secrets.
try:
    from dotenv import load_dotenv
except ImportError:
    pass

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Roteirizador de Suporte IA", page_icon="🤖")

# --- CARREGAMENTO DE SEGREDOS E MODELOS (BACKEND EMBUTIDO) ---

# 1. Configuração da Chave (Híbrida: Funciona no PC e na Nuvem)
chave_google = None

# Tenta pegar dos Segredos do Streamlit (Nuvem)
try:
    if "GEMINI_API_KEY" in st.secrets:
        chave_google = st.secrets["GEMINI_API_KEY"]
except FileNotFoundError:
    # Se não houver arquivo de secrets (Ambiente Local), ignora o erro
    pass
except Exception:
    pass

# Se não achou nos secrets, tenta pegar do arquivo .env (PC Local)
if not chave_google:
    try:
        load_dotenv()
        chave_google = os.getenv("GEMINI_API_KEY")
    except:
        chave_google = None

# Configurar o Gemini
if chave_google:
    genai.configure(api_key=chave_google)
else:
    st.warning("⚠️ Chave de API não encontrada. Configure o .env (Local) ou Secrets (Nuvem).")

# 2. Carregar Modelos de ML (Com Cache para não travar o site)
@st.cache_resource
def carregar_modelos():
    try:
        # O Streamlit lê os arquivos direto do repositório
        modelo = joblib.load('modelo_prioridade.pkl')
        vetor = joblib.load('vetorizador.pkl')
        return modelo, vetor
    except Exception as e:
        st.error(f"Erro ao carregar modelos .pkl: {e}")
        return None, None

modelo_prioridade, vetorizador = carregar_modelos()

# --- INTERFACE (FRONTEND) ---

st.title("🤖 Roteirizador de Suporte IA")
st.markdown("Arquitetura: **Streamlit Native** (ML e LLM rodando localmente)")

st.subheader("Novo Ticket")
descricao_ticket = st.text_area(
    "Descreva o problema:", 
    height=150, 
    placeholder="Ex: O cliente reclamou que a entrega atrasou..."
)

col1, col2 = st.columns(2)

# Botão 1: ML Clássico (Roda direto na memória do Streamlit)
with col1:
    if st.button("🔍 Prever Prioridade"):
        if descricao_ticket:
            if modelo_prioridade and vetorizador:
                vetor_input = vetorizador.transform([descricao_ticket])
                previsao = modelo_prioridade.predict(vetor_input)[0]
                st.success(f"Prioridade: {previsao}")
            else:
                st.error("Modelos não carregados.")
        else:
            st.warning("Digite um ticket.")

# Botão 2: GenAI (Chama o Google direto do Streamlit)
with col2:
    if st.button("🧠 Análise GenAI"):
        if descricao_ticket:
            if chave_google:
                try:
                    with st.spinner('Consultando Gemini...'):
                        model = genai.GenerativeModel('gemini-2.0-flash')
                        prompt = f"""
                        Analise este ticket de suporte: "{descricao_ticket}"
                        1. Resumo curto.
                        2. Categoria (Financeiro, Logística, etc).
                        3. Sentimento (Positivo, Negativo, Neutro).
                        """
                        response = model.generate_content(prompt)
                        st.markdown("### Resultado")
                        st.write(response.text)
                except Exception as e:
                    st.error(f"Erro na API Google: {e}")
            else:
                st.error("Sem chave configurada.")
        else:
            st.warning("Digite um ticket.")