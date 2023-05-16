from clipboard import copy
original =''''''
  
original = original.strip()
original = original.split('\n')

result = ''
for i in range(0,len(original)):
    if 'me.RemoveKeyword(`' in original[i]:
        temp = original[i].replace('me.RemoveKeyword(`','').replace('`);','').replace('\t','')
        result += temp + '\n'
copy(result)
print(result)