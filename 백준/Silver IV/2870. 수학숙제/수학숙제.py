n = int(input())
words = [input().rstrip() for _ in range(n)]
numlist = []
for x in words:
    num = ""
    for i in x:
        if i.isalpha():
            if num != '':
                numlist.append(int(num))
                num = ""
        else:
            num += i

    if num != '':
        numlist.append(int(num))
            
numlist.sort()

for x in numlist:
    print(x)