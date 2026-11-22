import sys
input = sys.stdin.readline

n, k = map(int, input().split())
l = list(input().rstrip())
visited = [0 for _ in range(n)]
for i in range(n):
    if l[i] == 'P':
        for j in range(max(0, i-k), min(n, i+k+1)):
            if l[j] == 'H' and not visited[j]:
                visited[j] = 1
                break
print(sum(visited))