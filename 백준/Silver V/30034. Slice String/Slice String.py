import sys
input = sys.stdin.readline

n = int(input())
sp1 = input().rstrip().split()
m = int(input())
sp2 = input().rstrip().split()
k = int(input())
merge = set(input().rstrip().split())
sp = set(sp1+sp2)-merge
input()
s = input().rstrip()
newline = 1
for i in s:
    if i == ' ':
        if not newline:
            print()
            newline = 1
    elif i in sp:
        if not newline:
            print()
            newline = 1
    else:
        print(i, end='')
        newline = 0