from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from typing import List
from langchain_classic.schema import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
import torch
from langchain_huggingface import HuggingFaceEmbeddings


def load_pdf_files(data):
    loader = DirectoryLoader(
        data,
        glob= '*.pdf',
        loader_cls=PyPDFLoader
    )
    
    document = loader.load()
    
    return document



def filter_to_minimal_doc(docs: List[Document]) -> List[Document]:
    """
    
    This function returns only the source in metadata and original page content of the given documents.
    
    """
    minimal_docs = []
    for doc in docs:
        src = doc.metadata.get('source')
        minimal_docs.append(
            Document(
                page_content = doc.page_content,
                metadata = {'source' : src}
            )
        )
    return minimal_docs



def text_splitter(docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size= 1000,
        chunk_overlap= 200
    )
    
    texts = text_splitter.split_documents(docs)
    
    return texts




def download_embeddings_model():
    
    model_name = 'BAAI/bge-small-en'
    embeddings = HuggingFaceEmbeddings(
        model_name = model_name,
        model_kwargs = {'device' : 'cuda' if torch.cuda.is_available() else 'cpu'}
    )
    
    return embeddings