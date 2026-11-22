import sys
input = sys.stdin.readline

d = {2:1,3:7,4:4,5:2,6:6,7:8,8:10,9:18,10:22,11:20,12:28,13:68}
d2 = {1:'10',2:'1',3:'200',4:'20',5:'2',6:'6',0:''}
d3 = {1:8,2:2,3:17,4:11,5:5,6:6,0:0}
for _ in range(int(input())):
    n = int(input())
    mini, maxi = 0, 0
    if n <= 13:
        mini = d[n]
    else:
        mini = int(d2[n%7]+'8'*((n-d3[n%7]) // 7))
    if n%2:
        maxi = int('7'+'1'*((n-3)//2))
    else:
        maxi = int('1'*(n//2))
    print(mini, maxi)