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
    pi = getPi(b)
    begin, matched = 0, 0
    while begin <= n - m:
        if matched < m and a[begin + matched] == b[matched]:
            matched += 1
            if matched == m: 
                print("YES")
                sys.exit(0)
        else:
            if matched == 0: begin += 1
            else:
                begin += matched - pi[matched]
                matched = pi[matched]
    print("NO")
m = int(input())
n = m*2
a = list(map(int, input().split()))
b = list(map(int, input().split()))
kmp(a*2, b)