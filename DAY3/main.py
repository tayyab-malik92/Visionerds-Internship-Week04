import asyncio
import os
import sys

from dotenv import dotenv_values

from fastmcp import Client
from fastmcp.client.transports import StdioTransport

from agent import decide


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

        while True:

            user = input("\nYou : ")

            if user.lower() == "exit":
                break

            decision = decide(user)

            if "reply" in decision:

                print("\nAssistant :", decision["reply"])
                continue

            tool = decision["tool"]
            arguments = decision["arguments"]

            print("\n🤔 LLM Decision :", tool)

            result = await client.call_tool(
                tool,
                arguments
            )

            print("\n✅ Tool Result :", result.data)


if __name__ == "__main__":
    asyncio.run(main())