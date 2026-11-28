import sys
input = sys.stdin.readline

n, q = map(int, input().split())
arr = list(map(int, input().split()))
querys = [list(map(int, input().split())) + [i] for i in range(q)]
querys = [[l-1, r-1, idx] for l, r, idx in querys]
ans = [0 for _ in range(q)]
querys.sort(key = lambda x: [x[0]//(n**0.5), x[1]])

val = 0
cnt = [0 for _ in range(10**6+1)]
for i in range(querys[0][0], querys[0][1]+1):
    val += arr[i] * (cnt[arr[i]] * 2 + 1)
    cnt[arr[i]] += 1
ans[querys[0][2]] = val

l, r = querys[0][0], querys[0][1]
for i in range(1, q):
    nl, nr, idx = querys[i]
    while r < nr:
        r += 1
        val += arr[r] * (cnt[arr[r]] * 2 + 1)
        cnt[arr[r]] += 1
    while l > nl:
        l -= 1
        val += arr[l] * (cnt[arr[l]] * 2 + 1)
        cnt[arr[l]] += 1
    while r > nr:
        val -= arr[r] * (cnt[arr[r]] * 2 - 1)
        cnt[arr[r]] -= 1
        r -= 1
    while l < nl:
        val -= arr[l] * (cnt[arr[l]] * 2 - 1)
        cnt[arr[l]] -= 1
        l += 1
    ans[idx] = val

print('\n'.join(map(str, ans)))