import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
val1 = max(arr, key = lambda x : x[0] + x[1]), min(arr, key = lambda x : x[0] + x[1])
val2 = max(arr, key = lambda x : x[0] - x[1]), min(arr, key = lambda x : x[0] - x[1])
print(max(sum(val1[0]) - sum(val1[1]), abs(val2[0][0] - val2[0][1] - val2[1][0] + val2[1][1])))