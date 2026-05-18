s = "This is a duplicate word in the sentence. This will help to find the duplicate words in the sentence."
y = s.split()
d = {}
for i in y:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)
