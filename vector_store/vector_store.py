from langchain.schema import Document
from typing import List
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Pinecone
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class VectorStore:
    def __init__(
        self,
        model_name: str,
        documents: List[Document],
        index_name: str,
    ):
        self.model = model_name
        self.documents = documents
        self.index_name = index_name

    def initialize_vectorstore(self):
        embedding = HuggingFaceEmbeddings(model_name=self.model)
        vector_store = Pinecone.from_documents(
            documents=self.documents,
            embedding=embedding,
            index_name=self.index_name,
        )

        return vector_store
