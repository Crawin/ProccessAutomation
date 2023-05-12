import os
os.chdir("C:/Users/crawin/Desktop/컷신 대사 맞추기")
fileB = open("BlankB.txt",'r',encoding='UTF8')
fileC = open("BlankC.txt",'r',encoding='UTF8')
# fileB = open("npc1.txt",'r',encoding='UTF8')
# fileC = open("npc2.txt",'r',encoding='UTF8')
# fileB = open("test1.txt",'r',encoding='UTF8')
# fileC = open("test2.txt",'r',encoding='UTF8')
Blines = fileB.readlines()
Clines = fileC.readlines()

Wfile = open("resultver2.txt", 'w',encoding='UTF8')
# Wfile = open("resultnpc.txt", 'w',encoding='UTF8')
# Wfile = open("resulttest.txt", 'w',encoding='UTF8')
for B in Blines:
    BX = B.replace("\t","")
    BX = BX.replace(" ","")
    C = Clines.pop(0)
    CX = C.replace("\t","")
    CX = CX.replace(" ","")
    if BX in CX:
        pass
    else:
        for num in B:
            if num == "\t":
                break
            Wfile.write(num)
        if "\"" in CX and "\"" not in BX:
            Wfile.write("\t큰따옴표")
        if len(BX) > len(CX):
            Wfile.write("\t중복")
        Wfile.write("\n")