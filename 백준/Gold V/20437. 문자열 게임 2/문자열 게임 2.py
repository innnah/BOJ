import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().rstrip()
    k = int(input())
    a = [[] for _ in range(26)]
    for i in range(len(s)):
        a[ord(s[i])-97].append(i)
    reta, retb = 987654321, 0
    for i in range(26):
        if len(a[i]) < k: continue
        for j in range(len(a[i])-k+1):
            reta = min(reta, a[i][j+k-1] - a[i][j])
            retb = max(retb, a[i][j+k-1] - a[i][j])
    if reta == 987654321 and retb == 0:
        print(-1)
    else:
        print(reta+1, retb+1)