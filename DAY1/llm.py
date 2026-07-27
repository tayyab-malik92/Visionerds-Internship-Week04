from openai import OpenAI

from config import GROQ_API_KEY, BASE_URL, MODEL
from schemas import TOOLS

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url=BASE_URL
)


def ask_llm(messages):
    """
    Send conversation to Groq and return the assistant message.
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=TOOLS,
        tool_choice="auto"
    )

    return response.choices[0].message