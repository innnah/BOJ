import sys

def repaint(l):
    ret = [0, 0]
    letters = ['B', 'W']
    for k in range(2):
        correctChar = letters[k]
        for i in range(8):
            innerRet = 0
            for j in range(8):
                if correctChar != l[i][j]:
                    innerRet += 1
                correctChar = 'B' if correctChar == "W" else "W"
            correctChar = 'B' if correctChar == "W" else "W"
            ret[k] += innerRet
    return ret

def make8squareList(l, startidx1, startidx2):
    ret = []
    for i in range(startidx1, startidx1+8):
        ret.append(l[i][startidx2:startidx2+8])
    return ret

def solution(l):
    global n, m
    ret = sys.maxsize
    for i in range(n - 7):
        for j in range(m - 7):
            tmp = repaint(make8squareList(l, i, j))
            tmp.append(ret)
            ret = min(tmp)
    return ret

n, m = map(int, input().split())
l = [list(input().rstrip()) for _ in range(n)]
print(solution(l))