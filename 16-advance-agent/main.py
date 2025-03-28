import os
from dotenv import load_dotenv
import chainlit as cl
from agents import Agent , Runner , AsyncOpenAI ,OpenAIChatCompletionsModel
from typing import Optional , Dict 
from agents.tool import function_tool
import requests


load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)
model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=provider)


@cl.oauth_callback
def aouth_callback(
    provider_id:str,
    token:str,
    raw_user_data:Dict[str,str],
    default_user:cl.User,

) -> Optional[cl.User]:
    """ Handle the oAuth callback from Github
    Return the user object from if authentication is succesfull ,None otherwise"""


    return default_user


@function_tool("get_muskan_data")
def get_muskan_data() -> str:
    """
Fetches profile data about Muskan Fatima from her personal API endpoint.

This function makes a request to Muskan's profile API and returns information
about her background, skills, projects, education, work experience, and achievements.

Returns:
    str: JSON string containing Muskan Fatima's profile information.
"""


    try:
        response = requests.get("https://personal-api-orcin.vercel.app/profile")
        if response.status_code == 200:
            return response.text
        else:
            return f"Error fetching data: Status code {response.status_code}"
    except Exception as e:
        return f"Error fetching data: {str(e)}"
 
agent = Agent(
    name="Greeting agent",
    instructions="""Greeting Agent, Your task is to greet the user with a friendly message ,
     when someone say Aslam-alikum  or Hi you should reply  walikum-aslam from muskan when someone say Allah hafiz  or bye then say Allah hafiz 
     When users request information about Muskan fatima , use the get_muskan_data tool to retrieve and share his profile information
     For any questions not related to greetings or Muskan fatima , politely explain: 'I'm only able to provide greetings from muskan fatima . I can't answer other questions at this time.""",
    model=model,
    tools=[get_muskan_data]

)

@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history",[])
    await cl.Message(content="Hello! How can I help you today?").send()


@cl.on_message
async def handle_message(message:cl.Message):
    history = cl.user_session.get("history")
    history.append({"role":"user","content":message.content})
    
    result = await cl.make_async(Runner.run_sync)(agent, history)

    response_text = result.final_output

    await cl.Message(content=response_text).send()

    history.append({"role": "assistant", "content": response_text})
    cl.user_session.set("history", history)