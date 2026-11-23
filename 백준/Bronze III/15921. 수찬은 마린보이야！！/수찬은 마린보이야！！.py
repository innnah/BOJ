n = int(input())
if n == 0:
    print("divide by zero")
else:
    numlist = list(map(int, input().split()))
    average = sum(numlist) / n
    total = 0
    for x in list(set(numlist)):
        total += x * (numlist.count(x) / n)
    if total != 0:
        print("{0:.2f}".format(average / total))
    else:
        print("divide by zero")