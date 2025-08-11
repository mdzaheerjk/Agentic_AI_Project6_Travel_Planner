# 🌍 Agentic AI Project 6: Travel Planner

![Python](https://img.shields.io/badge/Python-3.13%2B-brightgreen)
![Agentic AI](https://img.shields.io/badge/Agentic%20AI-Travel%20Planner-blue)
![Travel Planning](https://img.shields.io/badge/AI-Travel%20Planning-orange)
![License](https://img.shields.io/badge/License-GPL--3.0-orange)

A smart, agentic, end-to-end AI-powered travel planner platform. This project uses a modular multi-agent design to orchestrate custom travel plans, research destinations, and optimize itineraries using LLMs and integrated tools. Built for extensibility, real-world trip planning, and rapid experimentation.

> 📁 **Repository:** `Agentic_AI_Project6_Travel_Planner`

---

## 🚀 Project Highlights

- 🧳 **AI Trip Planning:**  
  Automatically researches destinations, builds itineraries, and suggests travel logistics.
- 🤖 **Multi-Agent Architecture:**  
  Specialized agent modules for planning, research, and collaboration.
- 🌐 **LLM-Powered Recommendations:**  
  Utilizes advanced language models for personalized suggestions and planning logic.
- 🏆 **Extensible Workflows:**  
  Easily add new agents, planning strategies, or sources for richer plans.
- 🧩 **User-Friendly:**  
  Designed for custom input, interactive planning, and integration with travel APIs.

---

## 🧠 Technical Stack

- **Python 3.13+**
- **AutoGen v0.4**
- **Agentic AI Patterns**
- **Modular agent, team, and tool abstractions**

---

## 🏗️ Project Structure

```bash
Agentic_AI_Project6_Travel_Planner/
├── main.py                        # Main entry point
├── requirements.txt
├── LICENSE
├── README.md
├── 1. Project Structure.ipynb
├── Project.ipynb
├── config/
│   ├── __init__.py
│   └── settings.py
├── agents/
│   ├── __init__.py
│   ├── planner.py
│   └── researcher.py
├── models/
│   ├── __init__.py
│   └── openAIModel.py
├── teams/
│   ├── __init__.py
│   └── travel_team.py
├── utils/
│   ├── __init__.py
│   └── utils.py
├── tests/
│   └── agents_test.py
└── __pycache__/
```

---

## ⚡ Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/mdzaheerjk/Agentic_AI_Project6_Travel_Planner.git
cd Agentic_AI_Project6_Travel_Planner
```

### 2. Set up a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure your API keys
- Set your `OPENAI_API_KEY` in a `.env` file in the project root.

### 5. Run the travel planner
```bash
python main.py
```

---

## 🧪 Example Usage

- **Plan a Trip:**  
  Launch the app and enter your travel preferences (destination, dates, interests) to get a full itinerary.
- **Custom Research:**  
  Use researcher agents to discover new places or optimize your route.
- **Extend Easily:**  
  Add support for new travel APIs, agents (e.g., for hotel, flight, weather), or custom planning modules.

---

## 🧩 Extensibility

- **Add More Agents:**  
  Implement agents for reviews, cost comparison, or group coordination.
- **Custom Planning Logic:**  
  Adapt or expand planners for different trip types (solo, family, business, adventure, etc).

---

## 📚 Documentation

See code comments and agent/team definitions for extension instructions and workflow details.

---

## ✍️ Author

**Mohammed Zaheeruddin**  
🎓 First-Year B.Tech Student | AI/ML & GenAI Enthusiast  
🏫 Shetty Institute of Technology, Gulbarga  
📧 info.zaheerjk@gmail.com

---

## 📜 License

This project is licensed under the **GPL-3.0 License** – see the LICENSE file for details.

---

#### Key Features:
1. Multi-agent, LLM-driven AI travel planning and research
2. Modular, extensible Python codebase for rapid adaptation
3. Add new agents or planning strategies as needed
4. Designed for real-world trip planning, learning, and experimentation
