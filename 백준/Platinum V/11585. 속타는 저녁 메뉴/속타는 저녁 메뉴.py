import sys, math
input = sys.stdin.readline

def getPi(s):
    m = len(s)
    pi = [0 for _ in range(m+1)]
    begin, matched = 1, 0
    while begin + matched < m:
        if s[begin + matched] == s[matched]:
            matched += 1
            pi[begin + matched] = matched
        else:
            if matched == 0: begin += 1
            else:
                begin += matched - pi[matched]
                matched = pi[matched]
    return pi
def kmp(a, b):
    n, m = len(a), len(b)
    ret = []
    pi = getPi(b)
    begin, matched = 0, 0
    while begin <= n - m:
        if matched < m and a[begin + matched] == b[matched]:
            matched += 1
            if matched == m: ret.append(begin)
        else:
            if matched == 0: begin += 1
            else:
                begin += matched - pi[matched]
                matched = pi[matched]
    return ret

n = int(input())
a = input().split()
b = input().split()
ret = kmp(b*2, a)
cnt = 0
for i in ret:
    if i >= n: break
    cnt += 1
g = math.gcd(cnt, n)
print(f"{cnt//g}/{n//g}")