n = int(input())

for _ in range(n):
    rangenum, string = map(str, input().split())
    rangenum = int(rangenum)
    
    for x in string:
        for _ in range(rangenum):
            print(x, end = '')
            
    print()