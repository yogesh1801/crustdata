import os
import logging
from utility.api_doc_processor import ApiDocProcessor
from assets.test_doc import api_docs
from utility.vector_store import VectorStore
from utility.llm import LLM
from utility.embeddings import Embeddings
from config import config
from langchain import hub
from utility.state import State
from langgraph.graph import START, StateGraph

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

embeddings_model = str(config.EMBEDDINGS_MODEL_NAME)
pinecone_api_key = str(config.PINECONE_ACCESS_TOKEN)
index_name = str(config.INDEX_NAME)
groq_api_key = str(config.GROQ_ACCESS_TOKEN)
groq_model_name = str(config.GROQ_MODEL_NAME)
prompt_template = str(config.PROMPT_TEMPLATE_NAME)
langsmith_api_key = str(config.LANGSMITH_API_KEY)

os.environ["PINECONE_API_KEY"] = pinecone_api_key
os.environ["GROQ_API_KEY"] = groq_api_key
os.environ["LANGSMITH_API_KEY"] = langsmith_api_key

embeddings = Embeddings().get_huggingface_embeddings(model_name=embeddings_model)

vector_store = VectorStore(embeddings=embeddings).get_pinecone_vector_store(
    pinecone_api_key=pinecone_api_key, index_name=index_name
)

llm = LLM().get_groq_llm(model_name=groq_model_name)

prompt = hub.pull(prompt_template)


def retrieve(state: State):
    retrieved_docs = vector_store.similarity_search(state["question"])
    return {"context": retrieved_docs}


def generate(state: State):
    docs_content = "\n\n".join(doc.page_content for doc in state["context"])
    messages = prompt.invoke({"question": state["question"], "context": docs_content})
    response = llm.invoke(messages)
    return {"answer": response.content}


def main():
    docs = ApiDocProcessor(api_docs=api_docs).process_api_docs()
    logging.info(f"Seeding {len(docs)} documents to the vector store")
    documents_ids = vector_store.add_documents(documents=docs)
    logging.info(f"Documents IDs {documents_ids[:3]}")

    graph_builder = StateGraph(State).add_sequence([retrieve, generate])
    graph_builder.add_edge(START, "retrieve")
    graph = graph_builder.compile()

    response = graph.invoke({"question": "give python code for Funding Milestones api"})
    print(response)


if __name__ == "__main__":
    main()
