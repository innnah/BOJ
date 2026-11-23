n = int(input())
tmp = 1
answer = 0
while True:
    n -= tmp
    if n >= 0:
        answer += 1
        tmp += 1   
    else:
        print(answer)
        break