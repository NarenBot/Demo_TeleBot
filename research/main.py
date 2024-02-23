# import openai
from dotenv import load_dotenv
import os

load_dotenv()

# Set your OpenAI API key
# openai.api_key = os.getenv("OPENAI_API_KEY")

# Generate a chat completion
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    response_format={"type": "json_object"},
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant designed to output JSON.",
        },
        {"role": "user", "content": "Who is Mahatma Gandhi?"},
    ],
)
print(response.choices[0].message.content)
