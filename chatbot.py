from config import client, MODEL, QUESTIONS, banner


SYSTEM_PROMPT = """
You are a helpful college assistant.

Answer the user's questions clearly and briefly.

You do not have access to the college's private course-fee database.
If the user asks about course fees, answer based only on your general
knowledge and clearly state that the exact private fee data is unavailable.
"""


def chatbot(question):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content


if __name__ == "__main__":

    banner("SYSTEM 1: PLAIN CHATBOT")

    for question in QUESTIONS:

        print("\nQ:", question)

        answer = chatbot(question)

        print("A:", answer)

        print("-" * 70)