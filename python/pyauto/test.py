import pyautogui
import time

everything = pyautogui.locateOnScreen('everything.png', confidence=0.9)
excel = pyautogui.locateOnScreen('excel.png', confidence=0.7)
excel_first = pyautogui.locateOnScreen('excelfirst.png', confidence=0.7)

print(everything)
print(excel)
print(excel_first)

pyautogui.moveTo(everything)
time.sleep(1)
pyautogui.moveTo(excel)