import sys

n = int(sys.stdin.readline())

alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
num = [0]*10
check = [0]*10

array = []
for i in range(n):
    array.append(list(sys.stdin.readline().strip('\n')))
    array[i].reverse()

array.sort(key=len,reverse = True)
print(array)

for i in range(len(array[0])-1,-1,0):
    for j in range(n):
        if num[alpha.index(array[j][i])] == 0:
            for q in range(9,-1,0):
                if check[q] == 0:
                    check[q] = 1
                    num[alpha.index(array[j][i])] = q

total = 0

for i in range(n):
    for j in range(len(array[n]):
                   
                    
                
