import sys, math

input = sys.stdin.readline
sys.setrecursionlimit(2147483647)

def gcd(l):
    def gcd2(a, b):
        while b != 0:
            a, b = b, a%b
        return a
    ret = l[0]
    for i in range(1, len(l)):
        ret = gcd2(ret, l[i])
    return ret

best = -1
def solution(l, g=0):
    global best
    if len(l) == 1:
        g += l[0]
        best = max(g, best)
        return
    solution(l[math.ceil(len(l)//2):], g+gcd(l[:math.ceil(len(l)//2)]))
    solution(l[:math.ceil(len(l)//2)], g+gcd(l[math.ceil(len(l)//2):]))

n = int(input())
l = list(map(int, input().split()))
solution(l)
print(best)