from openai import OpenAI

from config import GROQ_API_KEY, BASE_URL, MODEL
from schemas import TOOLS


# Create Groq Client
client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url=BASE_URL
)


def ask_llm(messages):
    """
    Sends conversation history to Groq
    and returns the assistant message.
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=TOOLS,
        tool_choice="auto",
        temperature=0
    )

    return response.choices[0].message