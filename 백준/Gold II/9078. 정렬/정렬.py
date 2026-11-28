import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    if n == 1:
        print("YES")
        continue
    if n == 2:
        print("YES" if arr[i] == 1 else "NO")
    for i in range(1, n-1):
        idx = arr.index(i)
        if idx == n-1:
            arr[-3:] = [arr[-2], arr[-1], arr[-3]]
            idx = n-2
        arr[i-1:] = arr[idx:idx+2] + arr[i-1:idx] + arr[idx+2:]
    if [i+1 for i in range(n)] == arr:
        print("YES")
    else:
        print("NO")