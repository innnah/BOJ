'''
하얀색(w)이 존재한다면 춘배, 검은색(b)이 존재한다면 나비, 회색(g)이 존재한다면 영철의 사진이다.
'''
for i in range(15):
    s = input()
    if 'w' in s:
        print("chunbae")
        break
    elif 'b' in s:
        print("nabi")
        break
    elif 'g' in s:
        print("yeongcheol")
        break