p = int(input())
s = 0
d = {False : "Yes", True : "No"}
for _ in range(int(input())):
    a, b = map(int, input().split())
    s += a*b
print(d[bool(s-p)])