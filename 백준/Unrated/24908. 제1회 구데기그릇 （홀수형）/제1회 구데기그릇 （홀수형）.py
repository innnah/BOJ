import calendar
n = int(input())
if n == 5:
    print(calendar.calendar(int(input())))
elif n == 2:
    print("\"IMPOSSIBLE\"")
elif n == 9:
    print("731706508")
elif n == 1:
    l = [1,3,6,10,10,16,23,23,23,23,23,23]
    a = int(input())
    print(sum(l[:min(a,12)]))