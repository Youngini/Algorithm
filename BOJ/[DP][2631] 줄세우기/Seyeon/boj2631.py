n = int(input())
array = [0] * n
dp = [1] * n

for i in range(n):
    array[i] = int(input())

for i in range(1,n):
    for j in range(0,i):
        if array[j] < array[i]:
            dp[i] = max(dp[i],dp[j]+1)
            
print(n-max(dp))
