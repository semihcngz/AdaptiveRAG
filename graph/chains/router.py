from typing import Literal

from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

class RouteQuery(BaseModel):
    """
    Route a user query to the most relevant datasource.
    """

    datasource: Literal["vectorstore", "websearch"] = Field(
        ...,
        description="Given a user question choose a route it to web search or a vectorstore.",
    )

llm = ChatOpenAI(model='gpt-5-nano', temperature=0)
structured_llm_router = llm.with_structured_output(RouteQuery)

system = """
You are an expert at routing a user question to a vectorseach or web search.
The vektorsearch contains documents related to agents, prompt engineering and adversarial attacks.
Use the vectorsearch for questions on these topics. For all else use web search.
"""

route_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "{question}")
    ]
)

question_chain = route_prompt | structured_llm_router

if __name__ == "__main__":
    print(question_chain.invoke(
        {"question": 'how can i create an agent'}
    ))