import sys
input = sys.stdin.readline
def getPi(s):
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
a = input().rstrip()
b = input().rstrip()
n = len(a)*2-1
m = len(b)
print(len(kmp((a*2)[:-1], b)))