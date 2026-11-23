for t in range(int(input())):
    h = int(input())
    s = input()
    for i in s:
        if i == 'c': h += 1
        else: h -= 1
        if h <= 0:
            break
    print(f"Data Set {t+1}:")
    print(h)
    print()