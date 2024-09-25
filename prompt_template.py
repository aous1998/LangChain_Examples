# Import the os module, which allows interaction with the operating system, 
# such as retrieving environment variables or managing files.
import os

# Import the ChatOpenAI class from the langchain.chat_models module.
# This class is used to interact with the OpenAI GPT models.
from langchain.chat_models import ChatOpenAI

# Import the ChatPromptTemplate class from langchain.prompts.chat module.
# This class allows you to define and format multi-message prompts that can be passed to the chat model.
from langchain.prompts.chat import ChatPromptTemplate

# Import the load_dotenv function from the dotenv package.
# This function loads environment variables from a `.env` file into the environment, 
# so you can access things like API keys without hardcoding them in your script.
from dotenv import load_dotenv

# Call the load_dotenv function to load the environment variables from the `.env` file into the current script.
load_dotenv()

# Retrieve the value of the "OPENAI_API_KEY" environment variable using os.getenv().
# This API key is needed to authenticate with the OpenAI API.
api_key = os.getenv("OPENAI_API_KEY")

# Create an instance of the ChatOpenAI class, passing in the OpenAI API key as an argument for authentication.
chat_model = ChatOpenAI(openai_api_key=api_key)

# Define a system-level template string for the chat model that outlines the assistant's task.
# The assistant will translate text from one language to another.
template = "You are a helpful assistant that translates {input_language} to {output_language} the following text: {text}"

# Define a human-level template that contains only the text to be translated.
human_template = "{text}"

# Create a ChatPromptTemplate instance using the system and human templates.
# This method uses `from_messages()` to combine both system and human messages.
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),  # The system message that sets the context for the assistant.
    ("human", human_template),  # The human message that contains the text to be translated.
])

# Format the messages by passing in the specific languages (input and output) and the text that needs to be translated.
# The system message and human message will be filled with these variables.
messages = chat_prompt.format_messages(input_language="English", 
                                       output_language="French", 
                                       text="I love programming.")

# Use the chat_model to send the formatted messages to the OpenAI model and predict the result (translation).
result = chat_model.predict_messages(messages)

# Print the translated text by accessing the content of the result.
print(result.content)
