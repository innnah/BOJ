import sys

input = sys.stdin.readline

def isinside(y, x): return 0 <= x < n and 0 <= y < m

m, n = map(int, input().split())
weights = [list(map(int, list(input().rstrip()))) for _ in range(m)]
memory = [[0] * n for _ in range(m)]
maxval = -1
for j in range(n):
    for i in range(m):
        if isinside(i-1, j-1):
            memory[i][j] = max(memory[i][j], memory[i-1][j-1]+weights[i-1][j-1])
        if isinside(i, j-1):
            memory[i][j] = max(memory[i][j], memory[i][j-1]+weights[i][j-1])
        if isinside(i+1, j-1):
            memory[i][j] = max(memory[i][j], memory[i+1][j-1]+weights[i+1][j-1])
        maxval = max(memory[i][j], maxval)
print(maxval)