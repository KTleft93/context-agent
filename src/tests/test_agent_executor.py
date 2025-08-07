# tests/test_agent_creator.py
import pytest
from unittest.mock import MagicMock, patch
from src.agents.agent_executor import create_agent

@patch('src.agents.agent_executor.ChatOpenAI')
@patch('src.agents.agent_executor.create_conversational_retrieval_agent')
def test_create_agent(mock_create_agent, mock_chat_openai):
    mock_llm_instance = MagicMock()
    mock_chat_openai.return_value = mock_llm_instance

    mock_agent = MagicMock()
    mock_create_agent.return_value = mock_agent

    tools = ['tool1', 'tool2']
    prompt = "Test prompt"

    agent = create_agent(tools, prompt)

    mock_chat_openai.assert_called_once_with(temperature=0)
    mock_create_agent.assert_called_once_with(
        llm=mock_llm_instance,
        tools=tools,
        memory_key='chat_history',
        custom_prompt=prompt,
        verbose=True
    )
    assert agent == mock_agent
