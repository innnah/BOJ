n = int(input())
a = (n//100)*100-1
b = a+100
if n <= 99:
    print(99)
elif n-a >= b-n:
    print(b)
else:
    print(a)