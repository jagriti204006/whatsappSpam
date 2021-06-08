import pyautogui
import time
import webbrowser as wb
wb.open("https://web.whatsapp.com/")
time.sleep(5) # after 5 sec it will start executing 

# it will open whatsapp and you just click on the chatbox you want to spam
for i in range(100):
    pyautogui.press("K")
    pyautogui.press("K")
    pyautogui.press("R")
    pyautogui.press("H")
    pyautogui.press("enter")