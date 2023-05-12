from difflib import context_diff

with open('공백 컷신 맞추기B.txt', 'r',encoding='UTF-8') as f1:
    with open('공백 컷신 맞추기C.txt', 'r',encoding='UTF-8') as f2:
        diff = context_diff(f1.readlines(), f2.readlines(), fromfile='f1', tofile='f2')
        for line in diff:
            print(line)
            