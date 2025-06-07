#Document Loading

from document_loading import load_documents_from_file

docs=load_documents_from_file("Thinking.pdf")

#make copy of the documents
import copy
deep_copy_docs=copy.deepcopy(docs)

#remove new line characters, this is done to reduce token count
for doc in deep_copy_docs:
    doc.page_content=' '.join(doc.page_content.split())


#Document Splitting
from document_splitter import split_document

#split the documents into smaller chunks
page_splits=split_document(pages=deep_copy_docs,chunk_size=300,chunk_overlap=20)

#Embedding
from embeddings import get_embeddings
embeddings = get_embeddings()

# Inspecting and managing the vector store
from store_in_chromadb import store_in_chromadb

# Store the page splits in the vector store
vector_store = store_in_chromadb(page_splits, embeddings)

question = "How many times the word 'Jesus' used?"

#Retriever
retriever = vector_store.as_retriever(search_type="mmr",
                                      search_kwargs={"k": 2, "lambda_mult": 0.7})

retrieved_docs = retriever.invoke(question)
print("Retrieved Documents:")
for doc in retrieved_docs:
    print(f"Content: {doc.page_content} \nSource: {doc.metadata['source']}\n")
