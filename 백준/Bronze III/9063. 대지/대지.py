n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
a=[arr[i][0] for i in range(n)]
b=[arr[i][1] for i in range(n)]
print((max(a)-min(a))*(max(b)-min(b)))