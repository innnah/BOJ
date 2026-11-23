import sys
input = sys.stdin.readline

s = '#' + '#'.join(input().rstrip()) + '#'
n = len(s)
a = [0 for _ in range(n)]
ret = 0
def manachers():
    global ret
    r, p = 0, 0
    for i in range(n):
        if i <= r:
            a[i] = min(a[2*p-i], r-i)
        else:
            a[i] = 0
        
        while i - a[i] - 1 >= 0 and i + a[i] + 1 < n and s[i - a[i] - 1] == s[i + a[i] + 1]:
            a[i] += 1
        
        ret += (a[i]+1) // 2
        if r < i + a[i]:
            r = i + a[i]
            p = i
manachers()
print(ret)