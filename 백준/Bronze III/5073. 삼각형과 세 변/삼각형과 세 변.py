'''
Equilateral 3
Scalene 1
Invalid 0
Isosceles 2
'''

while True:
    numlist = list(map(int, input().split()))
    if numlist == [0,0,0]:
        break
    
    if sum(numlist) - max(numlist) <= max(numlist):
        print("Invalid")
    elif numlist[0] == numlist[1] and numlist[1] == numlist[2]:
        print("Equilateral")
    elif numlist[0] == numlist[1] or numlist[1] == numlist[2] or numlist[0] == numlist[2]:
        print("Isosceles")
    else:
        print("Scalene")