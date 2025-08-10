
from autogen_agentchat.conditions import TextMentionTermination

from config.settings import TERMINATION_WORD
import json




def save_state(agent,filename):
    """
    Save the state of the agent to a file.
    """
    state = agent.save_state()
    with open(filename, "w") as f:
        json.dump(state, f)

def load_state(agent, filename):
    """
    Load the state of the agent from a file.
    """
    with open(filename, "r") as f:
        state = json.load(f)
    agent.load_state(state)

def get_termination_condition():
    """
    Get the termination condition for the agent.
    """
    text_mention_termination = TextMentionTermination(TERMINATION_WORD)
    return text_mention_termination
