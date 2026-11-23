import sys
input = sys.stdin.readline
def digitalRoute(n):
    sn = str(n)
    ret = 0
    for i in sn:
        ret += int(i)
    return ret
while True:
    n = int(input())
    if n == 0: break
    while len(str(n)) > 1:
        n = digitalRoute(n)
    print(n)