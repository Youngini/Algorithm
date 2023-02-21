import sys

n = int(sys.stdin.readline())
limits = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
boxes = list(map(int, sys.stdin.readline().split()))

limits.sort(reverse=True)
boxes.sort(reverse=True)

time = 0
if limits[0] < boxes[0]:
    print(-1)
    sys.exit()

while len(boxes)>0:
    for limit in limits:
        for box in boxes:
            if limit >= box:
                boxes.remove(box)
    time+=1
    
print(time)
