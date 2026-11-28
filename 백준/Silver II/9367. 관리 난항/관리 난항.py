import sys
from collections import defaultdict
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    cars = {}
    for _ in range(n):
        name, price, pickup, dist = input().rstrip().split()
        price = int(price)
        pickup = int(pickup)
        dist = int(dist)
        cars[name] = (price, pickup, dist)
    state = defaultdict(str)
    ans = defaultdict(int)
    for _ in range(m):
        t, pn, q, x = input().rstrip().split()
        t = int(t)
        if ans[pn] == -1:
            continue
        if q == 'p':
            if state[pn] != '':
                ans[pn] = -1
            else:
                state[pn] = x
                ans[pn] += cars[x][1]
        elif q == 'r':
            x = int(x)
            if state[pn] == '':
                ans[pn] = -1
            else:
                ans[pn] += cars[state[pn]][2] * x
                state[pn] = ''
        elif q == 'a':
            x = int(x)
            if state[pn] == '':
                ans[pn] = -1
            else:
                ans[pn] += (cars[state[pn]][0] * x + 99) // 100
    persons = sorted(ans.keys())
    for person in persons:
        if ans[person] == -1 or state[person] != '':
            print(person, "INCONSISTENT")
        else:
            print(person, ans[person])