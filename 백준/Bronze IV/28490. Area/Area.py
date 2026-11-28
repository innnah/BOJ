n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
print(max([i[0]*i[1] for i in arr]))