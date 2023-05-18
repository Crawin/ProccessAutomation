from clipboard import copy
original ='''
'''
  
original = original.strip()
original = original.split('\n')

result = ''
for i in range(0,len(original)):
    if 'player.RemoveKeyword(`' in original[i]:
        temp = original[i].replace('player.RemoveKeyword(`','').replace('`);','').replace('\t','')
        result += temp + '\n'
copy(result)
print(result)