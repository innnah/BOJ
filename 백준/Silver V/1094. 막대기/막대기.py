n = int(input())
cnt = 0

while n > 0:
    maxnum = 0
    for x in range(1, 8):
        if 2 ** x > n:
            maxnum = 2 ** (x - 1)
            break
            
    n -= maxnum
    cnt += 1
    
print(cnt)