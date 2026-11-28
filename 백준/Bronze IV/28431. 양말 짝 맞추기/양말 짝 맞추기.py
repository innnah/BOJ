l=[int(input())for _ in range(5)]
s=set(l)
for i in s:
    if l.count(i)%2:
        print(i)
        break