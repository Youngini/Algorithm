import sys
N = int(sys.stdin.readline())
weight = [int(x) for x in sys.stdin.readline().split()]
weight.sort()
weight_set = {weight[0]}
ans = 1

for i in range(1, len(weight)):
    arr = list(weight_set)
    for j in arr:
        weight_set.add(weight[i] + j)

arr = list(weight_set)

for i in range(len(arr)):
    if(i + 1 != arr[i]):
        ans = i + 1
        break

print(ans)