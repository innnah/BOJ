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

n = int(input())
s = input().rstrip()
pi = getPi(s)
dp = [987654321 for _ in range(n)]
for i in range(n):
    if pi[i+1] != 0: dp[i] = pi[i+1]
    if pi[pi[i+1]] > 0: dp[i] = dp[pi[i+1]-1]
ret = 0
end = n
while end > 0:
    ret += max(end - dp[end-1], 0)
    end -= 1
print(ret)