import math
x, y = list(map(float,input().split()))

tri_area = x * y  / 2
circle_area = math.pi* (x / 4)**2
print('%.10f' % (tri_area+circle_area))