myMessage = ["" for i in range(10)]


def breakString(string):
    brokenString = [string[i:i+2] for i in range(0, len(string), 2)]
    return brokenString


def combineToPayload():
    payload = ""
    for i in range(len(myMessage)):
        if myMessage[i] != "" and not myMessage[i].isspace():
            payload += myMessage[i]
    return payload


f = open("mayday.txt","r")
while True:
    fileData = f.readline().strip()
    if fileData == "":
        break
    if fileData[0:4] == "5555":
        order = int(fileData[12:14], 16)
        checksum = int(fileData[14:16], 16)
        message = fileData[16:]
        splitHex = breakString(message)
        splitMessage = []
        for i in range(len(splitHex)):
            splitMessage.append(int(splitHex[i], 16))
        if sum(splitMessage) % 256 == checksum:
            myMessage[order] = fileData[16:]


final = combineToPayload()
print(bytes.fromhex(final).decode("ASCII"))
