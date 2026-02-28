import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_resume(text: str):

    prompt = f"""
    Analyze the following resume and provide:
    1. Skills detected
    2. Strengths
    3. Improvement suggestions
    4. Suggested job roles

    Resume:
    {text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content