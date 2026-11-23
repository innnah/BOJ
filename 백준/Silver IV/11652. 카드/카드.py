import sys

input = sys.stdin.readline

n = int(input())
l = [int(input()) for _ in range(n)]
l.sort(reverse = True)
dic = {}

for i in l:
    if dic.get(i) == None:
        dic[i] = 1
    else:
        dic[i] += 1

maxnum = 0
biggest = 0
for a, b in dic.items():
    if biggest <= b:
        maxnum = a
        biggest = b

print(maxnum)