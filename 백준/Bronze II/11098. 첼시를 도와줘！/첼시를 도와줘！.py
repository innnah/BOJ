for _ in range(int(input())):
    n = int(input())
    name = [input().split() for _ in range(n)]
    for i in range(n):
        name[i][0] = int(name[i][0])
    name.sort(reverse = True)
    print(name[0][-1])