import sys
input = sys.stdin.readline

def changebase(num, k):
    ret = []
    while num > 0:
        ret.append(num%k)
        num //= k
    return ret[::-1]
def sumF(num):
    l = changebase(num, 2)
    ret = [0 for _ in range(len(l))]
    ret[0] = num - 2 ** (len(l)-1) + 1
    ret[-1] = (num+1) // 2
    a = 2
    for i in range(len(l)-2, 0, -1):
        ret[i] += 2 ** (len(l)-2)
        ret[i] += a * (ret[0] // (a * 2))
        tmp = ret[0] % (a*2)
        if tmp > a:
            ret[i] += tmp-a
        a *= 2
    return sum(ret)
n, m = map(int, input().split())
if n == 1: print(sumF(m))
else: print(sumF(m)-sumF(n-1))