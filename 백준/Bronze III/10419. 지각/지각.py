for _ in range(int(input())):
    a = int(input())
    i = 0
    while i*(i+1) <= a: i += 1
    print(i-1)