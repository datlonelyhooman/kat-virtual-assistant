# Kat – Virtual Assistant 🤖

Kat is a modular, command-line virtual assistant built in Python.  
It uses intent detection, task execution, and Wikipedia-based knowledge retrieval to answer user queries and perform basic actions.

This project demonstrates clean project architecture, modular design, and Git/GitHub workflow.

---

## ✨ Features

- Intent-based command handling
- Task execution (time, open browser, exit, greetings)
- Wikipedia-powered question answering
- Clean modular structure (`assistant`, `intents`, `tasks`)
- Beginner-friendly and easily extensible

---

## 🗂 Project Structure
kat_virtual_assistant/
├── main.py              # Entry point
├── requirements.txt     # Dependencies
├── README.md
└── src/
    ├── assistant.py     # Core assistant logic
    ├── intents.py       # Intent detection
    ├── tasks.py         # Task execution
    └── .gitignore


---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/datlonelyhooman/kat-virtual-assistant.git
cd kat-virtual-assistant

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run Kat
python main.py

💬 Example Interaction
KAT is online. Type 'exit' to quit.
You: time
KAT: The current time is 20:07:45

You: where is Japan
KAT: Japan is an island country in East Asia.

You: open google
KAT: Opening Google.

You: exit
KAT: Goodbye!


🧠 Technologies Used

Python 3

Wikipedia API

Git & GitHub

Modular programming principles

📌 Future Improvements

Live web search (Google/DuckDuckGo)

LLM integration (OpenAI / Gemini)

Voice input & output

GUI or web interface

👩‍💻 Author

Ria
Built as a learning-focused project to explore virtual assistants, intent handling, and clean software architecture.