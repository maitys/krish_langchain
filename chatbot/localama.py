#### Imports ####
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import os
import streamlit as st
from dotenv import load_dotenv

print(f"Conda environment: {os.getenv('CONDA_DEFAULT_ENV')}")

#### Load environment variables ####
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT") # for Langsmith tracking

#### Prompt Template ####
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI assistant. Please response to the user queries"),
        ("user", "Question: {question}"),
    ]
)

#### Streamlit App ####
st.title("Langchain Demo with OpenAI")
input_text = st.text_input("Search the topic you want")

# ollama LLAma2 LLM
llm=Ollama(model="llama2")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))