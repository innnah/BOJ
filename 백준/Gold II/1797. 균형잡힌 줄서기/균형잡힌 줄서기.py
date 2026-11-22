import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key = lambda x : x[1])
psum = 0
arr2 = [[] for _ in range(2*n+1)]
arr2[0].append(-1)
for i in range(n):
    psum += arr[i][0] * 2 - 1
    arr2[psum].append(i)
ans = 0
for i in range(2*n+1):
    if len(arr2[i]) < 2: continue
    ans = max(ans, arr[arr2[i][-1]][1] - arr[arr2[i][0]+1][1])
print(ans)