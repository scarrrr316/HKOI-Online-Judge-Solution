f = open('account.txt')
n = eval(f.readline())
b=0
for i in range(n):
    b+=eval(f.readline())

print(b)