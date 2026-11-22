for _ in range(int(input())):
    s = input()
    for i in range(len(s)):
        if s[i] == 'D':
            print(i)
            break
    else:
        print(len(s))