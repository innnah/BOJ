n = int(input())
numlist = list(map(int, input().split()))
numlist.sort()
total = sum(numlist)
money = 0

for x in numlist:
    total -= x
    money += total * x
    
print(money)