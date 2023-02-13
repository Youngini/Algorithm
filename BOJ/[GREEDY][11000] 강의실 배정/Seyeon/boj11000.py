import sys
n = int(sys.stdin.readline())

array = []

for i in range(n):
    array.append(list(map(int,sys.stdin.readline().split())))


for i in range(n):
    if array[i][0] == 0: continue
    for j in range(n):
        if j==i : continue
        if array[j][len(array[j])-1] == array[i][0]:
            array[j].append(array[i][len(array[i])-1])
            array[i][0] = 0
            
count = 0

for i in range(n):
    if array[i][0]!=0:
        count += 1

print(count)
