#this is the crappy passwd encryptor 
#this is the final product 
import values as v
import actualval as av
ui = input("enter: ")
a = []
b = []
for i in ui:
    a.append(v.fd[i])
for i in a:
    b.append(av.d[i])
print(*b)
