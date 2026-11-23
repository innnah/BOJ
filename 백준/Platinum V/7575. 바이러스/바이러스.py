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
    n, m = len(a), len(b)
    pi = getPi(b)
    begin, matched = 0, 0
    while begin <= n - m:
        if matched < m and a[begin + matched] == b[matched]:
            matched += 1
            if matched == m:
                return True
        else:
            if matched == 0: begin += 1
            else:
                begin += matched - pi[matched]
                matched = pi[matched]
    return False
def toStr(l):
    s = ''
    for i in l:
        s += str(i) + ' '
    return s[:-1]
n, k = map(int, input().split())
programs = []
strPrograms = []
for _ in range(n):
    input()
    l = input().rstrip()
    strPrograms.append(l)
    programs.append(list(map(int, l.split())))
for i in range(len(programs[0])-k+1):
    virus = programs[0][i:i+k]
    revVirus = virus[::-1]
    a = toStr(virus)
    b = toStr(revVirus)
    for j in range(1, n):
        if not kmp(strPrograms[j], a) and not kmp(strPrograms[j], b):
            break
    else:
        print("YES")
        sys.exit(0)
print("NO")