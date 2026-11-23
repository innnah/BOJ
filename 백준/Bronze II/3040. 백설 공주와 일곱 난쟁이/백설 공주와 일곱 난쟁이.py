taken_heights = [[False, int(input())] for _ in range(9)]

def findSumOfHeight(taken, heights = [], total = 0):
    if total == 100 and len(heights) == 7:
        return heights

    if len(heights) == 7:
        return [-1]

    firstFree = -1

    for i in range(len(taken)):
        if taken[i][0] == False:
            firstFree = i
            break

    for x in range(firstFree, 9):
        if not taken[x][0]:
            taken[x][0] = True
            ret = findSumOfHeight(taken, heights + [taken[x][1]], total + taken[x][1])
            if ret != [-1]:
                return ret
            taken[x][0] = False

        continue

    return [-1]

result = findSumOfHeight(taken_heights)
result.sort()

for x in result:
    print(x)