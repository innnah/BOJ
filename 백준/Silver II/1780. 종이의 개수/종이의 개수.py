import sys

input = sys.stdin.readline

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
divide = [[0, 0], [0, 1], [0,2], [1, 0], [1, 1], [1,2], [2, 0], [2, 1], [2,2]]
min1 = 0
p1 = 0
p0 = 0

def isfilledOneColor(l):
    for a in l:
        for i in a:
            if i != l[0][0]:
                return False
    return True

def makeList(l, div):
    ret = []
    for i in range(div[0], div[0]+len(l)//3):
        ret.append(l[i][div[1]:div[1]+len(l)//3])
    return ret

def solve(l):
    global min1, p1, p0
    if isfilledOneColor(l):
        if l[0][0]==-1: min1 += 1
        elif l[0][0]==1: p1 += 1
        else: p0 += 1
        return
    
    p = len(l) // 3
    for a in divide:
        tmp = []
        for i in a: tmp.append(i*p)
        solve(makeList(l, tmp))

solve(l)
print(min1)
print(p0)
print(p1)