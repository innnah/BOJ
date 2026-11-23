for _ in range(int(input())):
    n = int(input())
    numlist = [int(input()) for _ in range(n)]
    total = sum(numlist)
    maximum = max(numlist)
    
    if numlist.count(maximum) > 1:
        print("no winner")
    elif maximum / total > 0.5:
        print(f"majority winner {numlist.index(maximum) + 1}")
    else:
        print(f"minority winner {numlist.index(maximum) + 1}")