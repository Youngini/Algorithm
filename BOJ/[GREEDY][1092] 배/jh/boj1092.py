import sys
input = sys.stdin.readline

N = int(input())
crain = list(map(int,input().split()))
M = int(input())
weight = list(map(int,input().split()))
#crain.append(1000001)
crain.sort(reverse=True)
weight.sort(reverse=True)
# crain = sorted(crain,reverse=True)
# weight = sorted(weight,reverse=True)

time = 0

if (crain[0]<weight[0]):
    print(-1)
else:
    i = -1
    while(weight):
        i = (i+1)%(N)
        if(i==0):
            #i+=1
            time+=1
        for j in range(0,len(weight)):
            if (crain[i]>=weight[j]):
                del weight[j]
                break

    print(time)
