from llama_index.core import StorageContext, VectorStoreIndex
from llama_index.vector_stores.faiss import FaissVectorStore
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext
)
import faiss
import pickle
import os

def store_in_vector_store(json_data: dict, output_dir="faiss_store"):
    # Convert JSON to text
    text = "\n".join([f"{key}: {value}" for key, value in json_data.items()])
    # Save as temp file
    os.makedirs("tmp", exist_ok=True)
    with open("tmp/document.txt", "w") as f:
        f.write(text)

    documents = SimpleDirectoryReader("tmp").load_data()

    vector_store = FaissVectorStore()
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    index = VectorStoreIndex.from_documents(documents, storage_context=storage_context)

    # Save FAISS index
    os.makedirs(output_dir, exist_ok=True)
    faiss.write_index(vector_store.index, os.path.join(output_dir, "index.faiss"))
    with open(os.path.join(output_dir, "docstore.pkl"), "wb") as f:
        pickle.dump(index.docstore, f)

def load_faiss_index(directory="faiss_store"):
    faiss_index = faiss.read_index(os.path.join(directory, "index.faiss"))
    with open(os.path.join(directory, "docstore.pkl"), "rb") as f:
        docstore = pickle.load(f)
    vector_store = FaissVectorStore(faiss_index)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    index = VectorStoreIndex.from_vector_store(vector_store=vector_store, storage_context=storage_context)
    return index

def query_brand_index(prompt: str):
    index = load_faiss_index()
    engine = index.as_query_engine()
    response = engine.query(prompt)
    return str(response)
