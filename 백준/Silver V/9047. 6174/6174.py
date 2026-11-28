def toNum(a):
    return 1000*int(a[0]) + 100*int(a[1]) + 10 * int(a[2]) + int(a[3])
def toStrList(num):
    ret = list(str(num))
    return ['0'] * (4-len(ret)) + ret
for _ in range(int(input())):
    s = list(input())
    cnt = 0
    while s != ['6', '1', '7', '4']:
        s.sort()
        s = toStrList(-toNum(s) + toNum(s[::-1]))
        cnt += 1
    print(cnt)