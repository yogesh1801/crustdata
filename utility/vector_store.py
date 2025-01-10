import logging
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec
from langchain_huggingface import HuggingFaceEmbeddings


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class VectorStore:
    def __init__(self, embeddings: HuggingFaceEmbeddings):
        self.embeddings = embeddings

    def get_pinecone_vector_store(
        self, pinecone_api_key: str, index_name: str
    ) -> PineconeVectorStore:
        pc = Pinecone(api_key=pinecone_api_key)
        logging.info(f"Creating index {index_name}")
        if index_name not in pc.list_indexes().names():
            pc.create_index(
                name=index_name,
                dimension=768,
                metric="cosine",
                spec=ServerlessSpec(cloud="aws", region="us-east-1"),
            )
        index = pc.Index(name=index_name)
        logging.info(f"Pincone vector store initiated with index {index_name}")
        self.vector_store = PineconeVectorStore(embedding=self.embeddings, index=index)
        return self.vector_store
