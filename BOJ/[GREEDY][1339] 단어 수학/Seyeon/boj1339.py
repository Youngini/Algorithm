import sys

n = int(sys.stdin.readline())

alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
num = [0]*26 #알파벳에 숫자를 할당했는지 여부
check = [0]*10 #숫자를 사용했는지 여부

array = []
for i in range(n):
    array.append(list(sys.stdin.readline().strip('\n')))
    array[i].reverse()

array.sort(key=len,reverse = True)


for i in range(len(array[0])-1,-1,-1):
    for j in range(n):
        if len(array[j]) > i:
            if num[alpha.index(array[j][i])] == 0:
                for q in range(9,-1,-1):
                    if check[q] == 0:
                        check[q] = 1
                        num[alpha.index(array[j][i])] = q
                        break
total = 0

for i in range(n):
    array[i].reverse()
    temp = ""
    for j in range(len(array[i])):
        temp += str(num[alpha.index(array[i][j])])
    total += int(temp)
print(total)
