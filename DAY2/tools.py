def calculator(a: float, b: float, operation: str):
    operation = operation.lower()

    if operation == "add":
        return a + b

    elif operation == "subtract":
        return a - b

    elif operation == "multiply":
        return a * b

    elif operation == "divide":
        if b == 0:
            return "Cannot divide by zero."
        return a / b

    return "Invalid operation."


def word_counter(text: str):
    return len(text.split())


def character_counter(text: str):
    return len(text)


AVAILABLE_TOOLS = {
    "calculator": calculator,
    "word_counter": word_counter,
    "character_counter": character_counter
}