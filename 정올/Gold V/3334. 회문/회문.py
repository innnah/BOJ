import sys

input = sys.stdin.readline

def isP_Palindrome(s):
    i, j = 0, len(s)
    while i < j:
        if s[i] != s[j-1]:
            return s[i+1:j] == s[i+1:j][::-1] or s[i:j-1] == s[i:j-1][::-1]
        i += 1
        j -= 1
    return True

n = int(input())
for _ in range(n):
    s = input().rstrip()
    if s == s[::-1]:
        print(0)
        continue
    if isP_Palindrome(s):
        print(1)
    else:
        print(2)