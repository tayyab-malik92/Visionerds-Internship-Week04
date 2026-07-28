import json


def print_header():

    print("\n" + "=" * 70)
    print("🤖 DAY 17 - ReAct AI Agent")
    print("=" * 70)


def print_reason(step, tool_name, arguments):

    print("\n" + "=" * 70)
    print(f"🤔 REASONING STEP {step}")
    print("=" * 70)

    print(f"\nModel decided to use tool: {tool_name}")

    print("\nArguments:")

    print(
        json.dumps(
            arguments,
            indent=4
        )
    )


def print_action(tool_name):

    print("\n" + "-" * 70)
    print("🔧 ACTION")
    print("-" * 70)

    print(f"Running '{tool_name}'...")


def print_observation(result):

    print("\n" + "-" * 70)
    print("👀 OBSERVATION")
    print("-" * 70)

    print(result)


def print_final(answer):

    print("\n" + "=" * 70)
    print("✅ FINAL ANSWER")
    print("=" * 70)

    print(answer)