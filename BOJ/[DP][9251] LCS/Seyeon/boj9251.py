st1 = list(input())
st2 = list(input())

if len(st1)<len(st2):
    array1 = st1
    array2 = st2
else:
    array1 = st2
    array2 = st1

order = [0] * len(array1)
dp = [1] * len(array1)
result = 0

for i in range(len(array2)):
    if array1.count(array2[i]) == 0:
        array2[i] = 0

while array2.count(0)!=len(array2):
    for i in range(len(array1)):
        if array1[i] in array2:
            order[i] = (array2.index(array1[i]))+1
            array2[array2.index(array1[i])] = 0

            for q in range(len(array1)):
                if order[q] != 0:
                    for j in range(0,q):
                        if order[j]!=0 and order[j] < order[q]:
                            dp[q] = max(dp[q] , dp[j]+1)
            if result < max(dp):
                result = max(dp)
            dp = [1] * len(array1)

print(result)
