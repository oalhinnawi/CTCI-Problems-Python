# 1.6 String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).

def compressString(string):

    currentCharacter = string[0]
    characterCount = 0
    compressedString = ""
    for character in string:
        if(currentCharacter == character):
            characterCount += 1 
        else:
            compressedString += (currentCharacter + str(characterCount))
            currentCharacter = character
            characterCount = 1
    
    compressedString += (currentCharacter + str(characterCount))

    if(len(compressedString) < len(string)):
        return compressedString
    else:
        return string


if __name__ == "__main__":
    print(compressString("tttEEExxxTTT"))
    print(compressString("tttexttt"))


    