import sys
input = sys.stdin.readline

def dpf(s, e):
    if s == e:
        return [0, [arr[s]]]
    if dp[s][e] != [-1, []]: return dp[s][e]
    ret = [987654321, []]
    for i in range(s, e):
        v1 = dpf(s, i)
        v2 = dpf(i+1, e)
        cand = v1[0]+v2[0]+1
        possible = []
        idx1, idx2 = 0, 0
        a, b = idx1 != len(v1[1])-1, idx2 != len(v2[1])-1
        while a or b:
            if v1[1][idx1] == v2[1][idx2]:
                possible.append(v1[1][idx1])
                if a:
                    idx1 += 1
                else:
                    idx2 += 1
            elif b and v1[1][idx1] > v2[1][idx2]:
                idx2 += 1
            elif a and v1[1][idx1] < v2[1][idx2]:
                idx1 += 1
            else:
                break
            if idx1 == len(v1[1])-1:
                a = 0
            if idx2 == len(v2[1])-1:
                b = 0
        if v1[1][-1] == v2[1][-1]:
            possible.append(v1[1][-1])
        if possible:
            cand -= 1
            if ret[0] >= cand:
                ret[0] = cand
                ret[1] = possible.copy()
        else:
            if ret[0] >= cand:
                ret[0] = cand
                ret[1] = sorted(list(set(v1[1]) | set(v2[1])))
    dp[s][e] = ret
    return ret

n, k = map(int, input().split())
tmp = list(map(int, input().split()))
arr = [tmp[0]]
for i in range(1, n):
    if tmp[i] != tmp[i-1]:
        arr.append(tmp[i])
n = len(arr)
dp = [[[-1, []] for _ in range(n)] for _ in range(n)]
print(dpf(0, n-1)[0])