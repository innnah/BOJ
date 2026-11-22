for _ in range(int(input())):
    n = int(input())
    print(f"Pairs for {n}: ", end='')
    if n%2==0:
        for i in range(1, n//2):
            print(f"{i} {n-i}", end = '')
            if i != n//2-1:
                print(", ", end = '')
    else:
        for i in range(1, (n+1)//2):
            print(f"{i} {n-i}", end = '')
            if i != (n+1)//2-1:
                print(", ", end = '')
    print()