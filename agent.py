import json

from config import client, MODEL, QUESTIONS, banner
from tools import TOOLS, TOOL_FUNCTIONS


SYSTEM_PROMPT = """
You are a college course-fee AI agent.

You have access to a private college course-fee database.

Never guess course fees.

Always use the get_course_fee tool when the user asks about
course fees.

Use the calculator tool for arithmetic.

Available course codes:
CS101
AI202
DS303

You can answer directly when no tool is required.
"""


def agent(question, max_steps=6):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": question
        }
    ]

    for step in range(1, max_steps + 1):

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            temperature=0
        )

        message = response.choices[0].message

        # No tool required
        if not message.tool_calls:

            return message.content or ""

        # Add assistant tool call
        messages.append(
            {
                "role": "assistant",
                "content": message.content or "",
                "tool_calls": [
                    {
                        "id": call.id,
                        "type": "function",
                        "function": {
                            "name": call.function.name,
                            "arguments": call.function.arguments
                        }
                    }
                    for call in message.tool_calls
                ]
            }
        )

        # Execute tools
        for call in message.tool_calls:

            name = call.function.name

            arguments = json.loads(
                call.function.arguments or "{}"
            )

            function = TOOL_FUNCTIONS.get(name)

            if function is None:

                result = f"Unknown tool: {name}"

            else:

                result = function(**arguments)

            print(
                f" step {step}: "
                f"{name}({arguments}) -> {result}"
            )

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": call.id,
                    "content": result
                }
            )

    return "Maximum agent steps reached."


if __name__ == "__main__":

    banner("SYSTEM 3: AI AGENT")

    for question in QUESTIONS:

        print("\nQ:", question)

        answer = agent(question)

        print("A:", answer)

        print("-" * 70)