for _ in range(int(input())):
    l=list(map(int, input().split()))
    s = 0
    mini = 987654321
    for i in l:
        if i % 2 == 0:
            s += i
            mini = min(mini, i)
    print(s, mini)