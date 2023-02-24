import sys
N = int(sys.stdin.readline())
weight_limit = [int(x) for x in sys.stdin.readline().split()]
M = int(sys.stdin.readline())
weight = [int(x) for x in sys.stdin.readline().split()]

weight_limit.sort(reverse=True)
weight.sort(reverse=True)
t, j = 0, 0

if(weight_limit[0] < weight[0]):
    t = -1

else:
    while(len(weight) != 0):
        t += 1
        for i in weight_limit:
            for j in weight:
                if(i >= j):
                    weight.remove(j)
                    break
                
print(t)