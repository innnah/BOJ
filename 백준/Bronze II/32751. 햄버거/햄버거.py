import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
s = input().rstrip()

if not (s[0] == 'a' and s[-1] == 'a'):
    print("No")
    sys.exit(0)

for i in range(n-1):
    if s[i] == s[i+1]:
        print("No")
        sys.exit(0)

for i in range(4):
    if arr[i] < s.count(chr(i+97)):
        print("No")
        sys.exit(0)

print("Yes")