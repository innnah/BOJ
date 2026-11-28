import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().rstrip()
    s_ = s[:(len(s)+2)//3]
    rev_s_ = s_[::-1]
    tail_s_ = s_[1:]
    tail_rev_s = rev_s_[1:]
    print(int(s in (s_ + rev_s_ + s_, s_ + tail_rev_s + s_, s_ + rev_s_ + tail_s_, s_ + tail_rev_s + tail_s_)))