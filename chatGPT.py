import openai
import os
from dotenv import load_dotenv

load_dotenv('./chatgpt.env')
CHATGPT_TOKEN = os.getenv('CHATGPT_TOKEN')

openai.api_key = CHATGPT_TOKEN

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role" : "system", "content": "You are a chatbot"},
        {"role" : "user", "content": "Why should DevOps engineer learn kubernetes?"}
    ]
)

result = ''
for choice in response.choices:
    result += choice.message.content

print(result)

