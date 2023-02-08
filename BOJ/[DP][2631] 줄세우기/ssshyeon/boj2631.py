n = int(input())
num_list = []
for i in range(n):
    num_list.append(int(input()))


dp = [1] * n

for i in range(n):
    for j in range(i):
        if num_list[i]>num_list[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(n-max(dp))