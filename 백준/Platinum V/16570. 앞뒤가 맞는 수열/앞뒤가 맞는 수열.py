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
m = int(input())
s = list(map(int, input().split()))[::-1]
pi = getPi(s)
maximum = max(pi)
if maximum == 0: print(-1)
else: print(maximum, pi.count(maximum))