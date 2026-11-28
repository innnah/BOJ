from collections import defaultdict
a = defaultdict(int)
s = input()
for i in s:
    a[i] += 1
odd = 1
even = 1
for i in a.values():
    if i%2:
        even = 0
    else:
        odd = 0
if even == 0 and odd == 0:
    print('0/1')
elif even == 0:
    print('1')
else:
    print('0')