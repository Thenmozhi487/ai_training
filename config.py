import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

PROVIDER = os.getenv("PROVIDER", "groq")
MODEL = os.getenv("MODEL", "openai/gpt-oss-20b")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is missing in .env")


client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)


# Private college course-fee data
COURSE_FEES = {
    "CS101": 12000,
    "AI202": 18000,
    "DS303": 15000
}


QUESTIONS = [
    "What is the fee for AI202?",
    "What is the total fee for CS101 and AI202 after a 10% scholarship?",
    "Is DS303 more expensive than CS101, and by how much?",
    "Give me a two-line welcome message."
]


def banner(title):
    print("=" * 70)
    print(title)
    print("=" * 70)