# 🤖 WhatsApp Auto-Reply Bot

An **AI-powered WhatsApp automation script** that reads your latest chat messages and automatically replies using **OpenAI’s GPT model**, all through **Python automation** with `pyautogui` and `pyperclip`.

---

## ⚡ Overview

The **WhatsApp Auto-Reply Bot** simulates human-like interactions by:

* Reading recent WhatsApp messages directly from your screen
* Analyzing chat history
* Generating context-aware replies using OpenAI’s GPT API
* Automatically pasting and sending the response in WhatsApp

It’s a creative demonstration of **AI + RPA (Robotic Process Automation)** working together for conversational automation.

---

## 🚀 Features

| Feature                        | Description                                                                                       |
| ------------------------------ | ------------------------------------------------------------------------------------------------- |
| 💬 **Auto Chat Reply**         | Automatically replies to incoming WhatsApp messages using GPT.                                    |
| 🧠 **Context-Aware AI**        | Generates smart, conversational responses based on full chat history.                             |
| 👩‍💻 **Personalized Persona** | Responds as “Jidnyasa Pawar” — a multilingual Indian coder fluent in Marathi, Hindi, and English. |
| 🖱️ **Full GUI Automation**    | Uses `pyautogui` for mouse clicks, drags, and keyboard control.                                   |
| 📋 **Clipboard Integration**   | Fetches and sends messages using `pyperclip`.                                                     |
| 🛡️ **Safety Mechanism**       | Skips auto-reply if the last sender is you (to prevent loops).                                    |

---

## 🧩 Tech Stack

| Technology            | Purpose                                 |
| --------------------- | --------------------------------------- |
| 🐍 **Python 3**       | Core programming language               |
| 🧠 **OpenAI GPT API** | Generates intelligent message replies   |
| 💻 **pyautogui**      | Simulates user mouse & keyboard actions |
| 📋 **pyperclip**      | Handles clipboard copying/pasting       |
| ⏱️ **time**           | Controls timing for reliable automation |

---

## ⚙️ Setup & Installation

Follow these steps to run the bot locally 👇

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Jid02/whatsapp-auto-reply-bot.git
cd whatsapp-auto-reply-bot
```

### 2️⃣ Install Dependencies

```bash
pip install pyautogui pyperclip openai
```

### 3️⃣ Add Your OpenAI API Key

In your script (or environment variable), replace with your API key:

```python
client = OpenAI(api_key="your_api_key_here")
```

### 4️⃣ Adjust Screen Coordinates

Before running, **update the mouse coordinates** in the code according to your screen layout.
Use:

```python
import pyautogui
print(pyautogui.position())
```

to find the positions for:

* WhatsApp window
* Chatbox
* Text selection area

### 5️⃣ Run the Script

```bash
python whatsapp_bot.py
```

You’ll have a few seconds to open your **WhatsApp Desktop** before the bot begins.

---

## 🧠 How It Works

1. The bot clicks and selects the chat text from WhatsApp using **screen coordinates**.
2. It copies the text via clipboard.
3. The chat history is sent to **OpenAI’s GPT model**.
4. The model generates a **natural, context-based reply**.
5. The bot pastes and sends the response automatically.

---

## 🔐 Important Notes

* ⚠️ **For educational and personal use only** — this is a demonstration of RPA + AI, not meant for spamming or unauthorized automation.
* 🖥️ Ensure **WhatsApp Desktop** is open and active before running.
* 🧭 You may need to tweak screen coordinates depending on your display resolution.
* 🔑 Never commit your API key to GitHub — store it safely in an `.env` file or environment variable.

---

## 🚀 Future Enhancements

* 💡 Add OCR (Optical Character Recognition) for reading chat directly from screenshots.
* 🧩 GUI configuration tool for setting coordinates visually.
* 🌐 Multi-chat support (auto-reply to multiple conversations).
* 🤖 Integration with WhatsApp Web APIs when officially supported.

---

## 👩‍💻 Developer

**Developed by:** [Jidnyasa Pawar](https://github.com/Jid02)

💬 Passionate about building creative AI-powered automation tools that blend intelligence with practicality.

---

## 📄 License

This project is licensed under the **MIT License** — you’re free to use, modify, and share responsibly.

---

## ⭐ Support

If you find this project helpful, please give it a **⭐ on GitHub** — it helps others discover it too!
