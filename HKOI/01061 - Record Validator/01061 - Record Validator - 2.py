import re
x = input()

if (x.count(",") == 5):
    print(len(re.findall("^ *(?=,)|, *?(?=,)|, *?$", x,)))
    
else:
    print ("Invalid")
