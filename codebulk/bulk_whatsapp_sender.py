import pyautogui
import time
import pyperclip

# Load contacts
with open("contacts.txt", "r", encoding="utf-8") as file:
    contacts = [line.strip() for line in file if line.strip()]

# Load message (with Urdu text)
with open("message.txt", "r", encoding="utf-8") as file:
    message = file.read().strip()

# Get mouse position over WhatsApp search bar
print("👉 Move your mouse over the WhatsApp SEARCH BAR. You have 5 seconds...")
time.sleep(5)
search_bar_position = pyautogui.position()
print(f"📍 Search bar position: {search_bar_position}")

print("⚠️ Script will start in 5 seconds. DO NOT touch the keyboard or mouse.")
time.sleep(5)

for name in contacts:
    # Click the search bar
    pyautogui.moveTo(search_bar_position)
    pyautogui.click()
    time.sleep(1)

    # Type name
    pyautogui.typewrite(name, interval=0.05)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(2)

    # Copy message and paste using clipboard
    pyperclip.copy(message)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)
    pyautogui.press("enter")

    print(f"✅ Sent to: {name}")
    time.sleep(1.5)



