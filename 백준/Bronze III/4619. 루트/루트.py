while 1:
    a, b = map(int, input().split())
    if a == 0 and b == 0: break
    t = 0
    minv = 987654321
    ans = 0
    while t**b <= a:
        if minv >= abs(t**b-a):
            minv = abs(t**b-a)
            ans = t
        t += 1
    if minv >= abs(t**b-a):
        minv = abs(t**b-a)
        ans = t
    print(ans)
    