from dotenv import load_dotenv
import os
from langchain_huggingface import HuggingFaceEmbeddings

def get_embeddings():
    # loading api key
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    load_dotenv()
    # print("Key next line")
    # print(os.environ["HUGGINGFACEHUB_API_TOKEN"][:5])
    # Initialize the HuggingFace embeddings
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings


