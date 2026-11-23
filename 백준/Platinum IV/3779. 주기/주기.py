import sys
input = sys.stdin.readline
print = sys.stdout.write

def getPi(s):
    m = len(s)
    pi = [0 for _ in range(m+1)]
    begin, matched = 1, 0
    while begin + matched < m:
        if s[begin + matched] == s[matched]:
            matched += 1
            pi[begin + matched] = matched
        else:
            if matched == 0: begin += 1
            else:
                begin += matched - pi[matched]
                matched = pi[matched]
    return pi

cnt = 1
while True:
    n = int(input())
    if n == 0: break
    s = input().rstrip()
    pi = getPi(s)
    print(f"Test case #{cnt}\n")
    for i in range(1, len(pi)):
        if pi[i] != 0 and pi[i] % (i-pi[i]) == 0: print(f"{i} {pi[i]//(i-pi[i])+1}\n")
    cnt += 1
    print("\n")