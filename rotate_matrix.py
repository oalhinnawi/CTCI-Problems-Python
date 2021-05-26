# 1.7 Rotate Matrix: Given an image represented by an NxN matrix, 
# where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

# TODO: Implement swap on a square by square basis

def fourWaySwap(matrix, pos1, pos2, pos3, pos4):
    temp = matrix[pos2[0], pos2[1]]
    
    matrix[pos2[0], pos2[1]] = matrix[pos1[0], pos1[1]]



def rotateMatrix(matrix, n):
    temp = 0
    # 
    for j in range(0, n):
        for i in range(0, n):
            matrix[i][j]
            print(matrix[i][j])

    return matrix


if __name__ == "__main__":
    matrix = [[1,2],
              [3,4]]

    rotateMatrix(matrix, 2)