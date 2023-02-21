import sys
n = int(sys.stdin.readline())
word = []
for i in range(n):
    word.append(list(sys.stdin.readline().strip('\n')))

dict = {}
for i in range(n):
    for j in range(len(word[i])):
        val = 10 ** (len(word[i])-j-1)
        if word[i][j] in dict:
            dict[word[i][j]] += val
        else:
            dict[word[i][j]] = val

sorted_dict = sorted(dict.items(), key=lambda x: -x[1])

ans=0
num=9
for i in range(len(sorted_dict)):
    ans += sorted_dict[i][1]*num
    num-=1

print(ans)