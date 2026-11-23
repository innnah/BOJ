n = int(input())
birthday = []

for _ in range(n):
    name, *info = input().split()
    info = list(map(int, info))[::-1]
    birthday.append(info + [name])

birthday.sort()
print(birthday[-1][-1])
print(birthday[0][-1])