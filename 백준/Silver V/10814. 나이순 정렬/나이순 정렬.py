n = int(input())
year_old = []

for i in range(n):
    num, name = input().split()
    year_old.append([int(num), i, name])

year_old.sort()

for x in year_old:
    print(x[0], x[2])