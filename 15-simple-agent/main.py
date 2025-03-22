import os 
from dotenv import load_dotenv
from agents import Agent , Runner , AsyncOpenAI ,OpenAIChatCompletionsModel
import streamlit as st
import asyncio


load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)
model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=provider)

agent = Agent(
    name="Greeting agent",
    instructions="Greeting Agent, Your task is to greet the user with a friendly message , when someone say Aslam-alikum  or Hi you should reply  walikum-aslam from muskan when someone say Allah hafiz  or bye then say Allah hafiz if somone say another thing say I am only for greeting you",
    model=model,

)


user_question = input("Enter your question or message")

if user_question:
    result = Runner.run_sync(agent,user_question) 
    print(result.final_output)