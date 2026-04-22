a=[1,2,4,3,2,4,5,5]
b={}
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print(b)