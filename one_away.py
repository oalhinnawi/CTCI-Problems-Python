#1.5 One Away: There are three types of edits that can be performed on strings: insert a character,
#remove a character, or replace a character. Given two strings, write a function to check if they are
#one edit (or zero edits) away.

# First Thoughts: if zero edits, they should be the same string(?)

def checkInsertReplaceEdit(str_1, str_2):
    index_1 = 0
    index_2 = 0
    # Implement rest of this 


def checkOneAway(str_1, str_2):

    if(len(str_1) == len(str_2)):
        # Check if zero edits have been made
        if(str_1 == str_2):
            return True
        # Knowing they're the same length, check for more than one change
        else:
            edits = 0
            for i in range(0, len(str_1)):
                if not (str_1[i] == str_2[i]):
                    edits += 1
                    if(edits > 1):
                        return False
            return True

    #Now check is the length difference between the two exceeds one
    if(abs(len(str_1) - len(str_2)) > 1):
        
        return False

    # Now check insert/replace edits

