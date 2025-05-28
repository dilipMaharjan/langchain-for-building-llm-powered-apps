from langchain_community.document_loaders import (
    PyPDFLoader, Docx2txtLoader
)
import os

def load_documents_from_file(file_path: str):
    """
    Load documents from a file of any supported type.

    Args:
        file_path (str): The path to the document file.

    Returns:
        List[Document]: A list of LangChain Document objects.
    """
    ext = os.path.splitext(file_path)[-1].lower()

    if ext == ".pdf":
        loader = PyPDFLoader(file_path)
    elif ext == ".docx":
        loader = Docx2txtLoader(file_path)

    return loader.load()
