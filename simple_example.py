# This imports the ChatOpenAI class from the langchain.chat_models module.
# ChatOpenAI is a specific class in the langchain framework,
# designed to interact with the OpenAI GPT models, allowing users to send prompts and receive responses.
from langchain.chat_models import ChatOpenAI

# This imports the load_dotenv function from the dotenv library.
# dotenv is used to load environment variables from a .env file. This is useful for managing sensitive information (like API keys) without hardcoding them directly in the script. 
from dotenv import load_dotenv
# os allows interaction with the operating system, such as retrieving environment variables or accessing file paths.
import os

# This function call loads the environment variables defined in the .env file into the environment of the current running script.
load_dotenv()

# os.getenv() is used to retrieve the value of an environment variable.
# In this case, it retrieves the value of the API_KEY variable 
api_key = os.getenv("API_KEY")

# This line initializes an instance of the ChatOpenAI class and assigns it to the chat_model variable.
# openai_api_key=api_key passes the API key to authenticate requests to OpenAI's API.
chat_model=ChatOpenAI(openai_api_key=api_key)

# This calls the predict() method on the chat_model instance, 
# which sends the prompt "Hi!" to the OpenAI model.
# predict() is a method in ChatOpenAI that generates a response from the model based on the provided prompt.
result=chat_model.predict("Hi!")
print(result)