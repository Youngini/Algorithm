import sys
from collections import deque
n, k = map(int,sys.stdin.readline().split())

init = list(map(int,sys.stdin.readline().split()))
init.sort()
array = deque(init)

count = 0
pivot = -1
diff = max(abs(array[0]),abs(array[len(array)-1]))

for i in range(len(array)-1):
    if array[i]<0 and array[i+1]>0:
        pivot = i
        break


i = len(array)-1
    
while i > pivot:
    count += abs(array[len(array)-1]) * 2
    for j in range(k):
        i -= 1
        array.pop()
        if i<=pivot:
            break

i = 0

while i <= pivot:
    count += abs(array[0]) * 2
    
    for j in range(k):
        i += 1
        array.popleft()
        if i > pivot:
            break

print(count-diff)


    
