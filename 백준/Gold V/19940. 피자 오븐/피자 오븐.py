for _ in range(int(input())):
    n = int(input())
    buttons = [0] * 5
    btn60, btn10, btn1 = n // 60, (n%60) // 10, int(str(n)[-1])
    if btn1 > 5:
        btn10 += 1
        btn1 -= 10
    if btn10 > 3:
        btn60 += 1
        btn10 -= 6
    if btn10 < 0 and btn1 == 5:
        btn10 += 1
        btn1 -= 10
    
    buttons[0] = btn60
    buttons[2-(btn10>0)] = abs(btn10)
    buttons[4-(btn1>0)] = abs(btn1)
    print(*buttons)