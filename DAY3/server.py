from fastmcp import FastMCP

mcp = FastMCP("Visionerds MCP Server")


@mcp.tool
def calculator(a: int, b: int, operation: str = "add") -> float:
    """Perform arithmetic operations."""

    if operation == "add":
        return a + b

    elif operation == "subtract":
        return a - b

    elif operation == "multiply":
        return a * b

    elif operation == "divide":
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    raise ValueError("Invalid operation")


@mcp.tool
def word_counter(text: str) -> int:
    """Count words."""
    return len(text.split())


@mcp.tool
def character_counter(text: str) -> int:
    """Count characters."""
    return len(text)


if __name__ == "__main__":
    mcp.run()