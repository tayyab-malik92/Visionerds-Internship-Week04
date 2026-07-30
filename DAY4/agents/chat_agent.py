from llm import ask_llm


def answer(question: str):

    prompt = f"""
You are a friendly AI assistant.

User:
{question}
"""

    return ask_llm(prompt)