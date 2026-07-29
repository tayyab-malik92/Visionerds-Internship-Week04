import json

from llm import ask_llm


def decide(user_query):

    response = ask_llm(user_query)

    try:

        return json.loads(response)

    except:

        return {
            "reply": response
        }