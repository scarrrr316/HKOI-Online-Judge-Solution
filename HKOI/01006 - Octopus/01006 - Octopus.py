init = eval(input())
credit = 0
t = eval(input())
p = [eval(input()) for x in range(t)]
s = sum(p)

while s>=init:
    credit += 250
    s -= 250

print('$'+str(credit))

