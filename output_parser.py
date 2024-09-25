from langchain_openai import ChatOpenAI  # Updated import
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema import BaseOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

class AnswerOutputParser(BaseOutputParser):
    def parse(self, text: str):
        """Parse the output of an LLM call."""
        return text.strip().split("answer =")

# Initialize the chat model with the updated import
chat_model = ChatOpenAI(openai_api_key=api_key)

# Define the system template
template = """You are a helpful assistant that solves math problems and shows your work.
Output each step then return the answer in the following format: answer = <answer here>.
Make sure to output answer in all lowercase and to have exactly one space and one equal sign following it."""

human_template = "{problem}"

# Define the prompt
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template),
])

# Format the message using the new invocation method
messages = chat_prompt.format_messages(problem="2x^2 - 5x + 3 = 0")

# Use 'invoke' instead of 'predict_messages'
result = chat_model.invoke(messages)

# Parse the response from the AI model
parsed = AnswerOutputParser().parse(result.content)
steps, answer = parsed

print(answer)
