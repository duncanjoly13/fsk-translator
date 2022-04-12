def getIndex(character):
    characters = ".0123456789abcdefghijklmnopqrstuvwxyz"
    return characters.index(character)

def getBinary(index):
    return format(index, 'b')

def binaryToDecimal(binary):
    decimal = int(binary, 2)
    return decimal

def getRegular(index):
    characters = ".0123456789abcdefghijklmnopqrstuvwxyz"
    return(characters[index])

def translateToBinary(message):
    output = ""
    for character in message.lower():
        output+= (getBinary(getIndex(character))+" ")
    return output

def translateToText(message):
    split = message.split(" ")
    split.pop((len(split))-1)
    text = ""
    for item in split:
        text+=getRegular(binaryToDecimal(item))
    print(text)

original = "Joe1"
output = translateToBinary(original)
print(output)
translateToText(output)
