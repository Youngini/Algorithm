n = int(input())

arr = [0,1,1,1,1,1,1,1,1,1]
dp = [[0 for j in range(10)] for i in range(n)]
dp[0]=arr
sum = 0

for i in range(1,n):
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]
    for j in range (1,9):
        dp[i][j] = dp[i-1][j-1]+dp[i-1][j+1]

for i in range(10):
    sum = sum + dp[n-1][i]

print(sum%1000000000)