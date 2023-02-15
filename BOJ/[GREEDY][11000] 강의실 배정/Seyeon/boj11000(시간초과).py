import sys
n = int(sys.stdin.readline())

array = []

array.append(list(map(int, sys.stdin.readline().split())))

room = 1

for i in range(1,n):
    start, end = map(int, sys.stdin.readline().split())
    check = 0
    for j in range(len(array)):
        check += 1
        if array[j][1] <= start:
            array[j][0] = start
            array[j][1] = end
            break
    if check != i:
        room += 1
        array.append([start,end])
        
print(len(array))
