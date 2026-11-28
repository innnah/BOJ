import sys
input = sys.stdin.readline

cut = [65, 95, 125]

n = int(input())
arr = list(map(int, input().split()))
ans = [0, 0, 0, 0]
s, t = 0, 0
s1, t1 = 1, 4
for noon in arr:
    if t > 240:
        if s >= 35:
            for i in range(3):
                if s < cut[i]:
                    ans[i] += 1
                    break
            else:
                ans[3] += 1
        s, t, s1, t1 = 0, 0, 1, 4
    
    if noon == 1:
        if s >= 35:
            for i in range(3):
                if s < cut[i]:
                    ans[i] += 1
                    break
            else:
                ans[3] += 1
        s, t, s1, t1 = -1, -4, 1, 4
    elif noon == 2:
        if s1 == 1: t1 += 2
        else: s1 //= 2
    elif noon == 4:
        t += 56
    elif noon == 5:
        if t1 > 1: t1 -= 1
    elif noon == 6:
        if s1 < 32: s1 *= 2
    
    s += s1
    t += t1
for i in range(4):
    print(ans[i])