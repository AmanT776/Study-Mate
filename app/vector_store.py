from langchain_community.embeddings import HuggingFaceEmbeddings



def vector_store(chunk):
    hf = HuggingFaceEmbeddings(
        model_name = "sentence-transformers/all-mpnet-base-v2",
        model_kwargs={"device": "cpu"}
        
    )
    texts = [doc.page_content for doc in chunk]
    embedding_vectors = hf.embed_documents(texts)
    print(embedding_vectors)
    