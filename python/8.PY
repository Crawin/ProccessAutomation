from clipboard import copy

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
    while read[item_start] != '\n':
        temp += read[item_start]
        item_start+=1
        temp = temp.replace(find_item,item_id.replace('ID="','').replace('"','')).replace('\t',' ')
    result += temp
    result += '\n'


original ='''
				<item id="15069" pocket="5" x="0" y="0" figure="0" bundle="0" col1="00FFFFFF" col2="00FFFFFF" col3="00FFFFFF" />
				<item id="17032" pocket="7" x="0" y="0" figure="0" bundle="0" col1="00563211" col2="00FCDCD5" col3="007DA834" />
				<item id="2010001" pocket="8" x="0" y="0" figure="0" bundle="0" col1="00625F44" col2="00C0C0C0" col3="00601469" />
				<item id="2030002" pocket="9" x="0" y="0" figure="1" bundle="0" col1="00CA7B34" col2="00B45031" col3="00DABC87" />
				<item id="40017" pocket="11" x="0" y="0" figure="0" bundle="0" col1="00DAC3BC" col2="00AACFC8" col3="00B16B4A" />
				<item id="51002" pocket="2" x="0" y="1" figure="0" bundle="10" col1="00AB0E2C" col2="00B4BDC2" col3="00745D2F" />
				<item id="51002" pocket="2" x="1" y="1" figure="0" bundle="10" col1="00AB0E2C" col2="00B4BDC2" col3="00745D2F" />
				<item id="51002" pocket="2" x="2" y="1" figure="0" bundle="10" col1="00AB0E2C" col2="00B4BDC2" col3="00625F44" />
				<item id="51012" pocket="2" x="3" y="1" figure="0" bundle="10" col1="00FFD800" col2="00B4BDC2" col3="00625F44" />
				<item id="63000" pocket="2" x="4" y="1" figure="0" bundle="10" col1="00808080" col2="00FFC3AA" col3="0099BB36" />
				<item id="51007" pocket="2" x="0" y="2" figure="0" bundle="10" col1="00004BB1" col2="00B4BDC2" col3="00746C54" />
				<item id="51007" pocket="2" x="1" y="2" figure="0" bundle="10" col1="00004BB1" col2="00B4BDC2" col3="00746C54" />
				<item id="51007" pocket="2" x="2" y="2" figure="0" bundle="10" col1="00004BB1" col2="00B4BDC2" col3="00746C54" />
				<item id="51007" pocket="2" x="3" y="2" figure="0" bundle="10" col1="00004BB1" col2="00B4BDC2" col3="00745D2F" />
				<item id="51007" pocket="2" x="4" y="2" figure="0" bundle="10" col1="00004BB1" col2="00B4BDC2" col3="007F7237" />
				<item id="60005" pocket="2" x="1" y="3" figure="0" bundle="10" col1="00CCC8AB" col2="00AAB06B" col3="00EA9A56" />
				<item id="60005" pocket="2" x="2" y="3" figure="0" bundle="10" col1="00CCC8AB" col2="00AAB06B" col3="00EA9A56" />
				<item id="60005" pocket="2" x="3" y="3" figure="0" bundle="10" col1="00CCC8AB" col2="00AAB06B" col3="00EA9A56" />
				<item id="60005" pocket="2" x="4" y="3" figure="0" bundle="10" col1="00CCC8AB" col2="00AAB06B" col3="00EA9A56" />
				<item id="73008" pocket="2" x="4" y="7" figure="0" bundle="0" col1="00808080" col2="00808080" col3="00808080" />
'''

original = original.strip()
original = original.split('\n')
itemDB = open(r'Z:\Mabinogi\dev\release\asset\data\db\ItemDB.xml','r', encoding='UTF-16 LE')
items = itemDB.readlines()
item_txt = open(r'Z:\Mabinogi\dev\release\asset\data\local\xml\ItemDB.korea.txt','r', encoding='UTF-16 LE')
item_read = item_txt.read()
equipDB = open(r'Z:\Mabinogi\dev\release\asset\data\db\ItemDB_MainEquip.xml', 'r', encoding='UTF-16 LE')
equip_readlines = equipDB.readlines()
equip_txt = open(r'Z:\Mabinogi\dev\release\asset\data\local\xml\ItemDB_MainEquip.korea.txt', 'r', encoding='UTF-16 LE')
equip_read = equip_txt.read()
result = ''
for i in range(0,len(original)):
    item_id = original[i].split()[1].upper()
    find_item = ''
    if findItem(items):
        set_result(item_read, True)
        print('item에 있었네')
    elif findItem(equip_readlines):
        set_result(equip_read, False)
        print('equip에 있었네')
    else:
        print('없는데?')
copy(result)
itemDB.close()
item_txt.close()
equipDB.close()
equip_txt.close()