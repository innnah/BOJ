import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()
h = "IO" * n + "I"
cnt = 0
ans = 0
for i in range(m):
    if s[i] == h[cnt]:
        cnt += 1
        if cnt == len(h):
            ans += 1
            cnt -= 2
    else:
        cnt = (s[i] == "I")
print(ans)