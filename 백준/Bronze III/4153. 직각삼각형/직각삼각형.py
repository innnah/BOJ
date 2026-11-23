while True:
    numlist = list(map(int, input().split()))

    if not any(numlist):
        break

    numlist.sort()

    if numlist[0] ** 2 + numlist[1] ** 2 == numlist[2] ** 2:
        print("right")
    else:
        print("wrong")