from collections import defaultdict
a = input()
b = list(map(int, input().split()))
ret = 0
for i in range(1,7):
    for j in range(1,7):
        cand = 0
        b.append(i)
        b.append(j)
        l = list(sorted(b))
        for k in range(6):
            if a[k] == "Y":
                cand = max(cand, l.count(k+1) * (k+1))
        if a[6] == "Y":
            d = defaultdict(int)
            for k in l:
                d[k] += 1
            for k in range(1,7):
                if d[k] >= 4:
                    cand = max(cand, k*4)
                    break
        if a[7] == "Y":
            d = defaultdict(int)
            for k in l:
                d[k] += 1
            if list(d.values()) in [[3,2],[2,3]]:
                cand = max(cand, sum(l))
        if a[8] == "Y":
            if l == [1,2,3,4,5]: cand = max(cand, 30)
        if a[9] == "Y":
            if l == [2,3,4,5,6]: cand = max(cand, 30)
        if a[10] == "Y":
            for k in range(1,7):
                if l.count(k) == 5:
                    cand = max(cand, 50)
                    break
        if a[11] == "Y":
            cand = max(cand, sum(l))
        ret = max(cand, ret)
        b.pop()
        b.pop()
print(ret)