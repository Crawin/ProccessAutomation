from clipboard import copy, paste
import tkinter
import threading
import time

def findItem(readlines):
    global find_item
    for item in readlines:
        if item_id in item:
            item_name_start = item.find('Text_Name1=')
            item_name_start += 1
            while item[item_name_start+len('Text_Name1=')] != '"':
                find_item += item[item_name_start+len('Text_Name1=')]
                item_name_start += 1
            find_item += ' '
    if find_item != '':
        return True
    else:
        return False
    
def set_result(read, b):
    global find_item, result
    find_item = find_item.split()
    if b:
        find_item = find_item[0].replace('_LT[xml.itemdb.','').replace(']','')
    else:
        find_item = find_item[0].replace('_LT[xml.itemdb_mainequip.','').replace(']','')
    item_start = read.find(find_item)
    temp = ''
    while read[item_start-1] != '\n':
        item_start -= 1
    while read[item_start] != '\n':
        temp += read[item_start]
        item_start+=1
    temp_split = temp.split()
    if temp_split[0] == find_item:
        temp = temp.replace(find_item,item_id.replace('ID="','').replace('"','')).replace('\t',' ')
    else:
        temp = item_id.replace('ID="','').replace('"','') + ' ****'
    result += temp
    result += '\n'

def run():
    global item_id, find_item, result, situation, clipboard, itemDB, items, item_txt, item_read, equipDB, equip_readlines, equip_txt, equip_read, resultboard
    original = clipboard.get('1.0','end')
    original = original.strip()
    original = original.split('\n')
    cnt = 0
    for i in range(0,len(original)):
        temp = original[i].replace('\t','')
        if temp[0] == '<' and temp[1] == '!' and temp[-2] == '-' and temp[-1] == '>':
            cnt+=1
        else:
            item_id = original[i].split()[1].upper()
            find_item = ''
            if findItem(items):
                set_result(item_read, True)
                cnt+=1
            elif findItem(equip_readlines):
                set_result(equip_read, False)
                cnt+=1
    if cnt == len(original):
        resultboard.delete('1.0','end')
        resultboard.insert(1.0, result)
        situation.config(text='성공')
        clipboard.delete('1.0','end')
        a = paste()
    else:
        situation.config(text='실패')
    copy(result)
    result = ''

def check_clipboard():
    global a, b, clipboard, temp_thread
    while True:
        try:
            temp_thread.join()
        except:
            b = paste()
            if a != b:
                clipboard.insert('end', b)
                clipboard.insert('end', '\n')
            a = b
            time.sleep(1)

def stop():
    global wd, itemDB,item_txt,equipDB,equip_txt
    itemDB.close()
    item_txt.close()
    equipDB.close()
    equip_txt.close()
    wd.destroy()
    
def run_thread():
    global situation, temp_thread
    situation.config(text='작동중')
    temp_thread = threading.Thread(target=run)
    temp_thread.daemon = True
    temp_thread.start()
    
a = paste()
b = ''
result = ''
temp_thread = threading.Thread(target=run)
temp_thread.daemon = True
itemDB = open(r'Z:\Mabinogi\dev\release\asset\data\db\ItemDB.xml','r', encoding='UTF-16 LE')
items = itemDB.readlines()
item_txt = open(r'Z:\Mabinogi\dev\release\asset\data\local\xml\ItemDB.korea.txt','r', encoding='UTF-16 LE')
item_read = item_txt.read()
equipDB = open(r'Z:\Mabinogi\dev\release\asset\data\db\ItemDB_MainEquip.xml', 'r', encoding='UTF-16 LE')
equip_readlines = equipDB.readlines()
equip_txt = open(r'Z:\Mabinogi\dev\release\asset\data\local\xml\ItemDB_MainEquip.korea.txt', 'r', encoding='UTF-16 LE')
equip_read = equip_txt.read()


wd = tkinter.Tk()
wd.wm_attributes("-topmost", 1)
wd.title('소지 아이템 검색')
wd.bind('esc', stop)

paste_clipboard = threading.Thread(target=check_clipboard)
paste_clipboard.daemon = True
# paste_clipboard.start()

text_frame = tkinter.Frame(wd)
text_frame.pack()

text_label_frame = tkinter.Frame(text_frame)
text_label_frame.pack(side='top')

search_label = tkinter.Label(text_label_frame, text= '검색창')
search_label.pack(side='left')

result_label = tkinter.Label(text_label_frame,text='결과창')
result_label.pack(side='right')

clipboard = tkinter.Text(text_frame)
clipboard.pack(side='left')

resultboard = tkinter.Text(text_frame)
resultboard.pack(side='right')

situation = tkinter.Label(wd, text='정지')
situation.pack()
run_button = tkinter.Button(wd, text='Run', command=run_thread)
run_button.pack()

wd.mainloop()