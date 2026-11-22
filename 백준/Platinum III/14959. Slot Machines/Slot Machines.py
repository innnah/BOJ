import sys
input = sys.stdin.readline

def kmp_fail(pattern):
    lp = len(pattern)
    failure = [0 for _ in range(lp)]
    pidx = 0
    for idx in range(1, lp):
        while pidx > 0 and pattern[idx] != pattern[pidx]:
            pidx = failure[pidx-1]
        if pattern[idx] == pattern[pidx] :
            pidx += 1
            failure[idx] = pidx
    return failure

n = int(input())
l = list(map(int, input().split()))[::-1]
fail = kmp_fail(l)[::-1]
k, p = 129381928491820391029, 120398102940192340912
for i in range(n):
    ck, cp = i, n-i-fail[i]
    if ck + cp < k + p:
        k, p = ck, cp
    elif ck + cp == k + p:
        if cp < p:
            k, p = ck, cp
print(k, p)