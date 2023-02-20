import sys

n = int(sys.stdin.readline())
limit = [[0 for i in range(2)] for j in range(n)]

array = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    limit[i][0] = array[i]
    
limit.sort(reverse = True)

m = int(sys.stdin.readline())
weight = list(map(int, sys.stdin.readline().split()))
weight.sort(reverse = True)

i = 0
q = 0
for i in range(m):
    limit.sort(reverse = True)
    if weight[i] <= limit[(i+n-q)%n][0]:
        limit[(i+n-q)%n][1] += 1
    else:
        for j in range((q+n)%n,(i+n-q)%n):
            if weight[i] <=limit[j][0]:
                limit[j][1] += 1
                q+=1
                break
    print(limit)

if limit[limit.index(max(limit,key = lambda x:x[1]))][1] == 0:
    print(-1)
else:
    print(limit[limit.index(max(limit,key = lambda x:x[1]))][1])
