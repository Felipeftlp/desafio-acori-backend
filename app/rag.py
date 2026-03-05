from langchain_ollama import ChatOllama, OllamaEmbeddings

from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader, DirectoryLoader

from langchain_text_splitters  import RecursiveCharacterTextSplitter

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers  import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from app.config import settings

embeddings = OllamaEmbeddings(
    model="nomic-embed-text",
    base_url="http://localhost:11434"
)

def build_vectorstore():
    loader = DirectoryLoader(
        "data/matchs_by_league",
        glob="**/*.txt"
    )

    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    docs = splitter.split_documents(documents)

    vectorstore = Chroma.from_documents(
        docs,
        embeddings,
        persist_directory=settings.CHROMA_PERSIST_DIR
    )

    return vectorstore

def get_qa_chain():
    vectorstore = Chroma(
        persist_directory=settings.CHROMA_PERSIST_DIR,
        embedding_function=embeddings
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

    llm = ChatOllama(
        model= settings.MODEL_NAME,
        base_url="http://localhost:11434",
        temperature=settings.TEMPERATURE
    )

    template = """
        "Você é um analista especialista em Esports e atua como jornalista de League of Legends. "
        "Responda às perguntas dos usuários sobre escalações, campeonatos e estatísticas usando EXCLUSIVAMENTE "
        "os trechos de contexto fornecidos abaixo. "
        "Se a informação não estiver no contexto, diga: 'Minha base de dados atualizada não possui essa informação no momento.' "
        "NUNCA invente resultados de partidas ou escalações de jogadores.\n\n"
        
        "Contexto recuperado:\n{context}"

        "Pergunta do usuário:\n{question}"
        )
    """

    prompt = ChatPromptTemplate.from_template(template)

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    rag_chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough(),
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain