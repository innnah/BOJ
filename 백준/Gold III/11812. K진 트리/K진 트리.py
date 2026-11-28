import sys
input = sys.stdin.readline

n, k, q = map(int, input().split())
if k == 1:
    for _ in range(q):
        a, b = map(int, input().split())
        print(abs(a-b))
    sys.exit()
for _ in range(q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    cnt1 = 0
    while a >= k**cnt1:
        a -= k**cnt1
        cnt1 += 1
    cnt2 = 0
    while b >= k**cnt2:
        b -= k**cnt2
        cnt2 += 1
    
    dist = 0
    if cnt1 < cnt2:
        cnt1, cnt2 = cnt2, cnt1
        a, b = b, a
    while cnt1 > cnt2:
        cnt1 -= 1
        a //= k
        dist += 1
    while a != b:
        a //= k
        b //= k
        dist += 2
    print(dist)