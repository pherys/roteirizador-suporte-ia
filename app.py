import joblib
from flask import Flask, request, jsonify

# 1. CARREGAR O MODELO

try:
    modelo_prioridade = joblib.load('modelo_prioridade.pkl')
    vetorizador = joblib.load('vetorizador.pkl')
    print("Modelo e Vetorizador carregados com sucesso!")
except Exception as e:
    print(f"Erro ao carregar modelos: {e}")
    print("Verifique se você rodou o notebook de exploração antes!")

# 2. CRIAR O APP FLASK
app = Flask(__name__)

# 3. DEFINIR AS ROTAS

@app.route('/') # Rota raiz (http://localhost:5000/)
def home():
    
    return "A API do Roteirizador de Suporte está ONLINE! 🚀"

@app.route('/prever-prioridade', methods=['POST'])
def prever_prioridade():
    # Passo A: Receber o JSON enviado pelo cliente
    dados = request.get_json()
    texto_ticket = dados.get('texto')

    if not texto_ticket:
        return jsonify({'erro': 'Nenhum texto fornecido'}), 400

    # Passo B: Traduzir o texto
    
    texto_vetorizado = vetorizador.transform([texto_ticket])

    # Passo C: Usar o modelo para prever
    previsao = modelo_prioridade.predict(texto_vetorizado)[0]

    # Passo D: Devolver a resposta
    return jsonify({
        'texto_recebido': texto_ticket,
        'prioridade_prevista': previsao
    })

# 4. RODAR O APP
if __name__ == '__main__':
    # debug=True faz o servidor reiniciar sozinho se você mudar o código
    app.run(host='0.0.0.0', port=5000, debug=True)