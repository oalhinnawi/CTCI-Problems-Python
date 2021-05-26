
#1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

# First Thought: Obviously we need to iterate through each character, 
# this is easily done with hash tables/dicts in python


# Algo: 
# Build the dict/hash table
# As you iterate through the string, if the string doesn't exist in the table, 
# initialize a key with that character and set it to one, otherwise, if it does, reutrn False



# Clean Solution
def isUnique(string):
    table = {}

    for character in string:
        if character in table:
            return False
        else:
            table[character] = 1

    return True

# Brute Force Method
def bruteForce(string):
    
    # Any string of length 1 or 0 is by default 
    if len(string) is 1 or len(string) is 0:
        return True

    # Brute Force
    for i in range(0, len(string) - 1):
        for j in range(i + 1, len(string) - 2):
            if string[i] == string[j]:
                return False
    
    return True


if __name__ == "__main__":
    
    string = "teehee"
    unique = "Ryan"

    print("Non-Unique teehee: ", isUnique(string))
    print("Unique:", isUnique(unique))
