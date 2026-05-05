import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_refactoring_suggestions(code, analysis):
    prompt = f"""
You are a senior software engineer.

Analyze and refactor this Python code:

CODE:
{code}

STATIC ANALYSIS:
{analysis}

Return:
1. Problems
2. Improved code
3. Short explanation
"""

    res = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )

    return res.choices[0].message.content
