#Document Loading


from document_loading import load_documents_from_file

# docs=load_documents_from_file("DSA_Challenge.pdf")
docs=load_documents_from_file("RAG.docx")
print(docs)
print(len(docs))

#make copy of the documents
import copy
deep_copy_docs=copy.deepcopy(docs)

print("Before splitting :",deep_copy_docs)
#remove new line characters, this is done to reduce token count
for doc in deep_copy_docs:
    doc.page_content=' '.join(doc.page_content.split())

#print  doc content without new line characters
print("After splitting :",deep_copy_docs)
print(type(deep_copy_docs))

#Document Splitting
from document_splitter import split_document

#split the documents into smaller chunks
page_splits=split_document(pages=deep_copy_docs,chunk_size=300,chunk_overlap=20)

print(page_splits[0].page_content)
print(page_splits[1].page_content)

#Embedding
from embeddings import get_embeddings
embeddings = get_embeddings()

# vector = embeddings.embed_query(page_splits[0].page_content)
# print(vector)


# Inspecting and managing the vector store
from store_in_chromadb import store_in_chromadb, create_new_vector_store_from_persisted,add_new_documents_to_vector_store,update_document_in_vector_store,delete_document_in_vector_store
# Store the page splits in the vector store
vector_store = store_in_chromadb(page_splits, embeddings)

print(vector_store.get())

# Create a new vector store from the persisted data
persisted_vector_store = create_new_vector_store_from_persisted(
    persist_directory="./chroma_db", embedding_function=embeddings
)
print(persisted_vector_store.get())

print(persisted_vector_store.get(ids="60ba164f-9998-4118-b03b-56d203058799",include=["embeddings"]))

# #Add new documents to the vector store
from langchain.schema import Document
new_document=Document(
    page_content="This is a new document to be added to the vector store.",
    metadata={"source": "new_document.txt"}
)
add_documents_to_vector_store=add_new_documents_to_vector_store(persisted_vector_store,new_document)
print("After adding new document")
print(add_documents_to_vector_store)

import pprint
pprint.pprint(add_documents_to_vector_store.get())

print(add_documents_to_vector_store.get("8b4cf7c5-65e6-4816-a9b1-3e91753cb1fb"))

#Update document in the vector store

update_document = Document(
    page_content="This is an updated document content.",
    metadata={"source": "updated_document.txt"}
)

update_document_in_vector_store = update_document_in_vector_store(
    vector_store=persisted_vector_store,
    document_id="8b4cf7c5-65e6-4816-a9b1-3e91753cb1fb",
    updated_document=update_document
)

print(update_document_in_vector_store.get("8b4cf7c5-65e6-4816-a9b1-3e91753cb1fb"))

delete_document_in_vector_store = delete_document_in_vector_store(
    vector_store=persisted_vector_store,
    document_id="8b4cf7c5-65e6-4816-a9b1-3e91753cb1fb"
)
print(delete_document_in_vector_store.get("8b4cf7c5-65e6-4816-a9b1-3e91753cb1fb"))
