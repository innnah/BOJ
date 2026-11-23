import sys
input = sys.stdin.readline
ret = 1005
for _ in range(int(input())):
    a,b=map(int,input().split())
    if a<=b:ret=min(ret,b)
print(ret if ret!=1005else-1)