# Day 18 – Model Context Protocol (MCP)

## Objective
Learn the Model Context Protocol (MCP) and connect to an MCP server as a client.

## Features

- Built an MCP Server using FastMCP
- Exposed three tools:
  - Calculator
  - Word Counter
  - Character Counter
- Connected through an MCP Client using StdioTransport
- Discovered tools dynamically
- Invoked tools through the MCP protocol
- Added Groq LLM configuration for future integration

## Files

- server.py → MCP Server
- client.py → MCP Client
- llm.py → Groq wrapper
- config.py → API configuration
- main.py → Simple Groq chatbot