import requests


url = 'http://127.0.0.1:5000/analisar-ticket'


ticket_br = {
    'texto': 'Olá, tentei pagar meu pedido com PIX, o dinheiro saiu da conta mas o iFood diz que não foi pago. Quero meu estorno!'
}

print("Enviando ticket para o Gemini analisar...")
resposta = requests.post(url, json=ticket_br)

print("\n--- RESPOSTA DA IA ---")
print(resposta.json())