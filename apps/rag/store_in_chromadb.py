#Storing in Vector Store
from hmac import new
import re
from langchain_community.vectorstores import Chroma

def store_in_chromadb(page_splits,embeddings):
    vector_store=Chroma.from_documents(documents=page_splits,
                                     embedding=embeddings,
                                     persist_directory="./chroma_db")
    return vector_store

def create_new_vector_store_from_persisted(persist_directory,embedding_function):
    vector_store_from_persisted = Chroma(persist_directory=persist_directory,
                                     embedding_function=embedding_function)
    return vector_store_from_persisted

def add_new_documents_to_vector_store(vector_store, new_document):
    """
    Add new documents to the existing vector store.

    Args:
        vector_store (Chroma): The existing vector store to add new documents to.
        new_document (Document): The new document to add to the vector store.

    Returns:
        Chroma: The updated vector store with the new document added.
    """
    # Add the new document to the vector store.
    # The `add_documents` method takes a list of documents, so we wrap `new_document` in a list.
    vector_store.add_documents([new_document])
    # Return the updated vector store.
    return vector_store
def update_document_in_vector_store(vector_store, document_id, updated_document):
    vector_store.update_document(document_id, updated_document)
    return vector_store

def delete_document_in_vector_store(vector_store, document_id):
    vector_store.delete(document_id)
    return vector_store
