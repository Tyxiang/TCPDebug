import json
import socket
import os

stringFolderSend = "send"

def getFileData(stringFilePath):
    bytesData = b''
    if os.path.exists(stringFilePath):
        path, ext = os.path.splitext(stringFilePath)
        if ext == ".txt" or ext == ".bin":
            fileFile = open(stringFilePath, 'rb')
            bytesData = fileFile.read()
            fileFile.close()
    return bytesData

fileSetting = open('setting.json')
dictSetting = json.load(fileSetting)

bytesToSend = b''
for root, dirs, files in os.walk(stringFolderSend):
    for stringFileSend in files:
        bytesToSend = bytesToSend + getFileData(os.path.join(root, stringFileSend))

socketSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print()
print('Connect ...', end=" ") 
socketSocket.connect((dictSetting['ip/domain'], dictSetting['port']))
print('OK')
print()

print('[Send]')
print()

socketSocket.send(bytesToSend)

listSent = bytesToSend.split(b'\r\n')
for bytesLine in listSent:
    print("<{:^6}>".format(len(bytesLine)), end =' ')
    print(bytesLine)
print()

print('[Rece]')
print()
bytesReceived = socketSocket.recv(dictSetting['buffer'])
socketSocket.close()

listReceived = bytesReceived.split(b'\r\n')
for bytesLine in listReceived:
    print("<{:^6}>".format(len(bytesLine)), end =' ')
    print(bytesLine)
print()

fileReceived = open('received.dat', 'wb')
fileReceived.write(bytesReceived)
fileReceived.close()

os.system("pause ...")