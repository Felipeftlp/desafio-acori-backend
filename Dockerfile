FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Executa o RAG builder primeiro e, em seguida, inicia a API
CMD python init_db.py && uvicorn app.main:app --host 0.0.0.0 --port 8000