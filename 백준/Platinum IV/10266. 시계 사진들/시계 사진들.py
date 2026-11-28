import sys
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
    n = len(a) 
    m = len(b)
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
a = list(map(int, input().split()))
b = list(map(int, input().split()))
aa = [0 for _ in range(360000)]
bb = [0 for _ in range(360000)]
for i in a:
    aa[i] = 1
for i in b:
    bb[i] = 1
aa = aa*2
print("im" * (not len(kmp(aa, bb))) + "possible")