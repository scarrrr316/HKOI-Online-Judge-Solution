print((lambda d: "$"+str(d.Decimal(str(float(input().replace("$",""))/2)).quantize(d.Decimal('0.1'), rounding=d.ROUND_HALF_UP)))(__import__('decimal')))