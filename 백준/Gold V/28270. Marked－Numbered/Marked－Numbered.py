import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline

def dfs(idx):
    i = 1
    k = idx
    while k < n-1:
        while l[k] == l[k+1]:
            k += 1
            ret.append(i)
            i += 1
            if k+1 == n:
                return n
        ret.append(i)
        if l[k] - l[k+1] <= -2:
            print(-1)
            sys.exit(0)
        if l[k] < l[k+1]:
            k = dfs(k+1)
        else:
            return k
        k += 1
        i += 1
    ret.append(i)

n = int(input())
l = list(map(int, input().split()))
ret = []
dfs(0)
print(*ret)