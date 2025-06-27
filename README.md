---

# 🤖 Friday – Your Personal Voice Assistant

Welcome to **Friday**, a Python-powered voice assistant built for Windows! This assistant listens to your voice commands 🎤, processes them using Google’s speech recognition, and responds with natural-sounding speech 🗣️. Whether you want to open apps, search Wikipedia, or get the current time, Friday is ready to assist you — hands-free!

---

## ✨ Features

* 🎙️ **Voice Recognition**: Understands and processes your speech in real-time
* 🗣️ **Text-to-Speech**: Replies using a natural voice engine (via `pyttsx3`)
* 📚 **Wikipedia Integration**: Summarizes topics instantly
* ⏰ **Tells Time & Date**: Just ask for the current time or date
* 💻 **App/File Launcher**: Opens applications and documents on command
* 🧠 **Customizable Command Logic**: Easily extend with new voice actions

---

## 🛠️ Tech Stack & Dependencies

Install these with `pip` if not already installed:

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

## 🚀 Installation & Setup

1. Clone the repo:

   ```bash
   git clone https://github.com/m2kush/VOICE-ASSISTANT-.git
   ```
2. Run the main file:

   ```bash
   python friday.py
   ```
3. Speak your command when prompted. Friday will listen, interpret, and respond!

---

## 🧩 Packaging into .exe (Optional)

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

## 🙌 Acknowledgements

Built using open-source Python libraries and the power of voice automation! Special thanks to Google Speech API, `pyttsx3`, and the Python community.

---

## 📬 Contact

Feel free to fork, enhance, or customize the project. If you have suggestions or run into issues, open an issue or drop a message!

🔗 [GitHub Repository](https://github.com/m2kush/VOICE-ASSISTANT-/tree/main)

---
