from langchain_core.tools import create_retriever_tool
from store_in_chromadb import create_new_vector_store_from_persisted

#Embedding
from embeddings import get_embeddings
embeddings = get_embeddings()

vector_store=create_new_vector_store_from_persisted(persist_directory="./chroma_db",
                                                    embedding_function=embeddings)

retriver= vector_store.as_retriever(search_type="mmr",search_kwargs={'k': 1,'lambda_mult':0.7})

retriever_tool = create_retriever_tool(retriever=retriver,
                                       name="retriever", 
                                       description="Retrieves relevant documents from the vector store and provides the answer to users query.")

# print(retriever_tool)

response = retriever_tool.invoke("What is the theme of document?")

print(response)
