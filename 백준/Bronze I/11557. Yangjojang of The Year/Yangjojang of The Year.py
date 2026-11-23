for _ in range(int(input())):
    n = int(input())
    tmp = [input().rstrip().split()[::-1] for _ in range(n)]
    schools = [[int(tmp[i][0]), tmp[i][1]] for i in range(n)]
    schools.sort()
    print(schools[-1][1])