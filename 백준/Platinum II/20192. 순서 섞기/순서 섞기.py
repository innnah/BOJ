import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = [a[0]]
for i in range(1, n):
    if b[-1] != a[i]:
        b.append(a[i])
if len(b) == 1:
    print(0)
    sys.exit(0)
ret = 0
for i in range(1, len(b)-1):
    if (b[i-1] < b[i] and b[i] > b[i+1]) or (b[i-1] > b[i] and b[i] < b[i+1]):
        ret += 1
ret += 1
if ret == 1:
    if b[0] < b[1]:
        print(0)
    else:
        print(1)
    sys.exit(0)
cnt = 0
flag = False
while ret > 1:
    if ret % 2:
        flag = True
    ret = (ret+1)//2
    cnt += 1
if b[0] > b[1] and b[-2] < b[-1] and not flag:
    cnt += 1
print(cnt)