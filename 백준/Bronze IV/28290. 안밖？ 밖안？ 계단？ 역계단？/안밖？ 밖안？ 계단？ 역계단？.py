d = {"fdsajkl;" : "in-out", "jkl;fdsa" : "in-out", "asdf;lkj" : "out-in", ";lkjasdf" : "out-in", "asdfjkl;" : "stairs", ";lkjfdsa" : "reverse"}
s=input()
if d.get(s) is None:
    print("molu")
else:
    print(d[s])