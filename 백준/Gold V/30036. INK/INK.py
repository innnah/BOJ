import sys
input = sys.stdin.readline

def isInside(x, y): return 0<=x<m and 0<=y<m

d = {"U" : (0, -1), "R": (1, 0), "L" : (-1, 0), "D" : (0, 1)}
n, m, k = map(int, input().split())
inks = list(input().rstrip())
paper = [list(input().rstrip()) for _ in range(m)]
commands = input().rstrip()
box = [-1, -1]
for i in range(m):
    for j in range(m):
        if paper[i][j] == "@":
            box = [j, i]
cidx = 0
ink_c = 0
for q in commands:
    if q == 'j':
        ink_c += 1
    elif d.get(q) is not None:
        nx, ny = box[0] + d[q][0], box[1] + d[q][1]
        if isInside(nx, ny) and paper[ny][nx] == '.':
            paper[box[1]][box[0]] = '.'
            box = [nx, ny]
            paper[ny][nx] = '@'
    else:
        for i in range(max(0, box[1]-ink_c), min(m-1, box[1]+ink_c)+1):
            for j in range(max(0, box[0]-ink_c), min(m-1, box[0]+ink_c)+1):
                if abs(i-box[1])+abs(j-box[0]) <= ink_c and paper[i][j] not in ("@", "."):
                    paper[i][j] = inks[cidx]
        ink_c = 0
        cidx = (cidx+1)%n
for i in paper:
    print(''.join(i))