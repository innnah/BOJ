import sys
input = sys.stdin.readline

def rome_to_arab(arr):
    num = 0
    i = 0
    while i < len(arr):
        if i == len(arr)-1:
            num += arr[i]
            i += 1
        else:
            if arr[i] < arr[i+1]:
                num += arr[i+1]-arr[i]
                i += 2
            else:
                num += arr[i]
                i += 1
    return num
def arab_to_rome(num):
    s = ""
    length = len(str(num))
    mul = 10**(length-1)
    while mul > 0:
        digit = num//mul
        if digit == 9:
            s += revd[mul]+revd[mul*10]
        else:
            if digit >= 5:
                s += revd[mul*5]
                digit -= 5
            if digit == 4:
                s += revd[mul]+revd[mul*5]
            else:
                s += revd[mul]*digit
        num %= mul
        mul //= 10
    return s

a = list(input().rstrip())
b = list(input().rstrip())
al = []
bl = []
d = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
revd = {1000:"M",500:"D",100:"C",50:"L",10:"X",5:"V",1:"I"}
for i in a:
    al.append(d[i])
for i in b:
    bl.append(d[i])
num_a, num_b = rome_to_arab(al), rome_to_arab(bl)
print(num_a+num_b)
print(arab_to_rome(num_a+num_b))