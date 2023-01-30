n = int(input())
arr = []
val = 0

for i in range(n):
    cost = list(map(int, input().split()))  #공백을 기준으로 입력값 구분
    arr.append(cost)

for i in range(1,n):
    arr[i][0] = min(arr[i-1][1],arr[i-1][2])+arr[i][0]
    arr[i][1] = min(arr[i-1][0],arr[i-1][2])+arr[i][1]
    arr[i][2] = min(arr[i-1][0],arr[i-1][1])+arr[i][2]
    val = min(arr[i][0],arr[i][1],arr[i][2])
print(val)