import sys

n = int(sys.stdin.readline())
max_weight = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
boxes = list(map(int, sys.stdin.readline().split()))
boxes.sort()
max_weight.sort()

cnt = []
num = 0

if max_weight[n-1]<boxes[m-1]:
    print(-1)
else:
    for i in range(n):  #크레인 수 만큼
        for j in range(m/n):    
            if max_weight[i] < boxes[m/n*i+j]:
                cnt+=1
          

print(cnt)