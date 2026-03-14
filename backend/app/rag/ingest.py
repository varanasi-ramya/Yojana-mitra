import os
from dotenv import load_dotenv
from pathlib import Path
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document

load_dotenv()

EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")
CHROMA_PERSIST_DIR = os.getenv("CHROMA_PERSIST_DIR")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

SUMMARIES_DIR = Path(__file__).resolve().parent.parent.parent / "data" / "summaries"


def load_txt_files(folder):
    docs = []
    for text_file in folder.glob("*.txt"):
        content = text_file.read_text(encoding="utf-8")
        docs.append(Document(page_content=content, metadata={"source": text_file.name}))
        print(f"Loaded: {text_file.name}")
    return docs
