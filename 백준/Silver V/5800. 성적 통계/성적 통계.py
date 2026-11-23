for i in range(1, int(input()) + 1):
    print(f"Class {i}")
    a, *numlist = map(int, input().split())
    sub = []
    maximum = max(numlist)
    minimum = min(numlist)
    numlist.sort(reverse = True)
    for i in range(len(numlist) - 1):
        sub.append(abs(numlist[i] - numlist[i + 1]))
        
    maxsub = max(sub)
    
    print(f"Max {maximum}, Min {minimum}, Largest gap {maxsub}")