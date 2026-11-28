n, m = map(int, input().split())
c1, c9 = map(int, input().split())
if n > m+1:
    print(-1)
    exit(0)

arr = [-1]
s = n * (2*m-n+1) // 2
tmp = c9
for i in range(n-1):
    s -= m-n+1+i
    arr.append(max(arr[-1]+1, tmp-s))
    tmp -= arr[-1]
arr.append(tmp)
arr.pop(0)

if sum(arr) != c9 or sorted(arr) != arr or len(set(arr)) != len(arr):
    print(-1)
    exit(0)

for i in range(n):
    print(*([9]*arr[i]+[1]*(m-arr[i])))