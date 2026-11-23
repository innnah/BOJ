a = float(input())
b = float(input())
bmi = a/(b*b)
if bmi > 25:
    print("Overweight")
elif 18 < bmi <= 25:
    print("Normal weight")
else:
    print("Underweight")