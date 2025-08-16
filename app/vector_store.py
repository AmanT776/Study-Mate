from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma


def vector_store(chunk):
    hf = HuggingFaceEmbeddings(
        model_name = "sentence-transformers/all-mpnet-base-v2",
        model_kwargs={"device": "cpu"}
        
    )
    texts = [doc.page_content for doc in chunk]
    # pdf_vectors = hf.embed_documents(texts)
    pdf_store = Chroma(
        collection_name = "pdf_db",
        embedding_function=hf,
        persist_directory="./chroma_store"
    ) 
    pdf_store.add_documents(chunk)
    return pdf_store
    