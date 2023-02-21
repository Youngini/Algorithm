import sys

n = int(sys.stdin.readline())
max_weight = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
boxes = list(map(int, sys.stdin.readline().split()))
boxes.sort(reverse=True)
max_weight.sort(reverse=True)

cnt = 0

if max_weight[0]<boxes[0]:
    print(-1)
else:
    while len(boxes)>0:
        cnt+=1 
        for i in range(n):
            if len(boxes)==0:
                break
            if max_weight[i] < boxes[-1]:
                continue
            for j in range(len(boxes)):
                if max_weight[i] >= boxes[j]:
                    boxes.pop(j)
                    break
        
    print(cnt)