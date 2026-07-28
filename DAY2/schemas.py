TOOLS = [

    # ---------------------------------------------------
    # Calculator Tool
    # ---------------------------------------------------
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
                        "description": "Arithmetic operation",
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

    # ---------------------------------------------------
    # Word Counter
    # ---------------------------------------------------
    {
        "type": "function",
        "function": {
            "name": "word_counter",
            "description": "Count the number of words in a text.",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": "Input text"
                    }
                },
                "required": [
                    "text"
                ]
            }
        }
    },

    # ---------------------------------------------------
    # Character Counter
    # ---------------------------------------------------
    {
        "type": "function",
        "function": {
            "name": "character_counter",
            "description": "Count total number of characters including spaces.",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": "Input text"
                    }
                },
                "required": [
                    "text"
                ]
            }
        }
    }

]