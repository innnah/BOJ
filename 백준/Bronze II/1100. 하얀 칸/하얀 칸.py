l = ["F."*4, ".F"*4] * 4
strings = [input().rstrip() for _ in range(8)]
cnt = 0

for i in range(8):
    for j in range(8):
        if strings[i][j] == "F" and strings[i][j] == l[i][j]:
            cnt += 1

print(cnt)