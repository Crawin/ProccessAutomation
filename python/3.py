import os
os.chdir("C:/Users/crawin/Desktop/컷신 대사 맞추기")
fileB = open("npc1.txt",'r',encoding='UTF8')
fileC = open("npc2.txt",'r',encoding='UTF8')
Blines = fileB.readlines()
Clines = fileC.readlines()

Wfile = open("npcresult.txt", 'w',encoding='UTF8')

def write_differ(case, lineB, lineC):
    for i in lineB:
        if i == "\t":
            break
        Wfile.write(i)
        
    if case == 0:
        Wfile.write("\t글자 수 차이")
    if case == 1:
        Wfile.write("\t수치 차이\t")
        i = 0
        while i < len(lineB):
            if lineB[i] != lineC[i]:
                s = i
                e = i
                while lineB[s] >= '0' and lineB[s] <= '9':
                    s = s-1
                while lineB[e] >= '0' and lineB[e] <= '9':
                    e = e+1
                for n in range(s+1,e):
                    Wfile.write(lineB[n])
                i = e
            i = i+1
        Wfile.write("\t")
        i = 0
        while i < len(lineC):
            if lineB[i] != lineC[i]:
                s = i
                e = i
                while lineC[s] >= '0' and lineC[s] <= '9':
                    s = s-1
                while lineC[e] >= '0' and lineC[e] <= '9':
                    e = e+1
                for n in range(s+1,e):
                    Wfile.write(lineC[n])
                i = e
            i = i+1
    if case == 2:
        Wfile.write("\t오타\t")
        # for i in range(0,len(lineB)):
        #     if lineB[i] != lineC[i]:
        #         Wfile.write(lineB[i])
        # Wfile.write("\t")
        # for i in range(0,len(lineC)):
        #     if lineB[i] != lineC[i]:
        #         Wfile.write(lineC[i])
        i = 0
        while i < len(lineB):
            if lineB[i] != lineC[i]:
                s = i
                e = i
                while lineB[s] != ' ' and s > 0 and lineB[s] != '\t':
                    s = s-1
                while lineB[e] != ' ' and lineB[e] != '\n' and lineB[e] != '\t':
                    e = e+1
                for n in range(s+1,e):
                    Wfile.write(lineB[n])
                i = e
            i = i+1
        Wfile.write("\t")
        i = 0
        while i < len(lineC):
            if lineB[i] != lineC[i]:
                s = i
                e = i
                while lineC[s] != ' ' and s > 0 and lineC[s] != '\t':
                    s = s-1
                while lineC[e] != ' ' and lineC[e] != '\n' and lineC[e] != '\t':
                    e = e+1
                for n in range(s+1,e):
                    Wfile.write(lineC[n])
                i = e
            i = i+1
    if case == 3:
        Wfile.write("\t공백 차이")
        
    Wfile.write("\n")
    pass

for B in Blines:
    BX = B.replace("\t","")
    BX = BX.replace(" ","")
    C = Clines.pop(0)
    CX = C.replace("\t","")
    CX = CX.replace(" ","")
    if BX in CX:    # 모두 같으면 패스
        pass
    else:           # 뭔가가 다르다 0.글자수가 다르다 1. 수치가 다르다. 2. 글씨가 다르다
        if len(BX) != len(CX):  # 0. 공백을 제외한 글자수가 다르다
            write_differ(0, B,C)
            continue
        
        if len(B) != len(C):    # 공백을 제외한 글자수는 같지만 총 글자수는 다르다?
            write_differ(3,B,C)
            continue
        
        num = False             # 1. 수치가 다르다
        for i in range(0,len(B)):
            if B[i] != C[i]:
                if (B[i] >= '0' and B[i] <= '9') and (C[i] >= '0' and C[i] <= '9'): # 글자가 숫자라면
                    num = True
        
        if num:
            write_differ(1, B,C)
        else:
            write_differ(2, B,C)
            