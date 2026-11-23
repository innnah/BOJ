c = int(input())
for _ in range(c):
    n = int(input())
    l = list(map(int, input().split()))
    psum = 0
    maximum = -10987654321
    for i in range(n):
        psum = max(0, psum) + l[i]
        maximum = max(maximum, psum)

    print(maximum)