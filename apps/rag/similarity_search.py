#Embedding
from embeddings import get_embeddings
embeddings = get_embeddings()

from store_in_chromadb import create_new_vector_store_from_persisted
vector_store=create_new_vector_store_from_persisted(persist_directory="./chroma_db",
                                                    embedding_function=embeddings)

#similarity search

question = "How many times the word 'Jesus' used?"

# retrieved_docs = vector_store.similarity_search(query=question, k=2)

# print("Retrieved Documents:")
# for doc in retrieved_docs:
#     print(f"Content: {doc.page_content} \nSource: {doc.metadata['source']}\n")

# #Removes duplicates and retrieves the most relevant documents 
retrieved_docs = vector_store.max_marginal_relevance_search(query=question,
                                                            k=2, 
                                                            lambda_mult=0.7,
                                                            filter={"source": "Thinking.pdf"})

print("Retrieved Documents:")
for doc in retrieved_docs:
    print(f"Content: {doc.page_content} \nSource: {doc.metadata['source']}\n")

