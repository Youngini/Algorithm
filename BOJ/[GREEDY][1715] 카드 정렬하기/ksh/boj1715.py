import sys
n = int(sys.stdin.readline())
num_list = []
for i in range(n):
    num_list.append(int(sys.stdin.readline()))
num_list.sort()

queue=[]
sum = 0

if n==1:
    print(0)

else:
    queue.append(num_list[0]+num_list[1])
    
    i = 2
    while i+1<n:
        if queue[0]+num_list[i] < num_list[i]+num_list[i+1]:
            queue.append(queue[0]+num_list[i])
            sum+=queue.pop(0)
            i+=1
        else:
            queue.append(num_list[i]+num_list[i+1])
            i+=2
    #num_list에 원소가 1개로 남았을때
    if i == n-1:
        queue.append(queue[0]+num_list[i])
        sum+=queue.pop(0)
        
    #큐에 남은 원소 처리
    i = 0
    while len(queue)>1:
        sum+=queue[0]+queue[1]
        queue.append(queue[0]+queue[1])
        queue.pop(0)
        queue.pop(0)
    if len(queue)==1:
        sum+=queue.pop(0)

    print(sum)
