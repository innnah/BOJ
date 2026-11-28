import sys
input = sys.stdin.readline

n = int(input())
rules = {}
for _ in range(n):
    c, _, *nxts = input().rstrip().split()
    rules[c] = nxts

s = input().rstrip()
for i in range(len(s)-1):
    if rules.get(s[i]) == None or s[i+1] in rules.get(s[i]):
        continue
    else:
        print("no")
        break
else:
    print("yes")