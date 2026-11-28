import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = [input().rstrip() for _ in range(3)]
    state = [0 for _ in range(8)]
    for i in range(3):
        state[i] = (s[0][i] == 'O')
    state[3] = (s[1][2] == 'O')
    for i in range(3):
        state[6-i] = (s[2][i] == 'O')
    state[7] = (s[1][0] == 'O')
    ret = []
    cnt = 0
    for i in range(8):
        if state[i]:
            cnt += 1
        else:
            if cnt != 0:
                ret.append(cnt)
                cnt = 0
    if ret:
        if state[0]:
            ret[0] += cnt
        else:
            if cnt != 0:
                ret.append(cnt)
    else:
        if cnt != 0:
            ret.append(cnt)
    ret.sort()
    _, *a = map(int, input().split())
    print(int(a==ret))