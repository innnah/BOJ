for _ in range(int(input())):
    n=int(input())
    num=bin(n)[2:][::-1]
    for i in range(len(num)):
        if num[i]=='1':print(i,end=' ')
    print()