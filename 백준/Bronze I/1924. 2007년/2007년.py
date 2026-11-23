import calendar
yoil = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
n, m = map(int, input().split())
day = calendar.weekday(2007, n, m)
print(yoil[day])