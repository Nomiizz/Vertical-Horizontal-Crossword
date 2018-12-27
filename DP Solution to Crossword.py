# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 02:30:37 2018

@author: Nauman Ahmed
"""
import numpy as np

# Take as input first line followed by blank line
def getWordInput():
    matchStr = []
    while True:
        line = raw_input()
        if line:
            matchStr.append(line)
        else:
            break
    text1 = '\n'.join(matchStr)
    return list(text1)

matchStr = getWordInput()

# Take as input matrix of characters
def getMatrixInput():
    matrix = []
    line = raw_input()
    matrix.append(line)

    iters = len(line)
    for i in range(1, iters):
        line = raw_input()
        if line:
            matrix.append(line)

    return matrix

matrix = getMatrixInput()

def fillUpDPArray():
    matrix_dim = len(matrix[0])

    DArray = np.zeros((matrix_dim + 1, matrix_dim + 1, len(matchStr) + 1), dtype=np.bool)

    rows = cols = matrix_dim + 1

    # Fill front face of 3d-DArray with true values
    for i in range(rows):
        for j in range(cols):
            DArray[i][j][0] = True
            

    for i in range(1, rows):
        for j in range(1, cols):
            for k in range(1, len(matchStr) + 1):
                if i==1 and j==1 and k==1:
                    DArray[i][j][k] = (matrix[i - 1][j - 1]==matchStr[k - 1])
                else:
                    DArray[i][j][k] = (DArray[i - 1][j][k - 1] or DArray[i][j - 1][k - 1]) and (matrix[i - 1][j - 1] == matchStr[k - 1])

    return DArray
                
DArray = fillUpDPArray()

# Do backtracking to get start and finish coordinates
def isFound(matchStr, DArr):
    found = 0
    idx = 0
    start = []
    end = []
    
    result = np.where(DArr == True) # result is a tuple of i list & j list & k list where val is True
            
    for i in range(len(result[2])):
        if result[2][i] == len(matchStr):
            found = 1
            idx = i
            
    if found == 0:
        return 0
    else:
        end.append(result[0][idx])
        end.append(result[1][idx])
        
        
        i = result[0][idx]
        j = result[1][idx]
        for k in range(len(matchStr), 1, -1):
            if (DArr[i - 1][j][k - 1] == True):
                i -= 1
            else:
                j -= 1
        
        start.append(i)
        start.append(j)
        
        newList = start + end
        
        str1 = ' '.join(str(e) for e in newList)
        return str1
            

ret = isFound(matchStr, DArray)
print str(ret)