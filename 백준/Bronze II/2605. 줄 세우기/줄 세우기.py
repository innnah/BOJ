n = int(input())
l = list(map(int, input().split()))
arr = []
for i in range(n):
    arr.insert(i-l[i], i+1)
print(*arr)