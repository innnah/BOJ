n, m = map(int, input().split())
l = list(map(int, input().split()))
i = 0
while l[i] >= m:
    i = (i+1)%n
    m += 1
print(i+1)