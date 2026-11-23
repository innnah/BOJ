n = int(input())
cyclenum = n
cnt = 0

while True:
    tmp = list(str(cyclenum))
    
    if len(tmp) == 1:
        tmp.insert(0, "0")

    cyclenum = int(tmp[1]) * 10 + (int(tmp[0]) + int(tmp[1])) % 10

    cnt += 1

    if n == cyclenum:
        break

print(cnt)