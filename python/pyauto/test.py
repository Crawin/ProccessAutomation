import pyautogui

excel_first = pyautogui.locateOnScreen('excelfirst.png', confidence=0.7) # 인식이 안됨
print(excel_first)
if (excel_first == None):
    print("음슴")