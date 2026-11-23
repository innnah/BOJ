n = int(input())
numlist = []

for _ in range(n):
    k = int(input())
    if k == 0:
        del numlist[-1]
    else:
        numlist.append(k)
        
print(sum(numlist))