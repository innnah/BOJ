import sys, math
input = sys.stdin.readline

n = int(input())
arr_t = []
arr_d = []
for _ in range(n):
    a, b = input().rstrip().split()
    b = int(b)
    if a == 'T':
        arr_t.append(b)
    else:
        arr_d.append(b)
arr_t.sort()
arr_d.sort()
arr_t.append(1987654321)
arr_d.append(1000)
t, d = 0, 0
t_idx, d_idx = 0, 0
while d < 1000:
    if (arr_t[t_idx] - t) < (arr_d[d_idx] - d) * (t_idx+d_idx+1):
        d += (arr_t[t_idx] - t) / (t_idx+d_idx+1)
        t = arr_t[t_idx]
        t_idx += 1
    else:
        t += (arr_d[d_idx] - d) * (t_idx+d_idx+1)
        d = arr_d[d_idx]
        d_idx += 1
ft = math.floor(t)
if t - ft >= 0.5:
    print(ft+1)
else:
    print(ft)