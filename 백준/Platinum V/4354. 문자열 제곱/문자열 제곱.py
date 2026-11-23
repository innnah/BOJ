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

while True:
    s = input().rstrip()
    if s == '.': break
    pi = getPi(s)
    maximum = 1
    if pi[-1] % (len(s) - pi[-1]) == 0:
        maximum = pi[-1]//(len(s)-pi[-1])+1
    print(maximum)