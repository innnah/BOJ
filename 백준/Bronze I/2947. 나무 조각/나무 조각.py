numlist = list(map(int, input().split()))
step = 0

while numlist != [1,2,3,4,5]:
    if numlist[step] > numlist[step + 1]:
        numlist[step], numlist[step + 1] = numlist[step + 1], numlist[step]
        for x in numlist:
            print(x, end = ' ')
        print()
    
    if step == 3:
        step = 0
    else:
        step += 1