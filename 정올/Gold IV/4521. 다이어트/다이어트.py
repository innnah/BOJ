n = int(input())
mini = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]
ret = 987654321
ret_used = []
for i in range(2**n):
    p = [0, 0, 0, 0]
    cost = 0
    used = []
    for j in range(n):
        if i & (1 << j):
            for k in range(4):
                p[k] += a[j][k]
            cost += a[j][4]
            used.append(j+1)
    for i in range(4):
        if p[i] < mini[i]: break
    else:
        if ret > cost:
            ret = cost
            ret_used = [used.copy()]
        elif ret == cost:
            ret_used.append(used)
if ret != 987654321:
    print(ret)
    ret_used.sort()
    print(*ret_used[0])
else:
    print(-1)