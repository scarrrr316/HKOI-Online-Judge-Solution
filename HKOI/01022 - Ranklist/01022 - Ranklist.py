i = int(input())
names, marks ,dict_ = [] ,[] ,{}
for x in range(i):
    names.append(input())
    marks.append(int(input()))

for x in range(i):
    try:
        dict_[marks[x]].append(names[x])
    except:
        dict_[marks[x]] = [names[x]]

for _ in sorted(dict_,reverse=True):
    for __ in sorted(dict_[_]):
        print(__,_)
