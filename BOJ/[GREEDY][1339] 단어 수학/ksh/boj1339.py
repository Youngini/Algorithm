import sys
n = int(sys.stdin.readline())
word = []
for i in range(n):
    word.append(list(sys.stdin.readline().strip('\n')))


print(len(word[0]))