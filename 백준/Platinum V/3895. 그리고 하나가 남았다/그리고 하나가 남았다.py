import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0: break
    c -= 1
    dp = [0 for _ in range(a+1)]
    for i in range(2, a+1):
        dp[i] = (dp[i-1] + b) % i
    print((dp[a]+c-b+1)%a+1)