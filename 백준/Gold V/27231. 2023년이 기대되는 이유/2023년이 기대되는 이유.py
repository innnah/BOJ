import sys
input = sys.stdin.readline

def find_all_sum(idx, s):
    if idx == len(sn):
        l.append(s)
        return
    a = ""
    for i in range(idx, len(sn)):
        a += sn[i]
        find_all_sum(i+1, s+int(a))

for _ in range(int(input())):
    n = int(input())
    sn = str(n)
    l = []
    find_all_sum(0, 0)
    l.sort()
    ln = list(map(int, sn))
    ret = 0
    for i in range(1, 1000):
        c = []
        for j in range(len(ln)):
            c.append(ln[j] ** i)
        if sum(c) > l[-1]:
            print(ret)
            break
        if sum(c) in l:
            ret += 1
    else:
        print("Hello, BOJ 2023!")