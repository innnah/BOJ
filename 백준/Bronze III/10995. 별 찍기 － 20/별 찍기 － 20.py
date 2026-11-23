n = int(input())
spaceBar = False

for _ in range(n):
    if spaceBar:
        print(' ', end = '')
    spaceBar = not spaceBar
    for _ in range(n):
        print('*', end = ' ')
        
    print()