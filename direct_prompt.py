from agent import agent

QUESTION = (
    "Which is cheaper: CS101 and AI202 with a 10% scholarship, "
    "or all three courses (CS101, AI202 and DS303) with a 25% scholarship? "
    "By how much?"
)

prompt = f"""
Answer the following question directly.
Give only the final answer without explaining your reasoning.

{QUESTION}

Course fees:
CS101 = Rs. 12,000
AI202 = Rs. 18,000
DS303 = Rs. 15,000
"""

answer = agent(prompt, max_steps=1)

print("=== DIRECT PROMPTING ===")
print("QUESTION:", QUESTION)
print()
print("ANSWER:", answer)