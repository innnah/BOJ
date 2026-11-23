ret = 0
while True:
    try:
        input()
    except EOFError:
        print(ret)
        break
    else:
        ret += 1