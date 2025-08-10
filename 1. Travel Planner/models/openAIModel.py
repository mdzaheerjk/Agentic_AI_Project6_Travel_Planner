from config.settings import OPEN_API_KEY, MODEL, MAX_TURN, MAX_TURN_10, TERMINATION_WORD
from autogen_ext.models.openai import OpenAIChatCompletionClient

model_client = OpenAIChatCompletionClient(
    model = MODEL,
    openai_api_key = OPEN_API_KEY
)