name=" ebhad is the longest dattaprasad word in the sentence"
d=name.split()
long_s=[]

for i in d:
    if len(i)>len(long_s):
        long_s=i
        
print(long_s)
