s = input()
n = int(input())
arr = [input() for _ in range(n)]

dp = [0 for _ in range(len(s)+1)]
dp[-1] = 1
for i in range(len(s)):
    for j in range(n):
        if arr[j] == s[i-len(arr[j])+1:i+1]:
            dp[i] |= dp[i-len(arr[j])]
print(dp[len(s)-1])