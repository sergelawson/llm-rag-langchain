import warnings
import os
from dotenv import load_dotenv
from fastapi import FastAPI   
from langserve import add_routes     

# Suppress Pydantic v1 compatibility warnings BEFORE importing langchain
warnings.filterwarnings("ignore", category=UserWarning)

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGSMITH_TRACING"]="true"
os.environ["LANGSMITH_ENDPOINT"]="https://api.smith.langchain.com"
os.environ["LANGSMITH_API_KEY"]= os.getenv("LANGSMITH_API_KEY")
os.environ["LANGSMITH_PROJECT"]="programming-language-learning-planner"

app = FastAPI(title="Langchain Server", version="1.0", description="API server for Langchain models")

model = ChatOpenAI(model_name="gpt-5-mini", temperature=1)

# Create a prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that will help me plan my learning of a programming language in 4 steps."),
    ("human", "{input}")
])

# Create a chain (Runnable) by piping prompt and model
chat = prompt | model

add_routes(
    app,
    chat,
    path="/chat"
    ) 

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)