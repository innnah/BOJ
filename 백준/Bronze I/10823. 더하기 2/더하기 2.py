import sys
r=sys.stdin.readlines
l=r()
l=''.join([i.rstrip()for i in l])
print(sum(map(int,l.split(','))))