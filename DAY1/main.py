import json

from llm import ask_llm
from tools import AVAILABLE_TOOLS

messages = [
    {
        "role": "system",
        "content": (
            "You are a helpful AI assistant. "
            "Use the available tools whenever necessary. "
            "If no tool is required, answer normally."
        )
    }
]

print("=" * 60)
print("      DAY 16 - FUNCTION CALLING AGENT (Groq)")
print("=" * 60)

while True:

    user_input = input("\nYou : ")

    if user_input.lower() == "exit":
        print("\nGoodbye!")
        break

    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    assistant_message = ask_llm(messages)

    # -------------------------
    # Tool Calling
    # -------------------------

    if assistant_message.tool_calls:

        messages.append(assistant_message)

        for tool_call in assistant_message.tool_calls:

            tool_name = tool_call.function.name

            arguments = json.loads(
                tool_call.function.arguments
            )

            print(f"\nTool Selected : {tool_name}")
            print(f"Arguments     : {arguments}")

            tool = AVAILABLE_TOOLS[tool_name]

            result = tool(**arguments)

            print(f"Tool Result   : {result}")

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result)
                }
            )

        final_message = ask_llm(messages)

        print("\nAssistant :", final_message.content)

        messages.append(
            {
                "role": "assistant",
                "content": final_message.content
            }
        )

    else:

        print("\nAssistant :", assistant_message.content)

        messages.append(
            {
                "role": "assistant",
                "content": assistant_message.content
            }
        )