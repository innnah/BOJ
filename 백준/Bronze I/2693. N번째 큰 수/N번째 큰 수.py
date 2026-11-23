for _ in range(int(input())):
    numlist = list(map(int, input().split()))
    
    numlist.remove(max(numlist))
    numlist.remove(max(numlist))
    
    print(max(numlist))