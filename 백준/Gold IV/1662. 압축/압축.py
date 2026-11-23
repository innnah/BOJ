def unzip(s):
    if len(s) == 0: return 0

    length = 0
    stack = 0

    i = 0 # s에서 현재 인덱스
    while i < len(s) - 1:
        ### 다음 문자가 '('가 아닌 다른 문자가 온다면 s[i]는 일반 문자이다.
        if s[i+1] != '(':
            length += 1
            i += 1
            continue

        ### 다음 문자가 '('가 온다면 s[i]는 반복 횟수이다.
        coef = int(s[i]) # 반복 횟수

        stack += 1
        idx = i+1 # 왼쪽 괄호 다음 인덱스부터 시작해서 stack이 빌 때까지 오른쪽 괄호를 찾는다.
        while stack > 0:
            idx += 1
            if s[idx] == '(': stack += 1
            if s[idx] == ')': stack -= 1
        # while문을 벗어나면 idx는 닫는 괄호를 가리킨다.

        midLength = unzip(s[i+2:idx]) # 괄호 안의 문자열에 대해 unzip()을 호출한다.
        length += coef*midLength

        i = idx + 1 # 괄호 다음으로 건너뛴다.

    if s[-1] != ')': length+=1

    return length

s = input()
print(unzip(s))