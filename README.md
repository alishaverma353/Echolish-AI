# Echolish – Personal Voice Agent 🔊🧠

**Echolish** is your intelligent, privacy-first personal voice assistant, designed to understand, respond, and assist using natural voice commands. With robust speech recognition, powerful natural language understanding via **LLaMA 3 (Ollama)**, and customizable skill modules, Echolish brings a truly personal AI to your desktop or device.

---

## 🚀 Features

- 🗣️ Speech-to-Text using Whisper, Vosk, or other engines  
- 🤖 Natural Language Understanding powered by **LLaMA 3 via Ollama**  
- 🔊 Text-to-Speech with realistic voice synthesis  
- 🧩 Modular Skill System for custom commands and actions  
- 🕵️‍♂️ 100% Privacy-First — offline-capable architecture  
- ⚙️ Extensible Plugin Support for developers  
- 🧠 Contextual Memory (optional)  
- 💻 Cross-platform: Linux, macOS, and Windows  

---

## 🧠 Powered by LLaMA 3 + Ollama

Echolish uses the **LLaMA 3 large language model**, running locally via [**Ollama**](https://ollama.com), to interpret and process voice commands with high accuracy and natural conversational flow.

### Why LLaMA 3 + Ollama?

- ✅ Fully local, no cloud dependency  
- ✅ Fast inference with GPU acceleration  
- ✅ State-of-the-art natural language reasoning  
- ✅ Easy model management using Ollama CLI  

Make sure Ollama is installed and running with LLaMA 3:
```bash
ollama run llama3


## 🛠 Installation

Follow these steps to set up Echolish on your system:

### 1. Clone the Repository
```bash
git clone https://github.com/alishaverma353/echolish.git
cd echolish

### 2. (Optional) Create a Virtual Environment

### 3. Install Dependencies

### 4. Ensure Ollama Is Running with LLaMA 3
Make sure you have Ollama installed. Then run:

bash
Copy code
ollama run llama3

### 5. Start Echolish
bash
Copy code
python main.py


##📦 Requirements
Python 3.8+

A microphone and speaker

Ollama installed with the llama3 model

Optional GPU for faster inference

Internet connection (only for optional features)

##🔌 Supported Skills (Examples)
Feature	Example Command
Weather	"What's the weather in Berlin today?"
Reminders	"Remind me to stretch at 4 PM."
Web Search	"Search GitHub Copilot tutorial."
System Tools	"Open Chrome" / "Mute the system volume"
Custom	Add your own in the skills/ directory


##🧩 Add Your Own Skills
Creating new skills is easy:

Create a new file in the skills/ directory, e.g., jokes.py

Define a function or class to handle specific intents

Register your skill in the dispatcher (if needed)

Test your skill by speaking the trigger phrase

Each skill can respond to custom phrases, use APIs, run commands, or trigger events.



##🛡️ Privacy First
Echolish is built with privacy in mind:

✅ No data is sent to the cloud unless explicitly configured

✅ Supports fully offline speech-to-text and TTS

✅ Local model options for all major tasks

✅ Configurable permissions and logging


##🤝 Contributing
Contributions are welcome!

Fork this repo

Create a new branch (feature/my-feature)

Commit your changes

Push to your fork

Create a Pull Request

Check CONTRIBUTING.md for coding guidelines and tips.


##📬 Contact
GitHub: @alishaverma353

Email: vermaalisha780@gmail.com


##🌟 Show Your Support
If you find Echolish useful, consider:

⭐ Starring the repository

🔁 Sharing it with others

💬 Providing feedback or suggestions

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
