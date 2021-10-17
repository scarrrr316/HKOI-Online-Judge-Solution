str_in,slicer=input(),input()
cnt = 0
for i in range(len(str_in)-len(slicer)+1):
    if str_in[i:i+len(slicer)] == slicer:
        cnt +=1
print(cnt)