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

s = input().rstrip()
pi = getPi(s)
for i in range(1, len(pi)):
    if pi[i] != 0 and pi[i] % (i-pi[i]) == 0: print(i, pi[i]//(i-pi[i])+1)