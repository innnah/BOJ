import sys

input = sys.stdin.readline

n = int(input())
l = [list(map(int, list(input().rstrip()))) for _ in range(n)]

def press(n, l):
    if n == 1:
        return str(l[0][0])
    
    ret = ""
    first = l[0][0]
    for i in range(n):
        for j in range(n):
            if first != l[i][j]:
                ret += "("
                ret += press(n//2, [l[k][:n//2] for k in range(n//2)])
                ret += press(n//2, [l[k][n//2:] for k in range(n//2)])
                ret += press(n//2, [l[k][:n//2] for k in range(n//2, n)])
                ret += press(n//2, [l[k][n//2:] for k in range(n//2, n)])
                ret += ")"
                return ret

    return str(first)

print(press(n, l))