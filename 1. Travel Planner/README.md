# AutoGen Travel Planner

A multi-agent system for planning trips using AutoGen v0.4.

## Setup
1. Clone the repo.
2. Create a virtual environment: `python -m venv venv`.
3. Activate it: `venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows).
4. Install dependencies: `pip install -r requirements.txt`.
5. Set `OPENAI_API_KEY` in a `.env` file.

## Run
Run `python main.py` to start planning a trip.

## Structure
- `config/`: Settings and API keys.
- `agents/`: Agent definitions.
- `teams/`: Team workflows.
- `utils/`: Helper functions.
- `tests/`: Unit tests.
- `main.py`: Application entry point.