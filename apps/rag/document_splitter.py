from langchain.text_splitter import CharacterTextSplitter,MarkdownHeaderTextSplitter

#set chunk_overlap to 0 for no overlap
def split_document(pages: str, chunk_size: int = 500, chunk_overlap: int = 0) -> list:
    """
    Splits a document into smaller chunks for processing.

    Args:
        text (str): The text of the document to be split.
        chunk_size (int): The size of each chunk.
        chunk_overlap (int): The number of overlapping characters between chunks.

    Returns:
        list: A list of text chunks.
    """
    character_splitter = CharacterTextSplitter(
        separator=" ",
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return character_splitter.split_documents(pages)

