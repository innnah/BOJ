import sys
input = sys.stdin.readline

d = {"P" : 0, "C" : 1, "V" : 2, "S" : 3, "G" : 4, "F" : 5, "O" : 6}
n = int(input())
arr = [input().rstrip() for _ in range(n)]
cost = list(map(int, input().split())) + [int(input())]
arr = [[d[j] for j in i] for i in arr]
ans = 0
for i in range(n):
    if arr[i] == [arr[i][0] for _ in range(len(arr[i]))]:
        if arr[i][0] == 6:
            ans += cost[6] * len(arr[i])
        else:
            ans += min(cost[6], cost[arr[i][0]]) * len(arr[i])
    else:
        ans += cost[6] * len(arr[i])
print(ans)