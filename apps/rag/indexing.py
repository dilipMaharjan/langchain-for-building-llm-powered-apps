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
from langchain_huggingface import HuggingFaceEmbeddings
import os
from dotenv import load_dotenv
#loading api key
load_dotenv()
print("Key next line")
print(os.environ["HUGGINGFACEHUB_API_TOKEN"][:5])
# Initialize the HuggingFace embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vector = embeddings.embed_query(page_splits[0].page_content)
print(vector)
