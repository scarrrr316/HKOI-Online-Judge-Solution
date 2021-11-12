f_in = open('title.in','r')
str_in = f_in.read()

str_out = str_in.replace(' ','').replace('\n','')

f_out = open('title.out','w')
f_out.write(str(len(str_out)))