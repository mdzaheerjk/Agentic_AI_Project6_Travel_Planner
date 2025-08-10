from autogen_agentchat.agents import AssistantAgent
from models.openAIModel import model_client

research_agent = AssistantAgent(
    name="Researcher",
    description="A researcher agent that helps users find information and answer questions.",
    model_client=model_client,
    system_message="You are a researcher agent. Your task is to help users find information and answer questions by conducting research and providing relevant data.",
)