# 🎙️ My Custom Voice Assistant
---

# 🤖 Friday – Your Personal Voice Assistant

Welcome to **Friday**, a Python-powered voice assistant built for Windows! This assistant listens to your voice commands 🎤, processes them using Google’s speech recognition, and responds with natural-sounding speech 🗣️. Whether you want to open apps, search Wikipedia, or get the current time, Friday is ready to assist you — hands-free!

---

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
## ✨ Features

A simple voice assistant in Python that listens to your voice, understands basic commands, and speaks back to you. Works offline for TTS!
* 🎙️ **Voice Recognition**: Understands and processes your speech in real-time
* 🗣️ **Text-to-Speech**: Replies using a natural voice engine (via `pyttsx3`)
* 📚 **Wikipedia Integration**: Summarizes topics instantly
* ⏰ **Tells Time & Date**: Just ask for the current time or date
* 💻 **App/File Launcher**: Opens applications and documents on command
* 🧠 **Customizable Command Logic**: Easily extend with new voice actions

---

## 📸 Demo Screenshots
## 🛠️ Tech Stack & Dependencies

<p align="center">
  <img src="https://via.placeholder.com/600x300.png?text=Voice+Assistant+Screenshot+1" alt="Screenshot 1" width="400">
  <img src="https://via.placeholder.com/600x300.png?text=Voice+Assistant+Screenshot+2" alt="Screenshot 2" width="400">
</p>
Install these with `pip` if not already installed:

> Replace the image URLs above with your own screenshots!
```bash
pip install pyttsx3
pip install SpeechRecognition
pip install wikipedia
```

Built-in modules used:

* `datetime`
* `subprocess`
* `os`

---

## ⚡ Features
## 🚀 Installation & Setup

1. Clone the repo:

   ```bash
   git clone https://github.com/m2kush/VOICE-ASSISTANT-.git
   ```
2. Run the main file:

✅ Voice recognition via microphone  
✅ Text-to-speech responses  
✅ Tells current time on command  
✅ Custom greetings  
✅ Continuous command loop  
✅ Quickstart demo script (no mic needed)  
✅ Clean, modular code structure  
   ```bash
   python friday.py
   ```
3. Speak your command when prompted. Friday will listen, interpret, and respond!

---

## 📂 Project Structure
## 🧩 Packaging into .exe (Optional)

├── assistant.py # Handles text-to-speech
├── npl.py # Command processing
├── main.py # Main voice assistant loop
├── quickstart.py # Demo runner with sample commands
├── requirements.txt # Python dependencies
├── README.md # This file
├── credentials.json # (Optional dummy placeholder)
└── service_account.json # (Optional dummy placeholder)
Want to make Friday an executable?

1. Install PyInstaller:

   ```bash
   pip install pyinstaller
   ```
2. Create the executable:

   ```bash
   pyinstaller --onefile friday.py
   ```

   Find your `.exe` in the `dist/` folder.

---

## 🚀 Quickstart
## 🙌 Acknowledgements

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
Built using open-source Python libraries and the power of voice automation! Special thanks to Google Speech API, `pyttsx3`, and the Python community.

---

## 📬 Contact

Feel free to fork, enhance, or customize the project. If you have suggestions or run into issues, open an issue or drop a message!

🔗 [GitHub Repository](https://github.com/m2kush/VOICE-ASSISTANT-/tree/main)

---
