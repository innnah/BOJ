import itertools, sys
input = sys.stdin.readline
while 1:
    k, *l = map(int, input().split())
    if k == 0: break
    ret = list(itertools.combinations(l, 6))
    for i in ret:
        print(*i)
    print()