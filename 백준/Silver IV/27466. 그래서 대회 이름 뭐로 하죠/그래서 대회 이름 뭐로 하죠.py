import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s = input().rstrip()
if s.count('A') < 2:
    print('NO')
    sys.exit(0)
idxa = []
for i in range(n-1, -1, -1):
    if s[i] == 'A':
        idxa.append(i)
    if len(idxa) == 2:
        break
consonent = ''
for i in range(idxa[0]+1, n):
    if s[i] not in ('A', 'E', 'I', 'O', 'U'):
        consonent = s[i]
        break
else:
    print("NO")
    sys.exit(0)
pop = idxa[0] - idxa[1] - 1 + n - idxa[0] - 2
if pop > n-m:
    print("NO")
    sys.exit(0)
ret = ""
for i in range(m-3):
    ret += s[i]
ret += "AA" + consonent
print("YES")
print(ret)