import json

from llm import ask_llm


SYSTEM_PROMPT = """
You are a Router Agent.

Your job is ONLY to decide which specialist agent should handle the user's request.

Return ONLY valid JSON.

Available routes:

1. chat
- Greetings
- Casual conversation
- Questions about yourself

Examples:
Hello
How are you?
Who are you?
Good morning

2. tool
- Calculations
- Arithmetic
- Count words
- Count characters
- Any request requiring a calculator or utility tool

Examples:
Multiply 56 by 90
Count words in Hello World
Count characters in Artificial Intelligence

3. document
- Questions that require information from uploaded PDFs or documents

Examples:
Explain Artificial Intelligence from the document.
Summarize Chapter 2.
What are the Graduate Attributes?

Output format:

{
    "route":"chat"
}

or

{
    "route":"tool"
}

or

{
    "route":"document"
}
"""


def decide(question: str):

    response = ask_llm(
        f"""
{SYSTEM_PROMPT}

User:

{question}
"""
    )

    try:
        return json.loads(response)

    except Exception:

        return {
            "route": "chat"
        }