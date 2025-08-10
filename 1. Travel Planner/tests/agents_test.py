import pytest


from agents.planner import planner_agent

def test_planner_agent():
    """
    Test the planner agent.
    """
    assert planner_agent.name == "Travel Planner"
    assert planner_agent.description == "A travel planner agent that helps users plan their trips."
    assert planner_agent.system_message == "You are a travel planner agent. Your task is to help users plan their trips by providing information about destinations, itineraries, and travel tips."

    