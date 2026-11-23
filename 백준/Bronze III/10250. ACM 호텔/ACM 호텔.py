T = int(input())

for _ in range(T):
    h, w, n = map(int, input().split())

    passw = n // h + 1
    passh = n % h

    if passh == 0:
        passh = h

    if n / h == float(n // h):
        passw -= 1
    
    print("%d%02d" % (passh, passw))