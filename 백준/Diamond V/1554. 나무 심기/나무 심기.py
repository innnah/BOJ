import sys
input = sys.stdin.readline

MOD = 10**9
comb = [[0 for _ in range(502)] for _ in range(502)]
for i in range(502):
    comb[i][0] = 1
    for j in range(1, i+1):
        comb[i][j] = (comb[i-1][j-1] + comb[i-1][j]) % MOD

trees, width, height, dist = map(int, input().split())
if trees == 1:
    print((width+1)*(height+1) % MOD)
    sys.exit()
visited = [[0 for _ in range(height+1)] for _ in range(width+1)]
ans = 0
for i in range(width+1):
    for j in range(height+1):
        if i == 0 and j == 0: continue
        if visited[i][j]: continue
        tmp = 1
        while 1:
            if i*tmp > width or j*tmp > height: break
            visited[i*tmp][j*tmp] = 1
            tmp += 1
        cnt = [0 for _ in range(tmp+1)]
        for k in range(1, tmp+1):
            cnt[k] = (width-i*(k-1)+1) * (height-j*(k-1)+1)
        s = cnt[tmp]
        s2 = cnt[tmp]*2
        for k in range(tmp-1, 0, -1):
            cnt[k] -= s2
            s += cnt[k]
            s2 += s + cnt[k]
        
        empty = int((dist**2 // (i**2 + j**2))**0.5)
        if dist**2 % (i**2 + j**2) == 0 and (dist**2 // (i**2 + j**2))**0.5 == empty: empty -= 1
        #print(i, j, cnt, empty)
        s_ans = 0
        for k in range(1, tmp+1):
            if k-empty*(trees-1) >= 0:
                s_ans += cnt[k] * comb[k-empty*(trees-1)][trees]
                s_ans %= MOD
                #print(k, cnt[k] * comb[k-empty*(trees-1)][trees])
        if i != 0 and j != 0: s_ans *= 2
        ans += s_ans
        ans %= MOD
print(ans % MOD)