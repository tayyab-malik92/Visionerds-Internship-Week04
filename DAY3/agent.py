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


def explain(user_query, tool_name, tool_result):

    prompt = f"""
The user asked:

{user_query}

The MCP tool '{tool_name}' returned:

{tool_result}

Write a short, friendly answer for the user.
Do not mention JSON.
Do not mention MCP.
"""

    return ask_llm(prompt)