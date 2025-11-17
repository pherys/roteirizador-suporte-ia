import joblib
import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai

# --- CONFIGURAÇÃO INICIAL ---

# 1. Carregar variáveis de ambiente
load_dotenv()

# 2. Configurar a Chave do Gemini
chave_google = os.getenv("GEMINI_API_KEY")
if not chave_google:
    print("ERRO: Chave do Google não encontrada no arquivo .env!")
else:
    genai.configure(api_key=chave_google)
    print("Gemini configurado com sucesso! 🤖")

# 3. Carregar o Modelo Local (Machine Learning Clássico)
try:
    modelo_prioridade = joblib.load('modelo_prioridade.pkl')
    vetorizador = joblib.load('vetorizador.pkl')
    print("Modelo Local carregado! 🧠")
except Exception as e:
    print(f"Aviso: Modelo local não encontrado. {e}")

# --- CRIAÇÃO DO APP FLASK ---
app = Flask(__name__)

@app.route('/')
def home():
    return "API do Roteirizador Inteligente (ML + GenAI) ONLINE! 🚀"

# --- ROTA 1: ML CLÁSSICO ---
@app.route('/prever-prioridade', methods=['POST'])
def prever_prioridade():
    dados = request.get_json()
    texto = dados.get('texto')
    
    if not texto: return jsonify({'erro': 'Sem texto'}), 400
    
    # Usando o modelo local
    vetor = vetorizador.transform([texto])
    previsao = modelo_prioridade.predict(vetor)[0]
    
    return jsonify({'prioridade_ml': previsao})

# --- ROTA 2: GENAI / GEMINI ---
@app.route('/analisar-ticket', methods=['POST'])
def analisar_ticket():
    dados = request.get_json()
    texto_ticket = dados.get('texto')

    if not texto_ticket: return jsonify({'erro': 'Sem texto'}), 400

    try:
        # A. Definir o Modelo
        model = genai.GenerativeModel('gemini-2.0-flash')

        # B. Engenharia de Prompt
        prompt = f"""
        Você é um gerente de suporte técnico experiente.
        Analise o seguinte ticket de suporte: "{texto_ticket}"

        Faça duas coisas:
        1. Resuma o problema em uma frase curta.
        2. Classifique a categoria (ex: Financeiro, Técnico, Entrega, Acesso).

        Responda neste formato:
        Resumo: [Seu resumo]
        Categoria: [Sua categoria]
        """

        # C. Gerar a resposta
        resposta = model.generate_content(prompt)

        return jsonify({
            'ticket_original': texto_ticket,
            'analise_ia': resposta.text
        })

    except Exception as e:
        return jsonify({'erro_ia': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)