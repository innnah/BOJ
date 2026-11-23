s = input()
rets = ""
flag = False
for i in s:
    if i == "<":
        flag = True
        print(rets[::-1], end='')
        rets = ""
    elif i == ">":
        flag = False
        print(">", end='')
    if flag: print(i, end='')
    elif i == " ":
        print(rets[::-1], end=' ')
        rets = ""
    elif i != ">":
        rets += i
print(rets[::-1])