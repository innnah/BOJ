places = [list(map(int, input().split())) for _ in range(3)]
x = [places[i][0] for i in range(3)]
y = [places[i][1] for i in range(3)]

if x.count(x[0]) == 1:
    print(x[0], end = ' ')
else:
    for a in x[1:]:
        if a != x[0]:
            print(a, end = ' ')
            
if y.count(y[0]) == 1:
    print(y[0], end = ' ')
else:
    for b in y[1:]:
        if b != y[0]:
            print(b, end = ' ')