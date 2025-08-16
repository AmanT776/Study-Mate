import torch
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import CrossEncoderReranker
from langchain_community.cross_encoders import HuggingFaceCrossEncoder
from langchain_community.vectorstores import Chroma


print(torch.cuda.get_device_name(0))
print(torch.cuda.get_device_capability(0))




def create_retriever(vector_store: Chroma,search_k:int=5,reranker_top_n:int =3):
    device = torch.device("cpu") 
    base_retriever = vector_store.as_retriever(search_kwargs={"k": search_k})
    cross_encoder_model = HuggingFaceCrossEncoder(model_name='cross-encoder/ms-marco-MiniLM-L-6-v2',model_kwargs={"device": "cpu"},device=device)
    reranker = CrossEncoderReranker(model=cross_encoder_model,top_n=reranker_top_n,)
    compression_retriever = ContextualCompressionRetriever(
        base_compressor=reranker,
        base_retriever=base_retriever
    )
    return compression_retriever