n = int(input())
a = [input() for _ in range(n)]
for i in a:
    if i[::-1] in a:
        print(len(i), i[len(i)//2])
        break