from langchain_groq import ChatGroq


class LLM:
    def get_groq_llm(self, groq_api_key: str, groq_model_name: str):
        return ChatGroq(
            groq_api_key=groq_api_key, model_name=groq_model_name, temperature=0.7
        )
