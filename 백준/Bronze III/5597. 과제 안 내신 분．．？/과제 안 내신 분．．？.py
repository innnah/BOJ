numlist = [i for i in range(1, 31)]

for _ in range(28):
    numlist.remove(int(input()))
    
print(numlist[0])
print(numlist[1])