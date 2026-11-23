from collections import defaultdict

for _ in range(int(input())):
    s = input()
    d = defaultdict(int)
    for i in s:
        d[i] += 1
    ret = 0
    for i in range(ord('A'), ord('Z')+1):
        if d[chr(i)] == 0: ret += i
    print(ret)