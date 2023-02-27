#incomplete

import sys

list = ['asd', 'a', 'asdfasdf']
list_len = []

for i in list:
    list_len.append(len(i))

print(list_len)

list.sort(key=len, reverse=True)

print(list)

for i in list:
    print(i)
