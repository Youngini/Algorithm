import sys
N = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split()]
dp = [[1 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(i + 1, N):
        for k in range(i, j):
            if(arr[k] < arr[j]):
                dp[i][j] = max(dp[i][j], dp[i][k] + 1)

print(max(max(dp)))