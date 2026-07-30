# Day 19 – Multi-Agent Router System

## Overview

This project demonstrates a **Multi-Agent AI System** where a **Router Agent** intelligently decides which specialized agent should handle a user's request.

Instead of one AI agent trying to perform every task, responsibilities are divided among multiple agents:

* **Chat Agent** – Handles normal conversations.
* **Tool Agent** – Uses MCP (Model Context Protocol) tools.
* **Document Agent** – Retrieves information from documents using a RAG pipeline.

This architecture is more modular, scalable, and easier to maintain than a single-agent system.

---

## Learning Objectives

* Understand the Multi-Agent architecture.
* Learn the Router Pattern.
* Route user queries to specialized agents.
* Integrate Retrieval-Augmented Generation (RAG).
* Integrate MCP-based Tool Calling.

---

## Project Structure

```text
DAY4/
│
├── main.py
├── router.py
├── llm.py
├── config.py
├── .env
├── requirements.txt
│
├── agent.py
│
├── agents/
│   ├── chat_agent.py
│   ├── rag_agent.py
│   └── tool_agent.py
│
├── rag/
│   ├── build_vector_store.py
│   ├── vector_store.pkl
│   ├── chunks.pkl
│   └── documents/
│       └── sample.pdf
│
└── mcp/
    └── server.py
```

---

## System Architecture

```text
                    User
                      │
                      ▼
                Router Agent
                      │
      ┌───────────────┼───────────────┐
      ▼               ▼               ▼
 Chat Agent      Tool Agent      Document Agent
                      │
                      ▼
                 MCP Server
```

---

## Agents

### Chat Agent

Handles general conversations and greetings using the LLM.

Example:

```
Hello
Who are you?
How are you?
```

---

### Tool Agent

Handles requests that require external tools.

It connects to the MCP Server and executes tools such as:

* Calculator
* Word Counter
* Character Counter

Example:

```
Multiply 45 by 90
Count words in Hello World
```

---

### Document Agent

Uses Retrieval-Augmented Generation (RAG).

Workflow:

1. Convert user query into an embedding.
2. Search the vector database.
3. Retrieve the most relevant document chunks.
4. Send the retrieved context to the LLM.
5. Generate the final answer.


---

## Router Agent

The Router Agent is the coordinator of the system.

It analyzes the user's query and selects one of the following routes:

* chat
* tool
* document

The selected agent processes the request and returns the final response.

---

## Technologies Used

* Python
* Groq API
* Llama 3.3 70B
* FastMCP
* Model Context Protocol (MCP)
* Sentence Transformers
* all-MiniLM-L6-v2
* NumPy
* Pickle
* python-dotenv

```

### Core Logic

Multi-Agent Architecture

```text
User
   │
   ▼
Router Agent
   │
   ├── Chat Agent
   ├── Tool Agent
   └── Document Agent
```

Each agent has one responsibility, making the system easier to maintain, extend, and debug.

---

## Key Learnings

* Built a Router Agent to coordinate specialized agents.
* Implemented a three-way routing mechanism.
* Integrated MCP for tool execution.
* Integrated RAG for document-based question answering.
* Designed a modular Multi-Agent architecture that can be extended with additional agents in the future.

---


