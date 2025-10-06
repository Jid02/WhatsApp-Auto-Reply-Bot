import pyautogui
import time
import pyperclip  # to access clipboard
from openai import OpenAI

client = OpenAI(
    api_key="**"
)

    # Wait a few seconds to give you time to switch to the screen
time.sleep(3)

    # Step 1: Click on the icon (WhatsApp window)
pyautogui.click(1639, 1412)
time.sleep(1)


while True:

    # Step 2: Drag to select text
    pyautogui.moveTo(662, 236)
    pyautogui.dragTo(1872, 943, duration=1, button='left')  # smooth drag

    # Step 3: Copy selected text (Ctrl+C)
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.5)
    pyautogui.click(1830, 820)

    # Step 4: Get text from clipboard
    chat_history = pyperclip.paste()
    print("Copied text:")
    print(chat_history)

    # --- Step 5: Check last message sender ---
    lines = [line.strip() for line in chat_history.split("\n") if line.strip()]
    if not lines:
        print("⚠️ No messages found.")
        continue

    last_message = lines[-1]
    print(f"Last message: {last_message}")

    try:
        sender_part = last_message.split("]")[1].split(":")[0].strip()
    except IndexError:
        sender_part = ""

    print(f"Detected sender: {sender_part}")

    if "Jidnyasa Pawar" in sender_part:
        print("✅ Last message is from Jidnyasa Pawar. Skipping reply.")
        continue  # skip to next loop iteration

    # --- Step 6: Generate a reply only if last sender is NOT Jidnyasa Pawar ---
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are person named Jidnyasa Pawar who speaks Marathi, Hindi as well as English. You are from India and you are a coder. You analyze chat history and respond like Jidnyasa Pawar. Output should be next chat response as (message only)"},
            {"role": "user", "content": chat_history}
        ]
    )

    response = completion.choices[0].message.content
    pyperclip.copy(response)  # copy text into clipboard

    # Step 7: Click at chatbox coordinates
    pyautogui.click(1234, 985)
    time.sleep(0.5)

    # Step 8: Paste text
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)

    # Step 9: Press Enter to send
    pyautogui.press("enter")
    print("✉️ Reply sent.")
