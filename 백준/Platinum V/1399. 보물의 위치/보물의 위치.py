import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    a -= 1
    if b % 9 == 0:
        x = ((a-1)//4 - (a-3)//4) * 9
        y = (a//4 - (a-2)//4) * 9 - 8
        print(x, y)
    elif b % 9 == 3:
        if a == 0:
            print(0, 1)
        else:
            x = ((a-1)//4 - (a-3)//4) * 9 - 6
            y = (a//4 - (a-2)//4) * 9 - 8
            print(x, y)
    elif b % 9 == 6:
        if a == 0:
            print(0, 1)
        else:
            x = ((a-1)//4 - (a-3)//4) * 9 - 3
            y = (a//4 - (a-2)//4) * 9 - 8
            print(x, y)
    else:
        b %= 9
        a += 4
        pattern_1 = [1]
        while (pattern_1[-1]*b)%9 != 1:
            pattern_1.append((pattern_1[-1]*b)%9)
        #print(pattern_1)

        pattern_4 = [[pattern_1[i%len(pattern_1)]] for i in range(4)]
        for i in range(4):
            while (pattern_4[i][-1]*(b**4)) % 9 != pattern_4[i][0]:
                pattern_4[i].append((pattern_4[i][-1]*(b**4)) % 9)
        #print(pattern_4)

        n = len(pattern_4[0])
        py = (a//4//n)*sum(pattern_4[0]) + sum(pattern_4[0][:a//4%n])
        my = ((a-2)//4//n)*sum(pattern_4[2]) + sum(pattern_4[2][:(a-2)//4%n])
        px = ((a-1)//4//n)*sum(pattern_4[1]) + sum(pattern_4[1][:(a-1)//4%n])
        mx = ((a-3)//4//n)*sum(pattern_4[3]) + sum(pattern_4[3][:(a-3)//4%n])
        print(px-mx, py-my)