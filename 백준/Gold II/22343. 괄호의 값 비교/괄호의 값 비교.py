import sys
input = sys.stdin.readline
def getValue(s):
    ret = []
    v = 0
    for i in range(len(s)):
        if s[i] == "(":
            v += 1
        else:
            if s[i-1] == "(": ret.append(v)
            v -= 1
    return ret
for _ in range(int(input())):
    a = input().rstrip()
    b = input().rstrip()
    a = getValue(a)
    b = getValue(b)
    cnta, cntb = [0 for i in range(3000001)], [0 for _ in range(3000001)]
    for i in a:
        cnta[i] += 1
    for i in b:
        cntb[i] += 1
    for i in range(1, 3000001):
        cnta[i] += cnta[i-1] // 2
        cnta[i-1] %= 2
        cntb[i] += cntb[i-1] // 2
        cntb[i-1] %= 2
    i = 3000000
    while i >= 0 and cnta[i] == cntb[i]:
        i -= 1
    if i == -1:
        print("=")
    elif cnta[i] < cntb[i]:
        print("<")
    else:
        print(">")