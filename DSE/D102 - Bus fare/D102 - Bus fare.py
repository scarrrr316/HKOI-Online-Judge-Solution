import decimal
# from decimal import Decimal
m = input().replace("$","")
m_str = str(float(m/2))
print("$",end='')
print(str(decimal.Decimal(m_str).quantize(decimal.Decimal('0.1'), rounding=decimal.ROUND_HALF_UP)))
