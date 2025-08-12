from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_and_chunk_file(file):
    loader = PyPDFLoader(file)
    pdf_content = loader.load()
    chunks = chunk(pdf_content)
    return chunks
def chunk(pdf):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 100,
    )
    texts = text_splitter.create_documents([doc.page_content for doc in pdf])
    return texts
