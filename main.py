import openai
import os
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat():
    print("Chatbot:Hello!Type 'bye' to exit")
    while True:
        user_input= input("You:")
        if user_input.lower=="bye":
            break
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"user","content":user_input}]
        )
        reply = response.choices[0].message.content
        print("chatbot",reply)

chat()
