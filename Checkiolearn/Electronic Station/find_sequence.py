def checkio(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if j + 4 <= len(matrix):
                if matrix[i][j] == matrix[i][j + 1] == matrix[i][j + 2] == matrix[i][j + 3]:
                    return True
            if i + 4 <= len(matrix):
                if matrix[i][j] == matrix[i + 1][j] == matrix[i + 2][j] == matrix[i + 3][j]:
                    return True
            if j + 4 <= len(matrix) and i + 4 <= len(matrix):
                if matrix[i][j] == matrix[i + 1][j + 1] == matrix[i + 2][j + 2] == matrix[i + 3][j + 3]:
                    return True
            if j >= 3 and i + 4 <= len(matrix):
                if matrix[i][j] == matrix[i + 1][j - 1] == matrix[i + 2][j - 2] == matrix[i + 3][j - 3]:
                    return True
    return False
'''
import numpy as np
    
    m = np.array(matrix)
    dim = m.shape
    
    #horizontal control
    for j in range(dim[0]):
        for i in range(dim[1]-3):    
            if np.all(m[j,i:i+4] == np.ones(4,dtype=np.int16)*m[j,i]): return True
    
    #vertical control
    for j in range(dim[1]):
        for i in range(dim[0]-3):
            if np.all(m[i:i+4,j] == np.ones(4,dtype=np.int16)*m[i,j]): return True
            
    #diagonal control
    for i in range(dim[1]-3):
        for j in range(dim[0]-3):
            right = left = np.array([],dtype=np.int16)
            for k in range(4):
                right = np.hstack((right,[m[j+k,i+k]]))
                left = np.hstack((left,[m[j+k,i+3-k]]))
            if np.all(right == np.ones(4,dtype=np.int16)*right[0]): return True
            if np.all(left == np.ones(4,dtype=np.int16)*left[0]): return True
            
    return False
'''

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
