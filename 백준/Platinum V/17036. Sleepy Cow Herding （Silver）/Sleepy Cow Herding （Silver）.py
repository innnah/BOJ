import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

min_moves = 10**20
if arr[n-2] - arr[0] == n-2 and arr[n-1] - arr[n-2] > 2:
    min_moves = 2
elif arr[n-1] - arr[1] == n-2 and arr[1] - arr[0] > 2:
    min_moves = 2
else:
    j = 0
    for i in range(n):
        while j < n-1 and arr[j+1] - arr[i] <= n-1: j += 1
        min_moves = min(min_moves, n-(j-i+1))

max_moves = max(arr[n-2] - arr[0], arr[n-1] - arr[1]) - (n-2)

print(min_moves)
print(max_moves)