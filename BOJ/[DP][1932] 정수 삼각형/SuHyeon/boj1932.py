n = int(input())
arr = []
result = 0

for i in range(n):
    num_list = list(map(int, input().split()))
    arr.append(num_list)


for i in range(1,n):
    for j in range(i+1):
        if j==0:
            arr[i][j] = arr[i-1][0] + arr[i][j]
        elif j==i:
            arr[i][j] = arr[i-1][j-1] + arr[i][j]
        else:
            arr[i][j] = max(arr[i-1][j-1],arr[i-1][j]) + arr[i][j]

if n==1:
    result=num_list[0]
else:
    result = max(arr[n-1])


print(result)