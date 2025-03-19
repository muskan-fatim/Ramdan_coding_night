import chainlit as cl
import os
import google.generativeai as genai
from dotenv import load_dotenv
import chainlit as cl


load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(model_name="gemini-2.0-flash")


@cl.on_chat_start
async def chat_start():
    await cl.Message(content="How can I help I you today?").send()
@cl.on_message
async def main(message:cl.Message):
    prompt  = message.content
    response = model.generate_content(prompt)
    response_text = response.text if hasattr(response,"text") else ""      
    await cl.Message(content = response_text ).send()

    
