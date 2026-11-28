a, b, c = map(int, input().split())
l = []
for i in range(a+1):
    if i + b*(c-1) < a and i + b*c >= a:
        l.append(i)
print(min(l), max(l))