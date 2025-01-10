from langchain_groq import ChatGroq
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class LLM:
    def get_groq_llm(self, model_name: str) -> ChatGroq:
        logging.info(f"getting groq llm client with model: {model_name}")
        return ChatGroq(model=model_name)
