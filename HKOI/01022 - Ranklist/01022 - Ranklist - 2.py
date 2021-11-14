n = int(input())
entry = []

for x in range(n):
    this = {}
    this['Name'] = input()
    this['Mark'] = int(input())
    entry.append(this)

entry = sorted(entry, key=lambda t: (t['Mark']*-1, t['Name']))

for x in entry:
    print(x['Name'], x['Mark'])
