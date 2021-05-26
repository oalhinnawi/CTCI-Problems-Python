# 1.9 String Rotation:Assumeyou have a method isSubstringwhich checks if one word is a substring
# of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
# call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").


def rotationCheck(original, rotated):
    for _ in range(0, len(original)):
        if(original == rotated):
            return True  
        original = original[1:] + original[0]
    return False


if __name__ == "__main__":

    original = "badabing"
    rotated = "bababoom"

    print("RotationCheck:", rotationCheck(original, rotated))