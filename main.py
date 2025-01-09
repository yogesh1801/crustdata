from api_doc_processor.doc_processor import ApiDocProcessor
from vector_store.vector_store import VectorStore
from assets.test_doc import api_docs
from config import config
import os
from pinecone import Pinecone, ServerlessSpec
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def main():
    os.environ["PINECONE_API_KEY"] = str(config.PINECONE_ACCESS_TOKEN)

    pc = Pinecone()

    index_name = config.INDEX_NAME

    if index_name not in pc.list_indexes().names():
        pc.create_index(
            name=index_name,
            dimension=384,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1"),
        )

    api_doc_processor = ApiDocProcessor(api_docs=api_docs)
    processed_api_documents = api_doc_processor.process_api_docs()

    vector_store = VectorStore(
        model_name=str(config.EMBEDDINGS_MODEL_NAME),
        documents=processed_api_documents,
        index_name=index_name,
    )
    vector_store = vector_store.initialize_vectorstore()


if __name__ == "__main__":
    main()
