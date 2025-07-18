# 🧳 AI-Powered Trip Planner Assistant

An AI-powered travel assistant built with **LangChain**, **CrewAI**, and **Ollama** that automates the creation of travel plans tailored to your preferences. It uses multiple AI agents to search for travel data, plan itineraries, and generate markdown reports — all based on your destination and interests.

---

## 🚀 Project Overview

This project includes:

- ✅ 3 intelligent AI agents (Location Expert, Guide Expert, Planner Expert)
- 🔍 Web search integration with DuckDuckGo
- 🌐 Support for French-speaking countries (auto-detects and responds in French)
- 📄 Output in human-readable **Markdown** files (`.md`)
- 🎯 User input-driven: city, date, and interest-based travel customization

---

## 📁 Folder Structure

#### project-root/

│

├── ai_powered_trip_planner_assistant.py # ✅ Main script that runs all agents and tasks

├── city_report.md # 🏙️ Output report with hotel info, visa, weather, and transport 

├── guide_report.md # 📍 Output report with sightseeing, food, and events

├── travel_plan.md # 📅 Final compiled markdown travel plan with intro + itinerary

├── README.md # 📘 Project documentation (you’re reading this!)

└── requirements.txt # 📦 (Optional) List of dependencies if needed

---

## 🧠 AI Agents Breakdown

### 1. 🧭 City Local Guide Expert
- **Role:** Discover local attractions, experiences, and hidden gems
- **Model:** `ollama/qwen2.5:0.5b`
- **Tool:** DuckDuckGo web search
- **Output File:** `guide_report.md`

### 2. 🎯 Travel Trip Expert
- **Role:** Provide city info like visa rules, accommodations, weather, and transport
- **Model:** `ollama/qwen2.5:0.5b`
- **Tool:** DuckDuckGo search
- **Output File:** `city_report.md`

### 3. 📅 Travel Planner Expert
- **Role:** Merge data from both experts and create a full markdown travel plan
- **Model:** `ollama/qwen2.5:0.5b`
- **Output File:** `travel_plan.md`

---

## 🧾 Input Example

Defined inside the script:

```python
from_city = "Pakistan"
destination_city = "Dubai"
date_from = "1st March 2025"
date_to = "7th March 2025"
interests = "sight seeing and good food"

## 🔍 Web Search Tool
### The agents use a DuckDuckGo-based search tool:

*** from langchain_community.tools import DuckDuckGoSearchResults ***
This allows them to pull live information like visa rules, local events, and weather.

## ⚙️ How It Works
*** ✅ You define the travel details (city, dates, interests)

*** 🧠 The 3 AI agents activate and perform their roles

*** 📄 Each agent generates a .md report

** 💾 You get 3 output files:

city_report.md

guide_report.md

travel_plan.md

## ▶️ How to Run the Project
*** 1. Install Dependencies *** 
    pip install crewai langchain langchain_community langchain_ollama
*** 2. Install and Run Ollama (LLM Backend) ***
  Install Ollama and run:
#### ollama run qwen2.5:0.5b
Make sure ollama/qwen2.5:0.5b is available on your machine.

### 3. Run the Script
*** python ai_powered_trip_planner_assistant.py
📤 Output Details
🏙️ city_report.md
Hotel suggestions
Visa requirements
Transportation options
Weather forecast
Cost of living
📍 guide_report.md
Attractions
Local food
Seasonal events
Cultural spots

## 📅 travel_plan.md
**** A welcome section with city description ****

*** A daily itinerary with time breakdown ***

** Recommendations in markdown with emojis 😎 **

💡 Future Enhancements
✈️ Add flight APIs for live flight prices

🏨 Integrate hotel booking systems

🌍 Add a front-end using Streamlit or Flask

📄 Export .md reports as downloadable PDFs

📱 WhatsApp or Telegram chatbot interface

## 📦 Optional requirements.txt
crewai
langchain
langchain_community
langchain_ollama
To install:

## pip install -r requirements.txt
👨‍💻 Author
Anis Malik
AI Developer | LangChain Enthusiast | Travel + LLM Projects
🌍 GitHub: malikanas1818
📧 Email: malikanas4737@gmail.com

🏁 Final Note
This project is a perfect example of how LLMs can be used beyond chat to automate real-world tasks like travel planning.
