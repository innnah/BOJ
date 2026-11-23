from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
def my_round(in_number, ndigits=0, rounding_rule=1):
    if ndigits > 0:
        expression = '0.' + '0'*ndigits
        number = in_number
    else:
        expression = '0'
        number = in_number / (10**(-ndigits))
    
    if rounding_rule == 2:
        round_number = Decimal(number).quantize(Decimal(expression), rounding=ROUND_HALF_EVEN)
    else:
        round_number = Decimal(number).quantize(Decimal(expression), rounding=ROUND_HALF_UP)
    
    if ndigits > 0:
        return float(round_number)
    else:
        return int(round_number * (10**(-ndigits)))

n = int(input())
for i in range(-1, -len(str(n)), -1):
    n = my_round(n, i)

print(n)