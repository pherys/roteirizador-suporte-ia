import google.generativeai as genai
import os
from dotenv import load_dotenv

# Carregar chave
load_dotenv()
chave = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=chave)

print(f"--- CONSULTANDO O GOOGLE COM A CHAVE ---")

try:
    # Pede a lista de todos os modelos disponíveis para esta chave
    for m in genai.list_models():
        # Filtra apenas os que servem para gerar texto (chat)
        if 'generateContent' in m.supported_generation_methods:
            print(f"Nome encontrado: {m.name}")
            
except Exception as e:
    print(f"ERRO GRAVE: {e}")
    print("Verifique se sua API KEY está correta no arquivo .env")