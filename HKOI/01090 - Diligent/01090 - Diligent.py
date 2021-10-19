import  sys
n = eval(input())
data = [eval(sys.stdin.readline()) for i in range(n)]
log = {}
for _ in data:
    try:
        if log[_] == True:
            log[_] = False
            print('out')
        else:
            log[_] = True
            print('in')
    except KeyError:
        log[_] = True
        print('in')