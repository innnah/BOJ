n = int(input())
s = input().rstrip()
red = s.count('R')
blue = n - red
ans = min(red, blue)
cnt = 1
for i in range(1, n):
    if s[i-1] != s[i]:
        break
    cnt += 1
if s[0] == "R": ans = min(ans, red-cnt)
else: ans = min(ans, blue-cnt)

cnt = 1
for i in range(n-2, -1, -1):
    if s[i+1] != s[i]:
        break
    cnt += 1
if s[-1] == "R": ans = min(ans, red-cnt)
else: ans = min(ans, blue-cnt)

print(ans)