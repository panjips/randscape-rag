from langchain_core.output_parsers import StrOutputParser
from langchain_ollama.chat_models import ChatOllama
from langchain_core.runnables import RunnableLambda,RunnablePassthrough

from app.config import Config
from .query import retriver
from .prompt import prompt

def chat(question):
    model = ChatOllama(model=Config.OLLAMA_MODEL, base_url=Config.OLLAMA_BASE_URL)
    context = retriver(query=question)

    retrieve_context = RunnableLambda(lambda _: {"context": context, "question": question})
    chain = (
        retrieve_context
        | prompt()
        | model
        | StrOutputParser()
    )
    result = chain.invoke({})

    return [result]
