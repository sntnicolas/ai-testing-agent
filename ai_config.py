import os

def create_llm(provider: str = "openai"):
    """
    Factory method to create an LLM depending on provider.
    Supported: "openai", "gigachat", "google"
    """

    if provider == "gigachat":
        # pip install langchain-gigachat
        from langchain_gigachat.chat_models import GigaChat
        return GigaChat(
            credentials=os.getenv("GIGACHAT_CREDENTIALS"),
            verify_ssl_certs=False,   # при необходимости
            model="GigaChat",
            temperature=0.0
        )

    elif provider == "google":
        # pip install langchain-google-genai
        from langchain_google_genai import ChatGoogleGenerativeAI
        return ChatGoogleGenerativeAI(
            model="gemini-1.5-pro",   # можно заменить на gemini-1.5-flash для дешевле/быстрее
            temperature=0.0,
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )

    elif provider == "openai":
        from langchain.chat_models import ChatOpenAI
        return ChatOpenAI(
            temperature=0.0,
            openai_api_key=os.getenv("OPENROUTER_API_KEY"),
            openai_api_base="https://openrouter.ai/api/v1",
            model_name="anthropic/claude-2"  # или gpt-4.1, или другое
        )

    else:
        raise ValueError(f"Unknown LLM provider: {provider}")


# Удобный глобальный объект LLM, чтобы можно было просто импортировать
llm = create_llm(os.getenv("LLM_PROVIDER", "openai"))
