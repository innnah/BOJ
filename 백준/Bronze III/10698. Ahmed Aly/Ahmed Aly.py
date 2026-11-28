'''
4
1 + 23 = 22
1 + 22 = 23
22 - 1 = 23
23 - 1 = 22
예제 출력 1 
Case 1: NO
Case 2: YES
Case 3: NO
Case 4: YES
'''
for i in range(int(input())):
    s = input()
    sl = s[:s.find('=')].strip()
    sr = int(s[s.find('=')+1:].strip())
    if eval(sl) == sr:
        print(f"Case {i+1}: YES")
    else:
        print(f"Case {i+1}: NO")