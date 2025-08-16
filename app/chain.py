from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_groq import ChatGroq
from langchain.retrievers import ContextualCompressionRetriever
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

env = load_dotenv()
def create_rag_chain(retriever: ContextualCompressionRetriever):
    llm = ChatGroq(
        temperature=0.3,
        model_name="llama3-8b-8192",
    )
    prompt_template = """
        You are a knowledgeable and supportive study assistant. Your task is to help the student learn from the provided document.  
        Use ONLY the information in the given context to answer questions, summarize, or explain. If the answer is not in the context, say "The document does not provide enough information about this."  

         Document Context:  
        {context}  

         Student Query:  
        {question}  

        Instructions:  
        - Give clear, step-by-step explanations.  
        - Highlight key terms, definitions, and examples.  
        - If it’s a concept, provide both a short summary and a detailed explanation.  
        - Where relevant, create study aids like:  
        - bullet-point notes  
        - flashcards (Q&A format)  
        - practice questions with answers  
        - Do NOT include unrelated information outside the document.  
        """
    prompt = ChatPromptTemplate.from_template(prompt_template)
    rag_chain = (
        {"context": retriever ,"question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return rag_chain