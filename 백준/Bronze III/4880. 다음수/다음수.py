while 1:
    a, b, c = map(int, input().split())
    if a == b == c == 0: break
    if a-b == b-c:
        print("AP " + str(c + c - b))
    else:
        print("GP " + str(c * c // b))