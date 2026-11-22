def solve(n):
    if n <= 9: return max(n, 1)
    nxt = (n-9)//10
    ans = solve(nxt)*9
    for i in range(nxt*10+10, n+1):
        si = str(i)
        cand = 1
        for j in si:
            cand *= int(j)
        ans = max(ans, cand)
    return ans

n = int(input())
print(solve(n))