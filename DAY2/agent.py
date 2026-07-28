import json

from llm import ask_llm
from tools import AVAILABLE_TOOLS
from memory import Memory

from utils import (
    print_reason,
    print_action,
    print_observation,
    print_final
)


SYSTEM_PROMPT = """
You are a ReAct AI Assistant.

Rules:

1. Think step by step.
2. Use tools whenever needed.
3. Never guess calculations.
4. Continue calling tools until the task is complete.
5. Treat tool outputs as the source of truth.
"""


class Agent:

    def __init__(self):

        self.messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

        self.memory = Memory()

    def chat(self, user_input):

        self.messages.append(
            {
                "role": "user",
                "content": user_input
            }
        )

        step = 1

        while True:

            assistant = ask_llm(self.messages)

            # -------------------------
            # No Tool Needed
            # -------------------------

            if not assistant.tool_calls:

                print_final(assistant.content)

                self.messages.append(
                    {
                        "role": "assistant",
                        "content": assistant.content
                    }
                )

                return assistant.content

            self.messages.append(assistant)

            # -------------------------
            # Execute Tools
            # -------------------------

            for tool_call in assistant.tool_calls:

                tool_name = tool_call.function.name

                arguments = json.loads(
                    tool_call.function.arguments
                )

                print_reason(
                    step,
                    tool_name,
                    arguments
                )

                tool = AVAILABLE_TOOLS[tool_name]

                print_action(tool_name)

                result = tool(**arguments)

                print_observation(result)

                # Save into memory
                self.memory.save(
                    tool_name,
                    result
                )

                print("\nCurrent Memory")

                print(
                    json.dumps(
                        self.memory.show(),
                        indent=4
                    )
                )

                self.messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": json.dumps(
                            {
                                "tool": tool_name,
                                "result": result
                            }
                        )
                    }
                )

                step += 1