import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = list(input().rstrip())
arr = []
psum = 0
for i in range(n*2):
    psum += int(s[i]) * 2 - 1
    arr.append(psum)
nums_arr = [0 for _ in range(max(arr)-min(arr)+1)]
for i in range(n*2):
    nums_arr[arr[i]] += 1

max_val = max(arr)
min_val = min(arr)
if max_val - min_val <= m:
    print(0)
    sys.exit(0)
u = [0 for _ in range(max_val-min_val)]
v = [0 for _ in range(max_val-min_val)]

cnt = 0
c = nums_arr.copy()
for i in range(max_val-1, -1, -1):
    c[i-1] += c[i+1]
    cnt += c[i+1]
    c[i+1] = 0
    u[i] = cnt

cnt = 0
c = nums_arr.copy()
for i in range(min_val+1, 1):
    c[i+1] += c[i-1]
    cnt += c[i-1]
    c[i-1] = 0
    v[i] = cnt

ret = 10**20
for i in range(min_val, 1):
    if m+i >= 0:
        ret = min(ret, v[i] + u[m+i])
print(ret)