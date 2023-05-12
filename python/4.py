from random import randint as rand
Total_Rock = 0
Complete_Rock = 0
Complete_Reverse_Rock = 0

percent = 75

oneturn = 0
twoturn = 0
debturn = 0
buff1 = [0,0,0,0,0,0,0,0,0,0]   # 1은 성공 2는 실패
buff2 = [0,0,0,0,0,0,0,0,0,0]
debuff = [0,0,0,0,0,0,0,0,0,0]

def click(rock_num):
    global buff1, buff2, debuff, oneturn, twoturn, debturn, percent
    if rock_num == 1:
        if rand(0,100) <= percent:
            buff1[oneturn] = 1
            if percent > 25:
                percent = percent - 10
        else:
            buff1[oneturn] = 2
            if percent < 75:
                percent = percent + 10
        oneturn = oneturn + 1
    elif rock_num == 2:
        if rand(0,100) <= percent:
            buff2[twoturn] = 1
            if percent > 25:
                percent = percent - 10
        else:
            buff2[twoturn] = 2
            if percent < 75:
                percent = percent + 10
        twoturn = twoturn + 1
    else:
        if rand(0,100) <= percent:
            debuff[debturn] = 1
            if percent > 25:
                percent = percent - 10
        else:
            debuff[debturn] = 2
            if percent < 75:
                percent = percent + 10
        debturn = debturn + 1

while oneturn+twoturn+debturn < 30:
    # 내 방식
    if percent > 55:
        if oneturn < 10:
            click(1)
        else:
            if twoturn < 10:
                click(2)
            else:
                click(3)
    elif percent == 55:
        if twoturn < 10:
            click(2)
        else:
            click(1)
    else:
        if debturn < 10:
            click(3)
        else:
            click(2)


print(buff1)
print(buff2)
print(debuff)