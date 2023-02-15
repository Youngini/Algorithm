import sys
import heapq
n = int(sys.stdin.readline())

array = []

for i in range(n):
    array.append(list(map(int, sys.stdin.readline().split())))

array.sort()

room = []
heapq.heappush(room,array[0][1])

for i in range(1,n):
    if array[i][0] < room[0]:
        heapq.heappush(room, array[i][1])

    else:
        heapq.heappop(room)
        heapq.heappush(room, array[i][1])
        
print(len(room))


    
            
    
    
    
