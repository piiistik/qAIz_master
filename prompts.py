import openai
import os

client = openai.Client(api_key=os.getenv("OPENAI_API_KEY"))


def get_ai_response(prompt, should_print):
    if should_print:
        print(f"Sending prompt: {prompt}\n")
    completion = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    answer = completion.choices[0].message.content
    if should_print:
        print(f"Received answer: {answer}\n\n")
    return answer
