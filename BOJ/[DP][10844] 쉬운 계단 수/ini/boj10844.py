import sys

N = int(sys.stdin.readline())
dp = [[0 for _ in range(10)] for _ in range(N)]

for i in range(1, 10):
    dp[0][i] = 1

for i in range(1, N):
    for j in range(0, 10):
        if(j == 0):
            dp[i][j] = (dp[i - 1][j + 1])
        elif(j == 9):
            dp[i][j] = (dp[i - 1][j - 1])
        else:
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1])

ans = 0
for i in range(10):
    ans += dp[N-1][i]

print(ans%1000000000)
