from autogen_agentchat.teams import RoundRobinGroupChat

# Agents
from agents.planner import planner_agent
from agents.researcher import research_agent

from config.settings import TERMINATION_WORD
from utils.utils import get_termination_condition

team = RoundRobinGroupChat(
    participants=[planner_agent, research_agent],
    system_message="You are a travel planning team. Your task is to help users plan their trips by providing information about destinations, itineraries, and travel tips.",
    termination_condition=get_termination_condition()
)