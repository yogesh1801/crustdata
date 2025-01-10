from api_doc_processor.doc_processor import ApiDocProcessor
from vector_store.vector_store import VectorStore
from assets.test_doc import api_docs
from config import config
import os
from pinecone import Pinecone, ServerlessSpec
import logging
from llm.llm import LLM
from assets.prompt_temp import prompt_temp
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def format_docs(docs):
    """Format retrieved documents into a single string"""
    return "\n\n".join(doc.page_content for doc in docs)


def main():
    os.environ["LANGCHAIN_TRACING_V2"] = "false"
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

    groq_llm = LLM().get_groq_llm(
        groq_api_key=config.GROQ_ACCESS_TOKEN,
        groq_model_name=str(config.GROQ_MODEL_NAME),
    )

    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    prompt = ChatPromptTemplate.from_template(template=prompt_temp)
    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | groq_llm
        | StrOutputParser()
    )

    answer = chain.invoke("can u tell me how to run this API")
    print(answer)
    answer = chain.invoke("what question did i ask earlier")
    print(answer)


if __name__ == "__main__":
    main()
