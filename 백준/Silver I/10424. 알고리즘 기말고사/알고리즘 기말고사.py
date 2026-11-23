n = int(input())
numlist = list(map(int, input().split()))
indexes = [[numlist[i], i] for i in range(n)]
indexes.sort()

for i in range(n):
    index = indexes[i][1]
    print(numlist[index] - (index + 1))