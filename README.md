# 🤖 Roteirizador de Suporte Inteligente

![Python](https://img.shields.io/badge/Python-3.9-blue?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue?style=for-the-badge&logo=docker&logoColor=white)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red?style=for-the-badge&logo=streamlit&logoColor=white)
![Gemini](https://img.shields.io/badge/AI-Gemini_2.0-orange?style=for-the-badge&logo=google&logoColor=white)

> **Case de Estudo:** Sistema de triagem inteligente aplicando Engenharia de Software e MLOps para otimizar o suporte ao cliente (focado no cenário iFood).

---

## 📋 Sobre o Projeto

Este projeto resolve o problema de **triagem manual de tickets de suporte**. Ele utiliza uma abordagem híbrida de Inteligência Artificial para processar reclamações de clientes em tempo real:

1.  **Classificação de Prioridade (Machine Learning Clássico):** Um modelo Scikit-Learn treinado prevê a urgência do ticket.
2.  **Análise Semântica (Generative AI):** Integração com **Google Gemini** para resumir o problema e categorizar o ticket (ex: Financeiro, Logística, Qualidade).
3.  **Interface de Operação:** Dashboard interativo em Streamlit para o time de atendimento.

---

## 🛠️ Arquitetura

O sistema foi desenhado seguindo a arquitetura de Microsserviços:

* **Frontend:** Streamlit (Consome a API).
* **Backend:** Flask API (Expõe os modelos de ML e LLM).
* **Containerização:** Docker (Garante reprodutibilidade).

---

## 🚀 Como Rodar o Projeto

Você pode rodar este projeto de duas formas: via **Docker** (recomendado) ou **Localmente** (Python).

### Pré-requisitos
* Git
* Docker Desktop (para método Docker)
* Python 3.9+ (para método Local)
* Uma chave de API do Google Gemini (Gratuita no Google AI Studio)

### 🔐 Passo 0: Configuração da Chave (Obrigatório)

Por segurança, as chaves de API não ficam no repositório.
1.  Na raiz do projeto, crie um arquivo chamado `.env`.
2.  Adicione sua chave do Gemini dentro dele:
    ```env
    GEMINI_API_KEY=sua_chave_aqui_sem_aspas
    ```

---

### 🐳 Opção A: Rodando com Docker (Recomendado)

O jeito mais fácil. O Docker cuida de todas as instalações.

1.  **Construa a imagem:**
    ```bash
    docker build -t roteirizador-ia .
    ```

2.  **Rode o container:**
    (Este comando conecta a porta 5000 e injeta sua chave de API)
    ```bash
    docker run -p 5000:5000 --env-file .env roteirizador-ia
    ```

3.  **Acesse a Interface:**
    O Backend estará rodando. Para ver o Frontend, abra um novo terminal (com Python instalado) e rode:
    ```bash
    pip install streamlit requests
    streamlit run interface.py
    ```

---

### 🐍 Opção B: Rodando Localmente (Sem Docker)

1.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv .venv
    # Windows:
    .venv\Scripts\activate
    # Linux/Mac:
    source .venv/bin/activate
    ```

2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    pip install streamlit requests
    ```

3.  **Inicie os serviços (Em dois terminais diferentes):**

    * **Terminal 1 (Backend):**
        ```bash
        python app.py
        ```

    * **Terminal 2 (Frontend):**
        ```bash
        streamlit run interface.py
        ```

---

## 🧪 Como Testar

1.  Acesse o endereço local que o Streamlit mostrará (geralmente `http://localhost:8501`).
2.  Digite um ticket de exemplo na caixa de texto.
    * *Ex: "Meu pedido chegou revirado e frio, quero meu dinheiro de volta."*
3.  Clique em **"Prever Prioridade"** para testar o modelo ML Local.
4.  Clique em **"Análise Profunda"** para testar a integração com o Gemini.

---

## 📂 Estrutura de Arquivos

* `app.py`: Servidor API (Flask).
* `interface.py`: Interface do Usuário (Streamlit).
* `Dockerfile`: Receita de construção do container.
* `exploracao.ipynb`: Notebook de treino e análise de dados.
* `*.pkl`: Modelos de ML serializados.

---

Desenvolvido por **Fernanda Brito** como parte de estudos avançados em Engenharia de Computação e IA.