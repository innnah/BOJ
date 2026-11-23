n = int(input())
for _ in range(n):
    a = input()
    s = 0
    for i in a:
        if i.isalpha():
            s += ord(i)-64
    print([s,"PERFECT LIFE"][s==100])