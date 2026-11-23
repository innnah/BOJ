while True:
    n = input()
    if n == "0": break
    ret = 1
    for i in n:
        if i == "1": ret += 3
        elif i == "0": ret += 5
        else: ret += 4
    print(ret)