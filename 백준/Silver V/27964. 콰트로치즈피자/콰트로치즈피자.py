import sys
input = sys.stdin.readline

d = set()
n = int(input())
l = input().rstrip().split()
for i in l:
    if i[-6:] == "Cheese":
        d.add(i)
if len(d) >= 4:
    print("yummy")
else:
    print("sad")