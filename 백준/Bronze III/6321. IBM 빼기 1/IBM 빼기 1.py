for i in range(int(input())):
    s = input()
    print(f"String #{i+1}")
    for i in s:
        if i != 'Z': print(chr(ord(i)+1), end = '')
        else: print('A', end = '')
    print()
    print()