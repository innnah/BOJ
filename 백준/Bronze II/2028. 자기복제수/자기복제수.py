for _ in range(int(input())):
    n = int(input())
    if int(str(n**2)[-len(str(n)):]) == n:
        print("YES")
    else:
        print("NO")