from config import client, MODEL

QUESTION = (
    "Which is cheaper: CS101 and AI202 with a 10% scholarship, "
    "or all three courses (CS101, AI202 and DS303) with a 25% scholarship? "
    "By how much?"
)

prompt = f"""
Solve the following problem step by step.
Number each step and show the calculation.
After the steps, give the final answer.

{QUESTION}

Course fees:
CS101 = Rs. 12,000
AI202 = Rs. 18,000
DS303 = Rs. 15,000
"""

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=0
)

answer = response.choices[0].message.content

print("=== CHAIN-OF-THOUGHT ===")
print("QUESTION:", QUESTION)
print()
print("ANSWER:")
print(answer)