TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Perform arithmetic operations on two numbers.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "number",
                        "description": "First number"
                    },
                    "b": {
                        "type": "number",
                        "description": "Second number"
                    },
                    "operation": {
                        "type": "string",
                        "enum": [
                            "add",
                            "subtract",
                            "multiply",
                            "divide"
                        ]
                    }
                },
                "required": [
                    "a",
                    "b",
                    "operation"
                ]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "word_counter",
            "description": "Count words in a text.",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string"
                    }
                },
                "required": [
                    "text"
                ]
            }
        }
    }
]