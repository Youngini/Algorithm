import sys
n = int(sys.stdin.readline())
arr = []
room = []
cnt = 1

for i in range(n):
    time = list(map(int,sys.stdin.readline().split()))
    arr.append(time)

arr.sort(key=lambda x: (x[0]))

room.append(arr[0][1])


for i in range(1,n):
    flag = 1
    for j in range(cnt):
        if (room[j] <= arr[i][0]):
            room[j] = arr[i][1]
            flag = 0
            break;
    if flag==1:
        room.append(arr[i][1])
        cnt+=1

print(cnt)