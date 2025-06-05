from langchain.schema import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path="C:/Users/Gajalakshmi G/Documents/Gen-AI/.env")

# Fetch the OpenAI API key
openai_key = os.getenv("OPENAI_API_KEY")

# Make sure the API key is set
if not openai_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables")

# Define the model (e.g., gpt-3.5-turbo)
llm_name = 'gpt-3.5-turbo'
model = ChatOpenAI(api_key=openai_key, model=llm_name)

# Define conversation messages
messages = [
    SystemMessage(content="You are a helpful assistant who is extremely competent as a computer scientist! Your name is Rob."),
    HumanMessage(content="What is a bit, and tell me your name.")
]

# Send the message and get a response
response = model.invoke(messages)

# Print the response content
print(response.content)
