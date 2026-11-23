import sys
sys.setrecursionlimit(10**5)

def deleteString(s):
    if len(s) <= 1:
        if len(s) == 0: return 1
        return 0
    cnt = 1
    flag = False
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            if cnt >= 2: 
                flag = flag or deleteString(s[:i-cnt] + s[i:])
            cnt = 1
        else:
            cnt += 1
    if cnt >= 2: flag = flag or deleteString(s[:len(s)-cnt])
    return int(flag)

for _ in range(int(input())):
    s = input()
    print(deleteString(s))