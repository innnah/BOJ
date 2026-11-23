for _ in range(int(input())):
    s = input().rstrip().split()
    for x in s:
        print(x[::-1], end = ' ')
    print()