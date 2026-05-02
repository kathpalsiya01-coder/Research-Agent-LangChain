# 🔍 Research Agent

An AI-powered research agent that searches the web in real-time
and delivers structured, accurate reports on any topic.

Built with LangChain, Groq, and Tavily Search.

---

## 🎯 What It Does

- Takes any research topic as input
- Autonomously searches the web using Tavily
- Reasons over multiple sources
- Delivers a clean, structured research report

No manual googling. No copy-pasting.
Just ask — the agent thinks and answers.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| LangChain | Agent framework and orchestration |
| Groq (llama3-70b) | LLM for reasoning and tool calling |
| Tavily Search API | Real-time web search for agents |
| Streamlit | Frontend UI |
| Python-dotenv | API key management |

---

## 🚀 How To Run

### 1. Clone the repo
git clone https://github.com/kathpalsiya01-coder/Research-Agent-LangChain.git
cd Research-Agent-LangChain

### 2. Create virtual environment
conda create -n research-agent python=3.12
conda activate research-agent

### 3. Install dependencies
pip install -r requirements.txt

### 4. Add your API keys
Create a .env file:
GROQ_API_KEY=your_groq_key_here
TAVILY_API_KEY=your_tavily_key_here

### 5. Run the app
streamlit run app.py

---

## 🧠 Concepts Covered

- LangChain AgentExecutor
- Tool calling with LLMs
- Real-time web search integration
- Agentic reasoning loop (Observe → Think → Act)
- Streamlit UI with session state

---

## 📁 Project Structure

project1/
├── agent.py          # Core agent logic
├── app.py            # Streamlit UI
├── requirements.txt  # Dependencies
├── .env              # API keys (not pushed)
└── .gitignore        # Ignores .env and venv

---

## 🔑 Get API Keys

- Groq API → https://console.groq.com
- Tavily API → https://app.tavily.com

---

Built by Siya Kathpal | Undergraduate AI Engineer
