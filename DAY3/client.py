import asyncio
import os
import sys

from dotenv import dotenv_values
from fastmcp import Client
from fastmcp.client.transports import StdioTransport
async def execute_tool(client, tool_name, arguments):

    result = await client.call_tool(
        tool_name,
        arguments
    )

    return result.data

async def main():

    env = dict(os.environ)
    env.update(dotenv_values(".env"))

    transport = StdioTransport(
        command=sys.executable,
        args=["server.py"],
        env=env,
        keep_alive=False,
    )

    client = Client(transport)

    async with client:

        print("=" * 60)
        print("CONNECTED")
        print("=" * 60)

        await client.ping()

        tools = await client.list_tools()

        print("\nAvailable Tools\n")

        for tool in tools:
            print(tool.name)

        print("\nCalculator")

        result = await client.call_tool(
            "calculator",
            {
                "a": 15,
                "b": 5,
                "operation": "multiply"
            }
        )

        print(result.data)

        print("\nWord Counter")

        result = await client.call_tool(
            "word_counter",
            {
                "text": "Large Language Models are amazing"
            }
        )

        print(result.data)

        print("\nCharacter Counter")

        result = await client.call_tool(
            "character_counter",
            {
                "text": "Artificial Intelligence"
            }
        )

        print(result.data)


if __name__ == "__main__":
    asyncio.run(main())