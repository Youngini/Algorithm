import sys

N = int(sys.stdin.readline())
arr = []
for i in range(N):
    arr.append( [int(x) for x in sys.stdin.readline().split()])

dp = [[0 for _ in range(3)] for _ in range(N)]
dp[0] = arr[0]

for i in range(1,N):
    for j in range(3):
        dp[i][j] = min(dp[i-1][(j+1)%3],dp[i-1][(j+2)%3]) + arr[i][j]
        
print(min(dp[N-1]))