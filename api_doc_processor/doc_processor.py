from typing import List, Dict
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class ApiDocProcessor:
    def __init__(self, api_docs: List[Dict]):
        self.api_docs = api_docs
        self.documents = []

    def process_api_docs(self) -> List[Document]:
        for doc in self.api_docs:
            text = f"""
            API Name: {doc["name"]}
            Endpoint: {doc["endpoint"]}
            Description: {doc["description"]}
            CURL Example: {doc["curl"]}
            Response Example: {doc["response"]}
            """

            document = Document(page_content=text, metadata={"api_name": doc["name"]})

            self.documents.append(document)

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=200, separators=["\n\n", "\n", " ", ""]
        )

        return text_splitter.split_documents(self.documents)
