a, b, v = map(int, input().split())

up = a - b
tmp = (v-a) // up
days = tmp + 1

if (v-a) % up == 0:
    print(days)
else:
    print(days + 1)