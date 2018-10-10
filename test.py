import os.path

from atm.ATM import ATM
l1 = [1,23,4]

for i in l1:
    print(i)


str = "催下"

print(str.__hash__())

d1 = {}


d1["cuixd"] = 1


print(len(d1))

filename = ATM.userDictPath

print(filename)
size = os.path.getsize(filename)

print(size)