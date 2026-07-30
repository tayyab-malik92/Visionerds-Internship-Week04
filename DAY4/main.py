import os

from colorama import Fore, Style, init

from router import decide

from agents.chat_agent import answer as chat_answer
from agents.tool_agent import answer as tool_answer
from agents.rag_agent import answer as rag_answer

init(autoreset=True)


def main():

    print("=" * 65)
    print("🤖 Visionerds Multi-Agent AI System")
    print("=" * 65)

    print("Agents Available:")
    print("• Chat Agent")
    print("• Tool Agent (MCP)")
    print("• Document Agent (RAG)")
    print()

    while True:

        question = input(Fore.CYAN + "You: " + Style.RESET_ALL)

        if question.lower() == "exit":
            print("\nGoodbye!")
            break

        decision = decide(question)

        route = decision["route"]

        print(f"\n🧠 Router selected: {route.upper()} Agent\n")

        if route == "chat":

            response = chat_answer(question)

        elif route == "tool":

            response = tool_answer(question)

        elif route == "document":

            response = rag_answer(question)

        else:

            response = "Router failed to determine the correct agent."

        print(Fore.GREEN + "Assistant: " + Style.RESET_ALL + str(response))
        print()


if __name__ == "__main__":
    main()