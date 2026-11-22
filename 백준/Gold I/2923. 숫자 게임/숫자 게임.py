import sys
input = sys.stdin.readline

n = int(input())
a = [0 for _ in range(100)]
b = [0 for _ in range(100)]
for k in range(n):
    lv, rv = map(int, input().split())
    a[lv] += 1
    b[100-rv] += 1
    ret = 0
    i, j = 0, 0
    iedit, jedit = 1, 1
    while i < 100 and j < 100:
        if iedit: ileft = a[i]
        if jedit: jleft = b[j]
        iedit = jedit = 0
        if ileft < jleft:
            if ileft != 0:
                ret = max(ret, i+100-j)
            jleft -= ileft
            i += 1
            iedit = 1
        elif ileft == jleft:
            if ileft != 0:
                ret = max(ret, i+100-j)
            i += 1
            j += 1
            iedit = jedit = 1
        else:
            if jleft != 0:
                ret = max(ret, i+100-j)
            ileft -= jleft
            j += 1
            jedit = 1
    print(ret)