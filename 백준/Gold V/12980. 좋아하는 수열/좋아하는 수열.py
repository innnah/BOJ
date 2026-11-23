import sys
input = sys.stdin.readline

def solve(idx, l, taken):
    global ret
    if idx == len(empty):
        score = 0
        for i in range(n):
            for j in range(i+1, n):
                if l[i] < l[j]: score += 1
        if m == score: ret += 1
        return
    place = empty[idx]
    for i in range(1, n+1):
        if not taken[i]:
            taken[i] = 1
            l[place] = i
            solve(idx+1, l, taken)
            l[place] = 0
            taken[i] = 0

n, m = map(int, input().split())
l = list(map(int, input().split()))
empty = []
taken = [0 for _ in range(n+1)]
for i in range(n):
    if l[i] == 0:
        empty.append(i)
    else:
        taken[l[i]] = 1
ret = 0
solve(0, l, taken)
print(ret)