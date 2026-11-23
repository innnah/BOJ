import sys
input = sys.stdin.readline

INF = 10 ** 15
n = int(input())
if n == 1: 
    print(0)
    sys.exit(0)
l = [list(map(int, input().split())) for _ in range(n)] + [[INF, INF]]
l.sort()
end = p = q = -1
shortest = INF
full_length = 0
for i in range(n):
    s = max(end, l[i][0])
    e = min(l[i+1][0], l[i][1])
    shortest = max(0, min(shortest, e-s))
    if l[i][0] < q: q = max(q, l[i][1])
    else:
        full_length += q-p
        p, q = l[i]
    end = l[i][1]
    #print(s, e, shortest, end)
full_length += q-p
print(full_length-shortest)