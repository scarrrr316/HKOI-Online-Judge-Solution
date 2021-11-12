f_in = open('score.in','r')
f_out = open('score.out','w')

m = list(map(eval,f_in.readline().split()))

m_ = m[0]*20/100+ m[1]*30/100+ m[2]*50/100

f_out.write(f'{int(m_)}')