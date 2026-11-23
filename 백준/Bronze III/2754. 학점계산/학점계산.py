s = input()
dic1 = {'A':4.0, 'B':3.0, 'C':2.0, 'D':1.0, 'F':0.0}
dic2 = {'+':0.3, '0':0.0, '-':-0.3}
try:
    print(dic1[s[0]] + dic2[s[1]])
except:
    print(dic1[s[0]])