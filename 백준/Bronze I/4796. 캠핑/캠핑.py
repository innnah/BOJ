i = 1
while True:
    l, r, v = map(int, input().split())
    if [l,r,v] == [0,0,0]:
        break
    print(f"Case {i}:", end = ' ')
    days = 0
    days += (v // r) * l
    days += v % r if v % r < l else l
    print(days)
    i += 1