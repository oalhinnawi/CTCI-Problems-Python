# 1.3 URLify: Write a method to replace all spaces in a string with '%20' 
# You may assume that the string has sufficient space at the end to hold the additional
# characters, and that you are given the "true" length of the string 


# First thoughts: In python this is easily done with string_class.replace(" ", "%20")
# Ok so lets say the em
# After trying: Nevermind, it needs some work
def dirtyReplace(string, length):
    text = ""
    for i in range(0, length-1):
        if(string[i] == " "):
            text += "%20"
        else:
            text += string[i]
    return text



if __name__ == "__main__":
    print(dirtyReplace("My longest yea boi ever   ", 23))
