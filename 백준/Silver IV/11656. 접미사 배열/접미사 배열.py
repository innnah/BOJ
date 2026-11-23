s = input().rstrip()
sub = []

for i in range(0, len(s)):
    sub.append(s[i:])

sub.sort()

for i in sub:
    print(i)