import sys

def makezero(n, get = 1, sum = 1, string = ""):
    if get == n:
        if sum == 0:
            return [string]
        return [""]

    l = []
    tmp1 = makezero(n, get+1, sum + get + 1, string + "+")
    tmp2 = makezero(n, get+1, sum - get - 1, string + "-")
    willadd = 0
    if string != "":
        if string[-1] == "+":
            willadd = int(str(get) + str(get+1)) - get
        elif string[-1] == "-":
            willadd = -(int(str(get) + str(get+1))) + get
        if string[-1] != " ":
            tmp3 = makezero(n, get+1, sum + willadd, string + " ")
        else:
            tmp3 = [""]
    else:
        willadd = 11
        tmp3 = makezero(n, get+1, sum + willadd, string + " ")

    if tmp1 != [""]:
        l += tmp1
    if tmp2 != [""]:
        l += tmp2
    if tmp3 != [""]:
        l += tmp3
    return l

def printnums(string1, string2):
    for i in range(len(string2)):
        print(string1[i] + string2[i], end = '')
    print(string1[-1])

t = int(sys.stdin.readline())
for k in range(t):
    n = int(sys.stdin.readline())
    l = makezero(n)
    l.sort()
    s = ""
    for i in range(1, n+1):
        s += str(i)
    for i in range(len(l)):
        printnums(s, l[i])
    if k != t-1:
        print()