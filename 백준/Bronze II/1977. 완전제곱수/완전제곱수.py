import math

start = int(input())
end = int(input())
numlist = []

for x in range(start, end + 1):
    tmp = math.sqrt(x)
    
    if float(int(tmp)) == tmp:
        numlist.append(x)
        
if len(numlist) == 0:
    print(-1)
else:
    print(sum(numlist))
    print(min(numlist))