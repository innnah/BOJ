d = {0 : "N", 1 : "E", 2 : "S", 3 : "W"}
direction = 0
for _ in range(10):
    o = int(input())
    if o == 1:
        direction += 1
        direction %= 4
    elif o == 2:
        direction += 2
        direction %= 4
    else:
        direction -= 1
        direction = (direction+4) % 4
print(d[direction])