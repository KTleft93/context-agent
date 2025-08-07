from langchain_openai import ChatOpenAI
from langchain.agents.agent_toolkits import create_conversational_retrieval_agent

def create_agent(tools, prompt):
    llm = ChatOpenAI(temperature=0)

    return create_conversational_retrieval_agent(
        llm=llm,
        tools=tools,
        memory_key='chat_history',
        custom_prompt=prompt,
        verbose=True
    )
