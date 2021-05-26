# 1.8 Write an algorithm such that if an element in an MxN matrix is 0, 
# its entire row and column are set to 0.

# First Thoughts: Brute Force algorithm, seems pretty straightforward(?)
# Not immediately obvious how to optimize
def zeroMatrix(matrix, m, n):

    markedRows = []
    markedColumns = []
    for i in range(0, m):
        for j in range(0, n):
            if(matrix[i][j] == 0):
                markedRows.append(i)
                markedColumns.append(j)
    
    for row in markedRows:
        matrix[row] = [0 for x in range(0, n)]

    for column in markedColumns:
        for i in range(0, m):
            matrix[i][column] = 0

    return matrix


if __name__ == "__main__":
    matrix = [[1,2,3],
              [3,0,5],
              [4,10,34]]

    print(zeroMatrix(matrix, 3, 3))