n = int(input())
stars = n * 2 - 1
multi = stars
down = True

for _ in range(stars):
    print(' ' * ((stars - multi) // 2) + '*' * multi)
    if multi == 1:
        down = False

    if down:
        multi -= 2
    else:
        multi += 2