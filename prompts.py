import openai
import os

client = openai.Client(api_key=os.getenv("OPENAI_API_KEY"))


def get_ai_response(prompt):
    completion = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content
