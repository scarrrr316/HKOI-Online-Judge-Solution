addr = input()
cnt = 0

if addr.count(',') !=5:
    print('Invalid')
else:
    addr = addr.split(',')
    for _ in addr:
        if _.isspace() or _=='':
            cnt += 1
    print(cnt)