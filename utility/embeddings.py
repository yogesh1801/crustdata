import logging
from langchain_huggingface import HuggingFaceEmbeddings

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class Embeddings:
    def get_huggingface_embeddings(self, model_name: str) -> HuggingFaceEmbeddings:
        logging.info(f"Getting hugging face embeddings with model {model_name}")
        return HuggingFaceEmbeddings(model_name=model_name)
