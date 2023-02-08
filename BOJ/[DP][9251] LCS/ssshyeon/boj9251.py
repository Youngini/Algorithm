str1 = input()
str2 = input()
len1 = len(str1)
len2 = len(str2)
dp = [0] * 1000

for i in range(len1):
    cnt = 0
    for j in range(len2):

        if cnt < dp[j]:
            cnt = dp[j]

        elif str1[i] == str2[j]:
            #cnt = cnt + 1
            dp[j] = cnt + 1
        

print(max(dp))