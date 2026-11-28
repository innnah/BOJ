import sys
input = sys.stdin.readline

n = int(input())
d = {}
for i in range(n):
    s = input().rstrip()
    if d.get(s) == None:
        d[s] = (i, 1)
    else:
        d[s] = (d[s][0]+i, d[s][1]+1)
ans = []
for i in d.keys():
    ans.append([d[i][0]/d[i][1], i])
ans.sort()
for i in range(len(ans)):
    print(ans[i][1])