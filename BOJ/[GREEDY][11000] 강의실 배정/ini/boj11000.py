import sys
N = int(sys.stdin.readline().split())
arr = [[int(x) for x in sys.stdin.readline().split()] for _ in range(N[0])]
arr.sort()

for i in range(N[0]):
    if(arr[i] > 0):
        B = i # 처음으로 양수되는 구간
        break

