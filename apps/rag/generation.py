from store_in_chromadb import create_new_vector_store_from_persisted

#Embedding
from embeddings import get_embeddings
embeddings = get_embeddings()
vector_store=create_new_vector_store_from_persisted(persist_directory="./chroma_db",
                                                    embedding_function=embeddings)

TEMPLATE = """
Answer the following question:
{question}
Use the following pieces of context to answer the question. If you don't know the answer, just say that you don't know. Don't try to make up an answer.
{context}

At the end of the response, specify the source of the information in the context.
Source: *Source* where *Source* only should be subsituted with the name of the document from which the context was taken.

"""
from langchain.prompts import PromptTemplate
prompt_template = PromptTemplate.from_template(TEMPLATE)

from langchain_ollama import ChatOllama
chat= ChatOllama(temperature=0, model="llama3.2")

# question = "How many times the word 'Jesus' used?"
question = "List two major thing we can learn from this?"


#Retriever
retriever = vector_store.as_retriever(search_type="mmr",
                                      search_kwargs={"k":1, "lambda_mult": 0.7})

retrieved_docs = retriever.invoke(question)
print("Retrieved Documents:")
for doc in retrieved_docs:
    print(f"Content: {doc.page_content} \nSource: {doc.metadata['source']}\n")
#chain 
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
chain=({'context':retriever,'question':RunnablePassthrough()} 
       | prompt_template 
       |chat
       |StrOutputParser())

#run the chain
response = chain.invoke(question)
print(response)
