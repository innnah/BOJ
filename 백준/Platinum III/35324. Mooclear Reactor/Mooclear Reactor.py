import sys
sys.setrecursionlimit(210000)
input = sys.stdin.readline

def get_exp(v, p):
    groups[-1].append(v)
    for nxt, val in graph[v]:
        if nxt == p: continue
        if exp[nxt][0] == -2:
            exp[nxt] = [-exp[v][0], val-exp[v][1]]
            get_exp(nxt, v)

for _ in range(int(input())):
    flag = 0

    n, m = map(int, input().split())
    left = list(map(int, input().split()))
    right = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    exp = [[-2, 0] for _ in range(n+1)]
    groups = []
    flag = 0
    for i in range(1, n+1):
        if exp[i][0] == -2:
            groups.append([])
            exp[i][0] = 1
            ret = get_exp(i, -1)

    for group in groups:
        xval = (0, 0)
        for i in group:
            for j, val in graph[i]:
                if exp[i][0] + exp[j][0] == 0 and exp[i][1] + exp[j][1] != val:
                    flag = 1
                    break
                elif exp[i][0] + exp[j][0] != 0:
                    a, b = exp[i][0] + exp[j][0], val - (exp[i][1] + exp[j][1])
                    if b % a:
                        flag = 1
                        break
                    xval = (1, b//a)
        if xval[0] == 1:
            x = xval[1]
            for i in group:
                exp[i] = [0, exp[i][0]*x+exp[i][1]]
    if flag:
        print(-1)
        continue

    for i in range(1, n+1):
        for j, val in graph[i]:
            if [exp[i][0] + exp[j][0], exp[i][1] + exp[j][1]] != [0, val]:
                flag = 1
                break
    if flag:
        print(-1)
        continue

    ans = 0
    for group in groups:
        if exp[group[0]][0] != 0:
            ranges = []
            nums = []
            for v in group:
                if exp[v][0] == 1:
                    ranges.append([left[v-1]-exp[v][1], right[v-1]-exp[v][1]])
                    nums += [left[v-1]-exp[v][1], right[v-1]-exp[v][1], right[v-1]-exp[v][1]+1]
                else:
                    ranges.append([exp[v][1]-right[v-1], exp[v][1]-left[v-1]])
                    nums += [exp[v][1]-right[v-1], exp[v][1]-left[v-1], exp[v][1]-left[v-1]+1]
            snums = sorted(list(set(nums)))
            dic = {snums[i] : i for i in range(len(snums))}
            psum = [0 for _ in range(len(snums)+1)]
            for ran in ranges:
                psum[dic[ran[0]]] += 1
                psum[dic[ran[1]+1]] -= 1
            for i in range(1, len(snums)):
                psum[i] += psum[i-1]
            ans += max(psum)
        else:
            for v in group:
                if left[v-1] <= exp[v][1] <= right[v-1]:
                    ans += 1
    print(ans)