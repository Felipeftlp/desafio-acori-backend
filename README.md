# 🏆 Projeto ACORI - Desafio Técnico Backend (League of Legends Esports)

Esta é uma API RESTful inteligente desenvolvida para o processo seletivo de Desenvolvedor Backend do Projeto ACORI. A aplicação atua como um assistente especializado no cenário competitivo de League of Legends, utilizando RAG (Retrieval-Augmented Generation) para responder a perguntas baseadas em um contexto documental específico.

## 🚀 Tecnologias Utilizadas

* **Framework Web:** FastAPI (com documentação Swagger/OpenAPI automática)
* **Linguagem:** Python 3.11
* **Orquestração LLM & RAG:** LangChain
* **Modelo de Linguagem (LLM):** llama3.1:8b
* **Banco de Dados Vetorial:** ChromaDB 
* **Containerização:** Docker e Docker Compose 
* **Testes Automatizados:** Pytest 

## ⚙️ Pré-requisitos

Antes de começar, certifique-se de ter instalado em sua máquina:
* [Docker](https://www.docker.com/get-started) e Docker Compose 
* *(Opcional para rodar sem Docker)* Python 3.11+ e `pip`

Você também precisara instalar o [Ollama](https://ollama.com/download), caso deseje rodar localmente.

## 🛠️ Configuração Inicial

1.  Clone este repositório:
    ```bash
    git clone [https://github.com/seu-usuario/acori-backend-challenge.git](https://github.com/seu-usuario/acori-backend-challenge.git)
    cd acori-backend-challenge
    ```

2.  Crie um arquivo `.env` na raiz do projeto e adicione as variáveis de ambiente:
    ```env
    MODEL_NAME: Modelo da LLM que vai usar
    TEMPERATURE: deixe um valor baixo para a IA usar somente os dados da documentação
    CHROMA_PERSISTI_DIR: Caso vá utilizar ChromaDB para persistir os dados
    ```

## 🐳 Executando com Docker (Recomendado)

[cite_start]A maneira mais fácil e segura de rodar a aplicação é através dos containers.

```bash
docker-compose up --build
```

A API estará disponível em http://localhost:8000.

## 💻 Executando Localmente (Sem Docker)

Caso prefira rodar diretamente no seu ambiente:

Crie e ative um ambiente virtual:

```bash
# No Linux/macOS
python -m venv venv
source venv/bin/activate

# No Windows
python -m venv venv
venv\Scripts\activate
```

Instale as dependências:
    
```bash
pip install -r requirements.txt
```

Iniciar o banco com as informações para a LLM:

```bash
python init_db.py
```

Inicie o servidor local:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## 📖 Documentação da API (Swagger)
A documentação interativa da API é gerada automaticamente pelo FastAPI. Com a aplicação rodando, acesse no seu navegador:

👉 http://localhost:8000/docs
🔗 Endpoints Principais

A API possui dois endpoints principais:

    POST /api/chat: Recebe uma pergunta (ex: estatísticas de jogadores) e o session_id, recupera o contexto na base de documentos de eSports e retorna a resposta gerada pelo LLM.

    GET /api/history/{session_id}: Retorna o histórico de mensagens trocadas em uma sessão específica, mantendo o controle de contexto.

🧪 Executando os Testes

Para rodar a suíte de testes automatizados com o pytest, execute o comando abaixo no terminal (com o ambiente virtual ativado ou dentro do container):

```bash
python -m pytest
```
