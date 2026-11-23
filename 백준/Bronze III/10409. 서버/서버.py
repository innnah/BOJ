n, ct = map(int, input().split())
l = list(map(int, input().split()))
t = 0
for i in range(n):
    t += l[i]
    if t > ct:
        print(i)
        break
else:
    print(n)