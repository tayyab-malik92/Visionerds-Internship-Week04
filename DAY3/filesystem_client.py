import asyncio
from fastmcp import Client
from fastmcp.client.transports import StdioTransport


PROJECT_PATH = r"C:\Users\T14S\Desktop\Week4\DAY3\Filesystem_MCP"


async def main():

    transport = StdioTransport(
        command="npx",
        args=[
            "-y",
            "@modelcontextprotocol/server-filesystem",
            PROJECT_PATH
        ]
    )

    client = Client(transport)

    async with client:

        print("=" * 70)
        print("📂 Connected to Official Filesystem MCP Server")
        print("=" * 70)

        # ==========================================================
        # 1. Discover Available Tools
        # ==========================================================

        print("\n🛠 Available Tools\n")

        tools = await client.list_tools()

        for tool in tools:
            print(f"• {tool.name}")

        # ==========================================================
        # 2. List Directory
        # ==========================================================

        print("\n" + "=" * 70)
        print("📂 Listing Directory")
        print("=" * 70)

        result = await client.call_tool(
            "list_directory",
            {
                "path": PROJECT_PATH
            }
        )

        print(result.data)

        # ==========================================================
        # 3. Read notes.txt
        # ==========================================================

        print("\n" + "=" * 70)
        print("📄 Reading notes.txt")
        print("=" * 70)

        result = await client.call_tool(
            "read_file",
            {
                "path": f"{PROJECT_PATH}\\notes.txt"
            }
        )

        print(result.data)

        # ==========================================================
        # 4. Write todo.txt
        # ==========================================================

        print("\n" + "=" * 70)
        print("✍ Writing todo.txt")
        print("=" * 70)

        result = await client.call_tool(
            "write_file",
            {
                "path": f"{PROJECT_PATH}\\todo.txt",
                "content": """Learn MCP
Complete Visionerds Week 4
Build AI Agents
Practice ReAct Loop"""
            }
        )

        print(result.data)

        # ==========================================================
        # 5. Read todo.txt
        # ==========================================================

        print("\n" + "=" * 70)
        print("📄 Reading todo.txt")
        print("=" * 70)

        result = await client.call_tool(
            "read_file",
            {
                "path": f"{PROJECT_PATH}\\todo.txt"
            }
        )

        print(result.data)

        # ==========================================================
        # 6. Get File Information
        # ==========================================================

        print("\n" + "=" * 70)
        print("ℹ File Information")
        print("=" * 70)

        result = await client.call_tool(
            "get_file_info",
            {
                "path": f"{PROJECT_PATH}\\notes.txt"
            }
        )

        print(result.data)

        # ==========================================================
        # 7. Search Files
        # ==========================================================

        print("\n" + "=" * 70)
        print("🔍 Searching for 'hello'")
        print("=" * 70)

        result = await client.call_tool(
            "search_files",
            {
                "path": PROJECT_PATH,
                "pattern": "hello"
            }
        )

        print(result.data)

        # ==========================================================
        # 8. List Resources (Optional)
        # ==========================================================

        print("\n" + "=" * 70)
        print("📦 Resources")
        print("=" * 70)

        try:
            resources = await client.list_resources()

            if resources:
                for resource in resources:
                    print(resource)
            else:
                print("No resources exposed.")

        except Exception:
            print("No resources exposed.")

        print("\n" + "=" * 70)
        print("✅ Day 18 MCP Filesystem Demo Completed Successfully!")
        print("=" * 70)


if __name__ == "__main__":
    asyncio.run(main())