import sys

input = sys.stdin.readline

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
divide = [[0, 0], [0, 1], [1, 0], [1, 1]]
black = 0
blue = 0

def isfilledOneColor(l):
    for a in l:
        for i in a:
            if i != l[0][0]:
                return False
    return True

def makeList(l, div):
    ret = []
    for i in range(div[0], div[0]+len(l)//2):
        ret.append(l[i][div[1]:div[1]+len(l)//2])
    return ret

def solve(l):
    global black, blue, divide
    if isfilledOneColor(l):
        if l[0][0]: blue += 1
        else: black += 1
        return
    
    p = len(l) // 2
    for a in divide:
        tmp = []
        for i in a: tmp.append(i*p)
        solve(makeList(l, tmp))
        
solve(l)
print(black)
print(blue)