n = int(input())
l = list(map(int, input().split()))
o, e = 0, 0
for i in range(n):
    if l[i]%2:
        o += 1
    else:
        e += 1
if o < e:
    print("Happy")
else:
    print("Sad")