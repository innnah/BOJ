n = int(input())
l = []
for _ in range(n):
    b, a = input().split()
    l.append((b, int(a)))
l.sort(key = lambda x:x[1])
print(l[0][0])