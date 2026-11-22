a = [int(input()) for _ in range(4)]
if a == [a[0]] * 4: print("Fish At Constant Depth")
elif a[3] < a[2] < a[1] < a[0]: print("Fish Diving")
elif a[0] < a[1] < a[2] < a[3]: print("Fish Rising")
else: print("No Fish")