import key_values as kv
import random as r

val = kv.d
flag = 0
size = int(input("Enter the size of the passwd : "))
passwd = ""
for i in range(1,size+1):
    rand_number = r.randint(1,97)
    k = val.get(rand_number)
    passwd += str(k)
print(passwd)
