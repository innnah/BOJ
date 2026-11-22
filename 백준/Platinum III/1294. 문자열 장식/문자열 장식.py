import sys
input = sys.stdin.readline

n = int(input())
pq = [input().rstrip() for _ in range(n)]
l = 0
for i in range(n):
    l += len(pq[i])
cnt = 0
ret = ''
while cnt < l:
    m = ''
    idx = -1
    for i in range(n):
        if len(m) < len(pq[i]):
            if m == pq[i][:len(m)]:
                m = pq[i]
                idx = i
            else:
                if m > pq[i]:
                    m = pq[i]
                    idx = i
        else:
            if m[:len(pq[i])] != pq[i]:
                if m > pq[i]:
                    m = pq[i]
                    idx = i
    pq[idx] = pq[idx][1:]
    ret += m[0]
    cnt += 1
print(ret)