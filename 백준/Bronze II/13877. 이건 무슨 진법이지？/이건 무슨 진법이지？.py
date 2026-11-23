for i in range(int(input())):
    _, a = input().split()
    try:
        print(i+1, int(a,8), int(a), int(a,16))
    except ValueError:
        print(i+1, 0, int(a), int(a,16))