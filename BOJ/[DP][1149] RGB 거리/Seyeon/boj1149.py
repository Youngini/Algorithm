n = int(input())

array = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for j in range(3)] for i in range(n)]

for i in range(3):
    dp[0][i] = array[0][i]

for i in range(1,n):
    for j in range(3):
        if j == 0:
            dp[i][j] = min(dp[i-1][1],dp[i-1][2]) + array[i][j]
        elif j == 1:
            dp[i][j] = min(dp[i-1][0],dp[i-1][2]) + array[i][j]
        else:
            dp[i][j] = min(dp[i-1][0],dp[i-1][1]) + array[i][j]

print(min(dp[n-1][0],dp[n-1][1],dp[n-1][2]))
