import sys
input = sys.stdin.readline

d, p, q = map(int, input().split())
if p < q:
    p, q = q, p
ret = (d+p-1)//p*p
for i in range(ret//p-1, -1, -1):
    newd = d - i*p
    cand = i*p+(newd+q-1)//q*q
    if cand == ret: break
    ret = min(ret, i*p+(newd+q-1)//q*q)
print(ret)