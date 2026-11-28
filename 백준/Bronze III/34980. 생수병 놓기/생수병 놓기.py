n = int(input())
s1 = input()
s2 = input()
c1, c2 = s1.count('w'), s2.count('w')
if c1 < c2:
    print("Manners maketh man")
elif c1 == c2:
    if s1 == s2:
        print("Good")
    else:
        print("Its fine")
else:
    print("Oryang")