cache = [[[-1 for _ in range(101)] for _ in range(101)] for _ in range(101)]

def w(a, b, c):
    if cache[a+50][b+50][c+50] != -1:
        return cache[a+50][b+50][c+50]
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        tmp = w(20, 20, 20)
        cache[70][70][70] = tmp
        return tmp
    elif a < b and b < c:
        tmp = [w(a, b, c-1), w(a, b-1, c-1), w(a, b-1, c)]
        cache[a+50][b+50][c+49] = tmp[0]
        cache[a+50][b+49][c+49] = tmp[1]
        cache[a+50][b+49][c+49] = tmp[2]
        return tmp[0]+tmp[1]-tmp[2]
    else:
        tmp = [w(a-1, b, c), w(a-1, b-1, c), w(a-1, b, c-1), w(a-1, b-1, c-1)]
        cache[a+49][b+50][c+50] = tmp[0]
        cache[a+49][b+49][c+50] = tmp[1]
        cache[a+49][b+50][c+49] = tmp[2]
        cache[a+49][b+49][c+49] = tmp[3]
        return tmp[0]+tmp[1]+tmp[2]-tmp[3]

while True:
    a, b, c = map(int, input().split())
    if (a, b, c) == (-1, -1, -1):
        break
    s = "w(%d, %d, %d) = " % (a, b, c)
    print(s + str(w(a, b, c)))