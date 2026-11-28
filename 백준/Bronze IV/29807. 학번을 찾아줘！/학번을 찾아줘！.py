n = int(input())
l = list(map(int, input().split()))
l += [0 for i in range(5-n)]
a = abs(l[2]-l[0]) * (108+(l[0]>l[2])*400)
b = abs(l[1]-l[3]) * (305-(l[1]>l[3])*93)
c = l[4]*707
print((a+b+c)*4763)