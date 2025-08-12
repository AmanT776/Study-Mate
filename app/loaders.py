from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import cryptography

def pdf_loader(file):
    loader = PyPDFLoader(file)
    pdf_content = loader.load()
    chunk(pdf_content)
    print(chunk)

def chunk(pdf):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 300,
        chunk_overlap = 100,
    )
    texts = text_splitter.create_documents([doc.page_content for doc in pdf])
    return texts
