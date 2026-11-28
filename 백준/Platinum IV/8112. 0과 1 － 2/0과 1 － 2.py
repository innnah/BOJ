import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque([1])
    visited[1] = 1
    while q:
        value = q.popleft()
        if value == 0: return 1
        for i in range(2):
            ne = (value * 10 + i) % mod
            if not visited[ne]:
                q.append(ne)
                trace[ne] = value
                visited[ne] = 1
    return 0
def reconstruct():
    string = ""
    mod_res = 0
    while mod_res != 1:
        prev = trace[mod_res]
        if mod_res == (prev * 10 + 1) % mod:
            string += "1"
        else:
            string += "0"
        mod_res = prev
    string += "1"
    return string[::-1]
for _ in range(int(input())):
    mod = int(input())
    if mod == 1:
        print(1)
        continue
    visited = [0 for _ in range(mod)]
    trace = [-1 for _ in range(mod)]
    if bfs():
        print(reconstruct())
    else:
        print("BRAK")