import sys
input = sys.stdin.readline

n = int(input())
weight = list(map(int, input().split()))
weight.sort(reverse = True)

if weight[len(weight)-1] >= 2:
    print(weight[len(weight)-1]-1)
    sys.exit()

for i in range(weight.count(1)+1,sum(weight)):
    integer = i
    sub = 0
    for w in range(n):
        if weight[w] <= integer:
            if integer > sum(weight)-sub:
                print(i)
                sys.exit()
            
            integer -= weight[w]
        sub += weight[w]    
        if integer == 0:
            break

    if integer > 0:
        print(i)
        sys.exit()

print(sum(weight)+1)



