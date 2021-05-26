# 1.7 Rotate Matrix: Given an image represented by an NxN matrix, 
# where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

import sys
import math

# This is inefficient, I could easily do this in the main loop
# For the sake of visualizing what's going on I'm going to keep it
def fourWaySwap(matrix, pos1, pos2, pos3, pos4):
    temp1 = matrix[pos1[0]][pos1[1]]
    temp2 = matrix[pos2[0]][pos2[1]]
    temp3 = matrix[pos3[0]][pos3[1]]
    temp4 = matrix[pos4[0]][pos4[1]]
    matrix[pos1[0]][pos1[1]] = temp4
    matrix[pos2[0]][pos2[1]] = temp1
    matrix[pos3[0]][pos3[1]] = temp2
    matrix[pos4[0]][pos4[1]] = temp3
    return matrix

def rotateMatrix(matrix, n):
    # n represents the number of elements, so it should be n-1 for traversal
    
    numSquares = math.ceil(n/2)
    # If the number of elements per row is odd, we'll need a different modifier
    
    jModifier = 2 if n % 2 == 0 else 1

    print("NUMSQUARES",numSquares)
    n -= 1
    
    temp = 0
    
    for j in range(0, numSquares):
        for i in range(0, n - (j * jModifier)):
            matrix = fourWaySwap(matrix, (j, i + j), (i + j, n-j), (n-j, n-i-j), (n-i-j, j))

    return matrix


if __name__ == "__main__":
    matrix = [[1,2,3],
              [4,5,6],
              [7,8,9]]
    # matrix = [[1,2,3,4],
    #           [5,6,7,8],
    #           [9,10,11,12],
    #           [13,14,15,16]]
    matrix = rotateMatrix(matrix, 3)
    print(matrix)