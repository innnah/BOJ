import sys
input = sys.stdin.readline

while 1:
    name = input().rstrip()
    if name == '': break
    ret = ""
    for i in name:
        if i == 'e': ret += 'i'
        elif i == 'i': ret += 'e'
        elif i == 'E': ret += 'I'
        elif i == 'I': ret += 'E'
        else: ret += i
    print(ret)