a = set()
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(1, 10):
                si = chr(i+48)
                sj = chr(j+48)
                sk = chr(k+48)
                sl = chr(l+48)
                a.add(min(int(si+sj+sk+sl), int(sj+sk+sl+si), int(sk+sl+si+sj), int(sl+si+sj+sk)))
a = list(a)
a.sort()
b = input().split()
num = 987654321
for i in range(4):
    cand = ""
    for j in range(i, i+4):
        cand += b[j%4]
    num = min(num, int(cand))
print(a.index(num)+1)