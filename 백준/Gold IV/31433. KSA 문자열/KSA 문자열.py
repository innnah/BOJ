import sys
input = sys.stdin.readline

string = input().rstrip()
k = 0
s = 0
a = 0
st = 'KSA'
for i in range(3):
    state = i
    ans = 0
    for j in range(len(string)):
        if string[j] == st[state]:
            state += 1
            state %= 3
        else:
            ans += 1
    if i == 0:
        k = ans*2
    if i == 1:
        s = max(ans*2, 2)
    if i == 2:
        a = max(ans*2, 4)
print(min(k, s, a))