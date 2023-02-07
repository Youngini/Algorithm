import sys
N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]
dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i + 1, N):
        if(arr[i] < arr[j]):
            dp[j] = max(dp[i] + 1, dp[j])

print(N - max(dp))