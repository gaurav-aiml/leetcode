import math
def matrix_rotate(arr):
    n = len(arr) - 1
    m = len(arr[0]) - 1

    rows = len(arr)
    cols = len(arr[0])

    for i in range(rows//2):
        for j in range(i,cols-i-1):
            arr[j][m-i],arr[m-i][n-j],arr[n-j][i],arr[i][j] = arr[i][j],arr[j][m-i],arr[m-i][n-j],arr[n-j][i]
    return arr

print(matrix_rotate([[0,1,2,3],[11,12,13,14],[15,16,17,18],[20,25,30,35]]))