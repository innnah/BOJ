for _ in range(int(input())):
    l = input().split()
    l[1] = int(l[1])
    l[2] = int(l[2])
    print(l[0][:l[1]] + l[0][l[2]:])