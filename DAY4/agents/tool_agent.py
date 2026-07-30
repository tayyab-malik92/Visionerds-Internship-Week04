import asyncio
import os
import sys

from dotenv import dotenv_values

from fastmcp import Client
from fastmcp.client.transports import StdioTransport

from agent import decide


async def _run(question: str):

    env = dict(os.environ)
    env.update(dotenv_values(".env"))

    transport = StdioTransport(
        command=sys.executable,
        args=["mcp/server.py"],
        env=env,
        keep_alive=False
    )

    async with Client(transport) as client:

        decision = decide(question)

        if "reply" in decision:
            return decision["reply"]

        tool = decision["tool"]
        arguments = decision["arguments"]

        result = await client.call_tool(
            tool,
            arguments
        )

        return result.data


def answer(question: str):

    return asyncio.run(
        _run(question)
    )