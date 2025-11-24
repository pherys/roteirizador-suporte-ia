🤖 Roteirizador de Suporte Inteligente

Case de Estudo: Sistema de triagem inteligente aplicando Engenharia de Software e IA para otimizar o suporte ao cliente (focado no cenário iFood).

🌐 Demo Online

👉 Clique aqui para testar o Roteirizador IA ao vivo

O sistema está rodando na nuvem (Streamlit Cloud), processando tickets em tempo real com Machine Learning e Google Gemini.

📋 Sobre o Projeto

Este projeto resolve o problema de triagem manual de tickets de suporte. Ele utiliza uma abordagem híbrida de Inteligência Artificial:

Classificação de Prioridade (Machine Learning Clássico): Um modelo Scikit-Learn treinado prevê a urgência do ticket.

Análise Semântica (Generative AI): Integração com Google Gemini para resumir o problema e categorizar o ticket (ex: Financeiro, Logística, Qualidade).

Interface de Operação: Dashboard interativo em Streamlit para o time de atendimento.

🛠️ Arquitetura

O sistema utiliza uma arquitetura Streamlit Native para alta eficiência:

Frontend & Backend Unificados: O Streamlit gerencia tanto a interface quanto a execução dos modelos Python.

Gestão de Segredos Híbrida: Funciona localmente via .env e na nuvem via Streamlit Secrets.

Containerização: O projeto mantém compatibilidade total com Docker para portabilidade.

🚀 Como Rodar o Projeto (Para Desenvolvedores)

Se você quiser clonar e rodar na sua máquina, siga os passos abaixo:

Pré-requisitos

Git

Python 3.9+

Uma chave de API do Google Gemini

🔐 Passo 0: Configuração

Clone o repositório.

Crie um arquivo .env na raiz.

Adicione sua chave: GEMINI_API_KEY=sua_chave_aqui

🐍 Opção A: Rodando Localmente

# 1. Instale as dependências
pip install -r requirements.txt

# 2. Execute o App
streamlit run interface.py


🐳 Opção B: Rodando via Docker

# 1. Construa a imagem
docker build -t roteirizador-ia .

# 2. Rode o container (passando as variáveis de ambiente)
docker run -p 8501:8501 --env-file .env roteirizador-ia


📂 Estrutura de Arquivos

interface.py: Aplicação principal (Frontend + Lógica de IA).

requirements.txt: Dependências do projeto.

Dockerfile: Receita para containerização.

exploracao.ipynb: Notebook de treino e análise de dados.

*.pkl: Modelos de ML serializados (Vetorizador e Classificador).

Desenvolvido por Fernanda Brito como parte de estudos avançados em Engenharia de Computação e IA.