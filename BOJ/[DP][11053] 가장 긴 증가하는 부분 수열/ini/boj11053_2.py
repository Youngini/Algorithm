import sys
N = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split()]
dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i + 1, N):
        if(arr[j] > arr[i]):
            dp[j] = max(dp[i] + 1, dp[j])

print(max(dp))