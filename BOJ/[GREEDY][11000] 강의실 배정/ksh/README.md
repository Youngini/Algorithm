#시간초과... n제곱인데 왜 안되지
import sys
n = int(sys.stdin.readline())
arr = []
room = []
cnt = 1

for i in range(n):
    time = list(map(int,sys.stdin.readline().split()))
    arr.append(time)

arr.sort(key=lambda x: (x[1], x[0]))

room.append(arr[0])


for i in range(1,n):
    flag = 1
    for j in range(cnt):
        if (room[j][1] <= arr[i][0]):
            room[j] = arr[i]
            flag = 0
            break;
    if flag==1:
        room.append(arr[i])
        cnt+=1

print(cnt)