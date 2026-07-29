from openai import OpenAI
from config import API_KEY, BASE_URL, MODEL
import json

client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)


SYSTEM_PROMPT = """
You are an AI Agent.

Available tools:

1. calculator
Arguments:
a
b
operation

2. word_counter
Arguments:
text

3. character_counter
Arguments:
text

If a tool is needed, respond ONLY in JSON.

Example:

{
 "tool":"calculator",
 "arguments":{
     "a":15,
     "b":5,
     "operation":"multiply"
 }
}

If no tool is needed, reply normally.
"""


def ask_llm(user_query):

    response = client.chat.completions.create(
        model=MODEL,
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_query
            }
        ]
    )

    return response.choices[0].message.content