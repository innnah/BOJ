import sys
from collections import deque
input = sys.stdin.readline

class State:
    def __init__(self, l):
        self.board = 0
        for i in range(3):
            for j in range(3):
                if l[i][j] == 0:
                    self.empty = (i, j)
                self.board += l[i][j] * (1 << ((i*3+j)*4))
    def get(self, idx): return self.board // (1 << ((idx[0]*3+idx[1])*4)) % 16
    def swap(self, idx):
        '''swap with empty place'''
        value = self.get(idx)
        self.board += value * (1 << ((self.empty[0]*3+self.empty[1])*4))
        self.empty = idx
        self.board -= value * (1 << ((self.empty[0]*3+self.empty[1])*4))
    def __str__(self):
        s = ""
        for i in range(3):
            for j in range(3):
                s += str(self.get((i, j))) + " "
        return s

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def bfs():
    q = deque([(board, 0)])
    d = set([board.board])
    while q:
        v, dist = q.popleft()
        if v.board == target.board: return dist
        y, x = v.empty
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 3 and 0 <= ny < 3:
                v.swap((ny, nx))
                if v.board not in d:
                    tmp = State([[1,2,3],[4,5,6],[7,8,0]])
                    tmp.board = v.board
                    tmp.empty = v.empty
                    q.append((tmp, dist+1))
                    d.add(tmp.board)
                v.swap((y, x))
    return -1

l = [list(map(int, input().split())) for _ in range(3)]
board = State(l)
target = State([[1,2,3],[4,5,6],[7,8,0]])
print(bfs())