import pandas

excel = pandas.read_excel(r'C:\Users\crawin\Desktop\test.xlsx',sheet_name=None, engine='openpyxl')
result = open('python\RP 수정 모음 던전test.txt','w')
# ''''Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10',
#       part          No.           ID           Name            No.          Name          Code         진행방법        Name       Location         Region
#
#    'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14', 'Unnamed: 15', 'Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20'
#      xmlName        대화mint        kwd획득        kwd제거       Item획득        Item제거       컷신Name   컷신 종료 후 호출     deskCAT          RP'''

excel = pandas.read_excel(r'C:\Users\crawin\Desktop\G1부터 리스트업\C6C7_메인스트림_진행정보_수정중.xlsx',sheet_name=None, engine='openpyxl')
sheets = list(excel.keys())
num = 0
for sheet in sheets:
    print(f"=============================== {sheet} ===============================")
    try:
        if excel[sheet]['Unnamed: 20'][7] == 'RP ':
            # try:
                row = len(excel[sheet]['Unnamed: 20'])
                for i in range(0,row):
                    if type(excel[sheet]['Unnamed: 20'][i]) is str and excel[sheet]['Unnamed: 20'][i] != 'RP ':
                        # result.write(f"{i+2}:\t{excel[sheet]['Unnamed: 20'][i]}\t{excel[sheet]['Unnamed: 12'][i]}\n")
                        # print(f"{i+2}:\t{excel[sheet]['Unnamed: 20'][i]}\t{excel[sheet]['Unnamed: 12'][i]}")
                        
                        if '\n' in excel[sheet]['Unnamed: 12'][i]:
                            addresses = excel[sheet]['Unnamed: 12'][i]
                            addresses = addresses.split('\n')
                            for address in addresses:
                                if "data\script\dungeon" in address.lower():
                                    result.write(f"{num}\t{sheet}\t{i+2}\t{excel[sheet]['Unnamed: 20'][i]}\t{address}\n")
                                    # print(f"{num}. {sheet} - {i+2}:\t{excel[sheet]['Unnamed: 2'][i]}\t{excel[sheet]['Unnamed: 20'][i]}\t{address}\n")
                                    num += 1
                        else:
                            result.write(f"{num}.\t{sheet}\t{i+2}\t{excel[sheet]['Unnamed: 20'][i]}\t{excel[sheet]['Unnamed: 12'][i]}\n")
                            # print(f"{num}. {sheet} - {i+2}:\t{excel[sheet]['Unnamed: 2'][i]}\t{excel[sheet]['Unnamed: 20'][i]}\t{excel[sheet]['Unnamed: 12'][i]}\n")
                            num += 1
                        
                        # result.write(f"{num}. {sheet} - {i+2}:\t{excel[sheet]['Unnamed: 20'][i]}\t{excel[sheet]['Unnamed: 12'][i]}\n")
                        # num += 1
            # except:
            #     print('error')
        else:
            print("['Unnamed: 20'][7] 가 RP가 아니다.")
    except:
        print("['Unnamed: 20'][7] 가 없다.")
result.close()