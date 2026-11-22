for _ in range(int(input())):
    input()
    n = int(input())
    if sum([int(input()) for _ in range(n)]) % n == 0:
        print("YES")
    else:
        print("NO")