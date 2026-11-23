a, b, c = map(int, input().split())
x, y, z = 1, 1, 1
cnt = 1
while x != a or y != b or z != c:
    x += 1
    y += 1
    z += 1
    if x > 15: x = 1
    if y > 28: y = 1
    if z > 19: z = 1
    cnt += 1
print(cnt)