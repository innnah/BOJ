n = int(input())
m = int(input())
if n >= m:
    print("Congratulations, you are within the speed limit!")
elif m-n <= 20:
    print(f"You are speeding and your fine is $100.")
elif m-n <= 30:
    print(f"You are speeding and your fine is $270.")
else:
    print(f"You are speeding and your fine is $500.")