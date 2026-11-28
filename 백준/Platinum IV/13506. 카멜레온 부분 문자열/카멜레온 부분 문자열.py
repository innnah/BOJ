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
s = input().rstrip()
m = len(s)
pi = getPi(s)
is_in_pi = [0 for _ in range(m+1)]
for i in range(m):
    is_in_pi[pi[i]] = 1
fail = pi[m]
while fail > 0:
    if is_in_pi[fail]:
        print(s[:fail])
        sys.exit(0)
    fail = pi[fail]
print(-1)