n, m = map(int, input().split())
print(int(sum(map(int, input().split())) % m == 0))