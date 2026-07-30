import asyncio
import os
import sys

from dotenv import dotenv_values

from fastmcp import Client
from fastmcp.client.transports import StdioTransport

from agent import decide, explain


async def main():

    env = dict(os.environ)
    env.update(dotenv_values(".env"))

    transport = StdioTransport(
        command=sys.executable,
        args=["server.py"],
        env=env,
        keep_alive=False
    )

    async with Client(transport) as client:

        print("=" * 60)
        print("🚀 Visionerds MCP Agent")
        print("=" * 60)
        print("Type 'exit' to quit.")

        while True:

            user = input("\nYou: ").strip()

            if user.lower() == "exit":
                print("\nGoodbye!")
                break

            if not user:
                continue

            decision = decide(user)

            # No tool required
            if "reply" in decision:
                print(f"\nAssistant: {decision['reply']}")
                continue

            tool = decision["tool"]
            arguments = decision["arguments"]

            print(f"\n🤔 LLM decided to use: {tool}")

            result = await client.call_tool(tool, arguments)

            tool_output = result.data

            print(f"🔧 Tool Output: {tool_output}")

            # Let the LLM generate the final response
            final_answer = explain(
                user_query=user,
                tool_name=tool,
                tool_result=tool_output
            )

            print(f"\nAssistant: {final_answer}")


if __name__ == "__main__":
    asyncio.run(main())