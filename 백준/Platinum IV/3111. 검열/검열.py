import sys
input = sys.stdin.readline

a = input().rstrip()
s = input().rstrip()
ra = a[::-1]
i, j = 0, len(s)-1
st1, st2 = [], []
while 1:
    while i <= j:
        st1.append(s[i])
        i += 1
        if len(st1) >= len(a):
            for k in range(len(a)):
                if st1[len(st1)-1-k] != ra[k]:
                    break
            else:
                for _ in range(len(a)):
                    st1.pop()
                break
    if i > j:
        break
    while j >= i:
        st2.append(s[j])
        j -= 1
        if len(st2) >= len(ra):
            for k in range(len(ra)):
                if st2[len(st2)-1-k] != a[k]:
                    break
            else:
                for _ in range(len(ra)):
                    st2.pop()
                break
    if j < i:
        break
s2 = st1 + st2[::-1]
i = 0
st3 = []
while i < len(s2):
    st3.append(s2[i])
    i += 1
    if len(st3) >= len(a):
        for k in range(len(a)):
            if st3[len(st3)-1-k] != ra[k]:
                break
        else:
            for _ in range(len(a)):
                st3.pop()
print(''.join(st3))