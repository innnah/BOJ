def solve(c, s, a, b):
    if s == 1:
        c1 = (c+1)//2
    else:
        c1 = c // 2
    if n-c+c1 >= m:
        val = s + (m-(n-c)-1) * 2
        print(a*val+b)
        exit(0)
    c2 = c - c1
    solve(c2, ((c%2)^(s-1)) + 1, a*2, b-a*(s==2))

n, m = map(int, input().split())
print(solve(n, 1, 1, 0))