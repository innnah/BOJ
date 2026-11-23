n = int(input())
l = list(map(int,input().split()))
m = int(input())
l.sort()

i, j = 0, n-1
cnt = 0
while i < j:
    if l[i] + l[j] == m:
        cnt += 1
        i += 1
        j -= 1
    elif l[i] + l[j] > m:
        j -= 1
    elif l[i] + l[j] < m:
        i += 1

print(cnt)