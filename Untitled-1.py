def convert(s):
        # initialization of string to ""
        new = ""
        # traverse in the string
        for x in s:
            new += x
        # return string
        return new

def CaesarEncryption(realText, step):
    outText = []
    cryptText = []
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for eachLetter in realText:
        if eachLetter in number:
            index = number.index(eachLetter)
            crypting = (index + step) % 10
            cryptText.append(crypting)
            newLetter = number[crypting]
            outText.append(newLetter)  
    return convert(outText)

def MirrorEncryption(string):
    translated = '' #cipher text is stored in this variable
    i = len(string) - 1

    while i >= 0:
        translated = translated + string[i]
        i = i - 1
    return translated

def HybirdEncryption(string, step = 3):
    Encrypted1 = CaesarEncryption(string, step)
    Encrypted2 = MirrorEncryption(Encrypted1)
    return (Encrypted2)

decryption = input("Enter OTP code: ")
encryption = HybirdEncryption(decryption)
print(encryption)   