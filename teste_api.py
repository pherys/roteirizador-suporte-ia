import requests # Biblioteca para fazer requisições (como um cliente)

url = 'http://127.0.0.1:5000/prever-prioridade'

dados_teste = {
    'texto': 'Meu sistema caiu e não consigo emitir notas fiscais! Urgente!'
}

# Enviando o pedido (POST)
print("Enviando ticket para a IA...")
resposta = requests.post(url, json=dados_teste)

# Mostrando a resposta da IA
print("Status Code:", resposta.status_code)
print("Resposta JSON:", resposta.json())