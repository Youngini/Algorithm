a = int(input())

dp = [1] * a

array = list(map(int, input().split()))

for i in range(1,a):
    for j in range(0,i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)
            
print(max(dp))
