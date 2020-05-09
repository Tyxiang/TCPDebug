import os

file = open('2.bin','w')

for i in range(256):
    intData = i%10
    stringData = str(intData)
    file.write(stringData)
    print(stringData)

file.close()

os.system("pause ...")