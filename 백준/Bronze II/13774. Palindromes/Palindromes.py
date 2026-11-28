while 1:
    s = input()
    if s == '#': break
    for i in range(len(s)):
        t = s[:i] + s[i+1:]
        if t == t[::-1]:
            print(t)
            break
    else:
        print("not possible")