'''
각각 만렙 = 
$300$, 구만렙 = 
$275$, 뀨만렙 = 
$250$이라는 용어가 존재한다.

모든 레벨은 만렙(구간 1), 구만렙이상 만렙 미만(구간 2), 뀨만렙이상 구만렙 미만(구간 3), 
뀨만렙 미만(구간 4) 에 속하게 된다.
'''
n = int(input())
l = list(map(int, input().split()))
for i in range(n):
    if l[i] >= 300:
        print(1, end = ' ')
    elif l[i] >= 275:
        print(2, end = ' ')
    elif l[i] >= 250:
        print(3, end = ' ')
    else:
        print(4, end = ' ')