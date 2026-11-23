n = int(input())
numlist = list(map(int, input().split()))
coin = 0

numlist.sort(reverse = True)

while len(numlist) > 1:
    coin += numlist[0] + numlist[1]
    numlist[0] = max(numlist[0], numlist[1])
    del numlist[1]

print(coin)