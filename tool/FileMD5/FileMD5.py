import hashlib
import base64
import os

file = open('2.bin', 'rb')
data = file.read()

m = hashlib.md5()
m.update(data)

md5_32 = m.hexdigest()
print("MD5 32:" + md5_32)

md5_16 = md5_32[8:-8]
print("MD5 16:" + md5_16)

content_md5 = base64.b64encode(md5_16.encode(encoding="utf-8"))
print("Content-MD5: " + content_md5.decode())

os.system("pause ...")
