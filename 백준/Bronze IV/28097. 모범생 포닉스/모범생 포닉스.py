n = int(input())
s = sum(list(map(int, input().split())))
v = s+(n-1)*8
print(v//24, v%24)