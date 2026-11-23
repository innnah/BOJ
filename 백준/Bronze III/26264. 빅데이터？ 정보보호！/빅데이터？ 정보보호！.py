import sys
input = sys.stdin.readline

n = int(input())
s = input().rstrip()
idx = 0
bigdata, security = 0, 0
for _ in range(n):
    if s[idx] == 's':
        idx += 8
        security += 1
    else:
        idx += 7
        bigdata += 1
if bigdata >= security:
    print("bigdata?", end = ' ')
if security >= bigdata:
    print("security!")