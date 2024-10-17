fd = dict()
j = 26
k = 52
for i in range(65,78):
    fd.update({chr(i):j})
    j-=1

for i in range(110,123):
    fd.update({chr(i):j})
    j-=1

for i in range(97,110):
    fd.update({chr(i):k})
    k-=1

for i in range(78,91):
    fd.update({chr(i):k})
    k-=1

# finally i created unique values for all alphabets(including upper case and lower case) totallly 52 characters
for i in range(91,97):
     fd.update({chr(i):j})
     j+=1

for i in range(33,49):
     fd.update({chr(i):j})
     j+=1


for i in range(123,127):
    fd.update({chr(i):j})
    j+=1
    
for i in range(49,65):
     fd.update({chr(i):j})
     j+=1

# finally i created unique values for each special characters (total 43 characters)
print(fd)