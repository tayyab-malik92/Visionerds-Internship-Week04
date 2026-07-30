from openai import OpenAI
from config import API_KEY, BASE_URL, MODEL

client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)


def ask_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()