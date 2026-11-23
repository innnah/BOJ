def solve(target, s = 0):
    if target == s: return 1
    if target < s: return 0
    return solve(target, s+1) + solve(target, s+2) + solve(target, s+3)

n = int(input())
for _ in range(n):
    print(solve(int(input())))