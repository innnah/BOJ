import sys

input = sys.stdin.readline
print = sys.stdout.write

MAX = 1000000
dp = [-1 for _ in range(MAX+1)]
d = {0:"koosaga", 1:"cubelover"}
dp[0] = 1
dp[1] = 0
for i in range(2, MAX+1):
    for j in range(1, int(i**0.5)+1):
        if dp[i-j**2]: 
            dp[i] = 0
            break
    else:
        dp[i] = 1
for _ in range(int(input())):
    print(str(d[dp[int(input())]]))
    print('\n')