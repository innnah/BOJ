s = [6,3,2,1,2]
for _ in range(2):
    l = list(map(int, input().split()))
    ret = 0
    for i in range(5):
        ret += l[i] * s[i]
    print(ret, end = ' ')