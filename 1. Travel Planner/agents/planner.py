from autogen_agentchat.agents import AssistantAgent
from models.openAIModel import model_client

planner_agent = AssistantAgent(
    name="Travel_Planner",
    description="A travel planner agent that helps users plan their trips.",
    model_client=model_client,
    system_message="You are a travel planner agent. Your task is to help users plan their trips by providing information about destinations, itineraries, and travel tips.",
)