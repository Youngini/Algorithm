import sys
N = int(sys.stdin.readline())

array = list(map(int, sys.stdin.readline().split()))

one = min(array)

two = 100 # 50 * 2 = 두 면의 최대 합 
three = 150 # 50 * 3 = 세 면의 최대 합

if N == 1: # N==1이라면 총 주사위 숫자 합에서 가장 큰 값을 뺀다.
    print(sum(array)-max(array))
    
else: # N>=2 일 때
    for i in range(6):
        three_list = []
        two_list = []
        for j in range(6):
            if i+j!=5 and i!=j:
                two_list.append([array[i]+array[j],j])
        two_list.sort()
        if two > two_list[0][0]:
            two = two_list[0][0]
        for q in range(6):
            for j in range(len(two_list)):
                if i+q!=5 and two_list[j][1]+q!=5 and i!=q and two_list[j][1]!=q:
                    three_list.append(two_list[j][0]+array[q])
        three_list.sort()
        if three > three_list[0]:
            three = three_list[0]

    print((three*4) + (two*(8*N - 12)) + (one*5*((N-2)**2)) +(one * 4* (N-2)))          
