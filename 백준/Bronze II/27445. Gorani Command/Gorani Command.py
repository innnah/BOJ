n, m = map(int, input().split())
mini, miniidx = 987654321, -1
for i in range(1, n):
    a = int(input())
    if mini >= a:
        mini = a
        miniidx = i
l = list(map(int, input().split()))
if mini >= l[0]: print(n, end = ' ')
else: print(miniidx, end = ' ')
mini, miniidx = 987654321, -1
for i in range(1, m+1):
    a = l[i-1]
    if mini >= a:
        mini = a
        miniidx = i
print(miniidx)