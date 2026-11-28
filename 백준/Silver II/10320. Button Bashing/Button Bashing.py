from collections import deque

for _ in range(int(input())):
    visited = [0 for _ in range(3601)]
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    q = deque([[0, 1]])
    visited[0] = 1
    while q:
        v, d = q.popleft()
        for i in range(n):
            nv = max(min(v+arr[i], 3600), 0)
            if not visited[nv]:
                visited[nv] = d+1
                q.append([nv, d+1])
    
    if visited[m]:
        print(visited[m]-1, 0)
    else:
        for i in range(m+1, 3601):
            if visited[i]:
                print(visited[i]-1, i-m)
                break