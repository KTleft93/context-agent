from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

def create_faiss_vector_store(docs):
    embedding = OpenAIEmbeddings()
    db = FAISS.from_documents(docs, embedding)
    return db.as_retriever()
