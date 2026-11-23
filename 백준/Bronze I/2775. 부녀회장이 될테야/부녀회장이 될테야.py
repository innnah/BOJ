cache = [[0 for _ in range(14)] for _ in range(100)]

def housePeople(floors, no):
    global cache
    if floors == 0:
        return no

    if cache[floors - 1][no - 1] == 0:
        for x in range(1, no + 1):
            tmp = housePeople(floors - 1, x)
            cache[floors - 1][no - 1] += tmp
    
    return cache[floors - 1][no - 1]

for _ in range(int(input())):
    k = int(input())
    n = int(input())
    print(housePeople(k, n))