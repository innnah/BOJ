a, b = map(int, input().split())
palin = []
for i in range(a, (b+1 if b <= 10000000 else 10000000)):
    if len(str(i)) % 2 or i == 11:
        if str(i) == str(i)[::-1]:
            for j in range(2, int(i**0.5)+1):
                if i % j == 0:
                    break
            else:
                print(i)
print(-1)