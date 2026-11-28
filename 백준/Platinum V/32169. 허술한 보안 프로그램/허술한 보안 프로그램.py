import sys
input = sys.stdin.readline

n = int(input())
a = 1
while a < n:
    a *= 2
a -= 1

arr = [a-i for i in range(n)]
used = [0 for _ in range(n)]
for i in range(n):
    if arr[i] < n:
        used[arr[i]] = 1
for i in range(n):
    if arr[i] >= n:
        for j in range(11, -1, -1):
            if (1 << j) & arr[i]:
                arr[i] -= 1 << j
                if not used[arr[i]]:
                    used[arr[i]] = 1
                    break

print("?", *[i for i in range(n)])
sys.stdout.flush()
ret1 = list(map(int, input().split()))
print("?", *arr)
sys.stdout.flush()
ret2 = list(map(int, input().split()))

ans = [0 for _  in range(n)]
for i in range(n):
    for j in range(12):
        if not ((1 << j) & i):
            ans[i] |= ret1[i] & (1 << j)
        if not ((1 << j) & arr[i]):
            ans[i] |= ret2[i] & (1 << j)
print("!", *ans)
sys.stdout.flush()