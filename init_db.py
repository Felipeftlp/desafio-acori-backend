from app.rag import build_vectorstore

if __name__ == "__main__":
    print("Construindo base vetorial...")
    build_vectorstore()
    print("Base criada com sucesso!")