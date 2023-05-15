# 1. 퀘스트 번호를 입력한다.
# 2. everything 에서 해당 번호를 검색하여 파일을 찾는다.
# 3. 해당 퀘스트 xml 파일에서 <objective code= 을 찾아내 엑셀에 쓴다
# 4. desc= 내부의 숫자를 찾아 엑셀에 쓴다.

import pyautogui
import tkinter
import clipboard
import time
import keyboard
import threading

# everything = (3083,1413)
# excel = (3392,1415)

everything = pyautogui.locateOnScreen('everything.png', confidence=0.9)
excel = pyautogui.locateOnScreen('excel.png', confidence=0.7)
excel_first = pyautogui.locateOnScreen('excelfirst.png', confidence=0.7)
if excel_first == None:         # 인식이 안됐다면
    excel_first = (2698,456)

def check_input_esc():
    while True:
        if keyboard.is_pressed("esc"):
            break

def search_everything():
    id = questid.get()
    id = id + '*.xml'
    clipboard.copy(id)
    pyautogui.click(everything)
    pyautogui.hotkey('ctrl','f')
    pyautogui.hotkey('ctrl','v')
    pyautogui.keyDown('return')
    pyautogui.keyDown('return')
    time.sleep(1)
    pyautogui.hotkey('shift','alt','c')

def paste_excel(list_code, list_desc, list_region):
    pyautogui.click(excel)
    # check_input = threading.Thread(target=check_input_esc)
    # check_input.start()
    # check_input.join()                                        행 자동 추가로 인한 주석처리
    
    pyautogui.click(excel_first)
    for i in range(0,int(N.get())):
        pyautogui.keyDown('down')
    for i in range(0,2):
        pyautogui.keyDown('right')
    if int(N.get()) == 1:
        pyautogui.keyDown('down')    
    pyautogui.keyDown('down')               # 행 추가 위치 선정 완료
    
    for i in range(0,len(list_code)-1):       # 코드의 개수만큼 행 추가, 1은 이미 있기에 -1해줌
        pyautogui.hotkey('ctrl','shift','=')
        pyautogui.keyDown('r')
        pyautogui.press('enter')
        pyautogui.press(str(i+2))               # No. 숫자 입력
        pyautogui.press('enter')
    
    for i in range(0,len(list_code)):
        pyautogui.keyDown('up')
    pyautogui.keyDown('right')
    pyautogui.keyDown('right')              # 코드 위치 도착
    
    for i in range(0,len(list_code)):
        clipboard.copy(list_code[i])
        time.sleep(0.1)
        pyautogui.hotkey('ctrl','v')
        pyautogui.keyDown('right')
        
        clipboard.copy(list_desc[i])
        time.sleep(0.1)
        pyautogui.hotkey('ctrl','v')
        pyautogui.keyDown('right')
        pyautogui.keyDown('right')
        pyautogui.keyDown('right')
        
        clipboard.copy(list_region[i])
        time.sleep(0.1)
        if list_region[i] != 'r: x: y:':
            pyautogui.hotkey('ctrl','v')
        
        pyautogui.keyDown('down')
        pyautogui.keyDown('left')
        pyautogui.keyDown('left')
        pyautogui.keyDown('left')
        pyautogui.keyDown('left')      
    pyautogui.hotkey('ctrl','s')

def activate():
    search_everything()
    time.sleep(0.5)
    quest = open(clipboard.paste(), 'r', encoding='UTF-16 LE')
    # quest = open(r"Z:\Mabinogi\dev\release\asset\data\db\GameQuest\G14\295016_Lord_Of_Verona.xml", 'r', encoding='UTF-16 LE')
    lines = quest.readlines()
    list_code = []
    list_desc = []
    list_region = []
    for line in lines:
        if "<objective code=" in line:
            list_line = line.split('"')
            desc = [False, False]
            quest_desc = ''
            for alpha in list_line[3]:          # 진행방법 알아내기
                if desc[1]:
                    if alpha == ']':
                        break
                    else:
                        quest_desc += alpha
                else:
                    if desc[0]:
                        if alpha == '.':
                            desc[1] = True
                    else:
                        if alpha == '.':
                            desc[0] = True
            list_code.append(list_line[1])
            list_desc.append(quest_desc)
            list_region.append('r:' + list_line[5] + ' x:' + list_line[7] + ' y:' + list_line[9])
    # print(list_region)
    quest.close()
    paste_excel(list_code,list_desc,list_region)
    new_N = str(int(N.get())+1)
    N.delete(0,'end')
    N.insert(0, new_N)
        
def run(event):
    prev_mouse = pyautogui.position()
    prev_mouse = [prev_mouse.x, prev_mouse.y]
    if goal_id['state'] == 'disabled':
        activate()
    else:
        while int(goal_id.get()) >= int(questid.get()):
            activate()
            up()
    pyautogui.moveTo(prev_mouse[0],prev_mouse[1])

def up():
    new_questid = str(int(questid.get())+1)
    questid.delete(0,'end')
    questid.insert(0,new_questid)

def auto():
    if goal_id['state'] == 'disabled':
        goal_id.config(state='normal')
    else:
        goal_id.config(state='disabled')

# def exit_window():
#     while True:
#         if keyboard.is_pressed("esc"):
#             wd.quit()
#             break

# pyautogui.mouseInfo()
# check_esc = threading.Thread(target=exit_window)

# check_esc.start()

wd = tkinter.Tk()
wd.geometry("200x200")
wd.resizable(False,False)
wd.wm_attributes("-topmost", 1)

id_frame = tkinter.Frame()
id_frame.pack(side= 'top')

questid_label = tkinter.Label(id_frame,text= "퀘스트 ID")
questid_label.pack(side='top')
questid = tkinter.Entry(id_frame,width=10)
questid.bind("<Return>",run)
questid.pack(side='left')
up_button = tkinter.Button(id_frame,text= "증가",command=up)
up_button.pack(side='right')

questid_label = tkinter.Label(wd,text= "퀘스트 번호")
questid_label.pack()
N = tkinter.Entry(wd,width=10)
N.bind("<Return>",run)
N.pack()


auto_frame = tkinter.Frame()
auto_frame.pack(side= 'top')

auto_button = tkinter.Checkbutton(auto_frame,text= '자동',command= auto)
auto_button.pack(side='top')

goal_id = tkinter.Entry(auto_frame,width=10,state='disabled')
goal_id.bind("<Return>",run)
goal_id.pack(side='bottom')

wd.mainloop()
# activate(0)