# 1.2 Check Permutation, given two strings, 
# write a method to decide if one is a permutation of the other

# First thoughts, if one string is a permutation of another, 
# then their lengths should be multiples of each other

# If they are of equal length, they should be the exact same string, otherwise
# they cannot be permutations of each other.

# Otherwise, if one string is smaller than the other, the bigger string should be a multiple 
# of the other.



def checkPermutation(str_1, str_2):

    if(str_1 == 0 or str_2 == 0):
        return True

    # if length of both strings are the same, they need to be the exact same
    if(len(str_1) == len(str_2)):
        if(str_1 == str_2):
            return True
        else:
            return False

    # if one's smaller than the other:
    # Make sure the bigger ones a multiple of the other
    # and check each segment to make sure it matches the perm
    elif(len(str_1) < len(str_2)):

        if(not (len(str_2) % len(str_1) == 0)):
            return False

        else:
            segments = int(len(str_2) / len(str_1))
            for i in range(0, segments):
                if(str_1 == str_2[0 + i*len(str_1):(i+1)*len(str_1)]):
                    continue
                else:
                    return False
            return True 

    else:

        if(not (len(str_1) % len(str_2) == 0)):
            return False

        else:
            segments = int(len(str_1) / len(str_2))
            for i in range(0, segments):
                if(str_2 == str_1[0 + i*len(str_2):(i+1)*len(str_2)]):
                    continue
                else:
                    return False
            return True 


if __name__ == "__main__":
    test1 = "taco"
    
    print("Permutation test1 <> test1 * 3:", checkPermutation(test1, test1+test1+test1))
    print("Permutation +1:", checkPermutation(test1+"b", test1+"a"))
