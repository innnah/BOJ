from decimal import *

setcontext(BasicContext)
dict = {"@":"*3", "%":"+5", "#":"-7"}
n = int(input())
for _ in range(n):
    l = input().rstrip().split()
    s = l[0]
    for a in l[1:]:
        s += dict[a]
        s = str(eval(s))
    ret = Decimal(s)
    ret = round(ret, 2)
    print(ret)