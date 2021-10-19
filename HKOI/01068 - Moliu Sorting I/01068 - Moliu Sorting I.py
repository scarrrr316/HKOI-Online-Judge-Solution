out = {}
temp = []
for i in range(eval(input())):
    ab = input()
    a ,b = ab.split()
    a ,b = eval(a)**2,eval(b)**2
    temp.append(ab)
    out[str(ab)] = a+b
out_ = [*out]
out_v = list(out.values())
out_v_s = sorted(out_v)

for i in out_v_s:
    print(list (out.keys()) [list (out.values()).index (i)])