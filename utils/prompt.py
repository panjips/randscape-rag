from langchain.prompts import ChatPromptTemplate

def prompt():
    template = """
        You are an intelligent assistant. Answer the question based only on the following context:
        {context}

        Question: {question}

        IMPORTANT:
        - If the user question is not clear, you can ask for clarification.
        - If the user is like "hello" or similar, you can respond with a greeting.
        - If the context does not contain relevant information, say "I don't know."!.
        - The response should be in English.
        - Use only the provided context to answer!.
        - Provide a clear and concise response.
    """
    prompt = ChatPromptTemplate.from_template(template)

    return prompt