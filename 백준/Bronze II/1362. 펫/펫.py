cnt = 1
while True:
    n, m = map(int, input().split())
    dead = False
    if (n, m) == (0, 0): break
    print(cnt, end = ' ')
    while True:
        a, b = input().rstrip().split()
        if (a, b) == ("#", "0"): break
        if a == "E": m -= int(b)
        elif a == "F": m += int(b)
        if m <= 0: 
            print("RIP")
            dead = True
    if not dead:
        if m < n*2 and m > n/2: print(":-)")
        else: print(":-(")
    cnt += 1