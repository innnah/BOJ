def solve(n):
    if n <= 2: return []
    if n in visited: return []
    visited.append(n)
    sqrtn = int(n**0.5)
    if sqrtn**2 != n:
        sqrtn += 1
    x, y = sqrtn, sqrtn**2-n
    ans = []
    ans += solve(x)
    ans += solve(y)
    ans.append((x, y))
    return ans

n = int(input())
visited = []
ret = solve(n)
for i in ret:
    print(*i)