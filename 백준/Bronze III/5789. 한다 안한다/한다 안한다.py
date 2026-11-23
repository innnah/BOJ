for _ in range(int(input())):
    s = input()
    print("Do-it", end='')
    if s[len(s)//2-1] !=  s[len(s)//2]: print("-Not")
    else:print()