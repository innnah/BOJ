l = [list(map(int, input().split())) for _ in range(9)]
m = l[0][0]
pos = [0, 0]
for i in range(9):
    for j in range(9):
        if l[i][j] >= m:
            m = l[i][j]
            pos = [i+1, j+1]
print(m)
print(*pos)