from collections import deque

for _ in range(int(input())):
    n,x = map(int, input().split())
    hs,ha,hb,hc = map(int, input().split())
    ws,wa,wb,wc = map(int, input().split())

    H, W = [0 for _ in range(n)], [0 for _ in range(n)]
    V = [0 for _ in range(n)]

    H[0] = hs % hc + 1
    W[0] = ws % wc + 1
    for i in range(1, n):
        H[i] = H[i-1] + 1 + (H[i-1] * ha + hb) % hc
        W[i] = (W[i-1] * wa + wb) % wc + 1
    for i in range(n):
        V[i] = H[i] * W[i]
    
    dq = deque([(V[0], H[0])])
    res = -1
    for i in range(1, n):
        while dq and H[i] - dq[0][1] > x:
            dq.popleft()
        if dq:
            res = max(res, dq[0][0] + V[i])
        while dq and dq[-1][0] <= V[i]:
            dq.pop()
        dq.append((V[i], H[i]))
    print(res)