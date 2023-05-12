import pyautogui
import time

everything = pyautogui.locateOnScreen('everything.png', confidence=0.9)
excel = pyautogui.locateOnScreen('excel.png', confidence=0.7)
excel_first = pyautogui.locateOnScreen('excelfirst.png', confidence=0.7)

print(everything)
print(excel)
print(excel_first)

# pyautogui.click(excel)
# list_code = [1,1,1]
# for i in range(0,len(list_code)-1):       # 코드의 개수만큼 행 추가
#     pyautogui.hotkey('ctrl','shift','=')
#     pyautogui.keyDown('r')
#     pyautogui.press('enter')

# pyautogui.keyDown('up')
# pyautogui.keyDown('right')
# pyautogui.keyDown('right')              # 코드 위치 도착

