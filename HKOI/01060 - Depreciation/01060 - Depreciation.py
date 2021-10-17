import decimal #use this lib to prevent inaccuracies

decimal.getcontext().rounding = decimal.ROUND_DOWN

price, percent, period = list(map(eval,input().split()))
price = decimal.Decimal(price)

for i in range(period):
    price -= round(price*percent/100,2)

print(round(price,2))