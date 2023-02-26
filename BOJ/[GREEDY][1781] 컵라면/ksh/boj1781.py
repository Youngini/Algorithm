import sys
_input = sys.stdin.readline
n = int(_input())
arr=[]
solve=[0,]
count = []
for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)
    solve.append(i+1)
    count.append(0)

arr.sort(key=lambda x: (-x[1]))

def union_find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = union_find(parent,parent[x])
    return parent[x]


for i in range(n):
    arr_index = arr[i][0]
    index = union_find(solve,arr_index)
    if index==0:
        continue
    else:
        solve[index] = solve[index-1]
        count[index-1]=arr[i][1]

print(sum(count))