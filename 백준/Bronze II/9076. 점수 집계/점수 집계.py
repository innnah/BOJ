for _ in range(int(input())):
    numlist=list(map(int,input().split()))
    numlist.remove(max(numlist))
    numlist.remove(min(numlist))
    if max(numlist)-min(numlist)>=4:
        print("KIN")
    else:
        print(sum(numlist))