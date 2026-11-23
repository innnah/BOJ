import math

n, k = map(int, input().split())
l = [[0, 0] for _ in range(6)]
rooms = 0
for _ in range(n):
    s, g = map(int, input().split())
    l[g-1][s] += 1
for grade in l:
    for i in grade:
        rooms += math.ceil(i / k)
print(rooms)