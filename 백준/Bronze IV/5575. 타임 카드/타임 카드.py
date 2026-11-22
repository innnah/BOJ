for _ in range(3):
    a, b, c, d, e, f = map(int, input().split())
    t1 = a*3600 + b*60 + c
    t2 = d*3600 + e*60 + f
    et = t2-t1
    print(et//3600, (et%3600)//60, et%60)