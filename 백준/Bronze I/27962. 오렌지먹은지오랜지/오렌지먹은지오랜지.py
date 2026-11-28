import sys
input = sys.stdin.readline
n = int(input())
s = input().rstrip()
s1, s2 = "", ""
for i in range(n):
    s1 += s[i]
    s2 = s[n-i-1] + s2
    dif = 0
    for j in range(len(s1)):
        if s1[j] != s2[j]:
            if dif:
                dif = 2
                break
            else:
                dif = 1
    if dif == 1:
        print("YES")
        break
else:
    print("NO")