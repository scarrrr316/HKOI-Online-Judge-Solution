[print(x['N'], x['M']) for x in sorted([{'N':input(),'M':int(input())} for i in range(int(input()))], key=lambda t: (t['M']*-1, t['N']))]
