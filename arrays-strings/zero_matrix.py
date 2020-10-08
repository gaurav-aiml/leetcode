#@author : Gaurav Pai
#date-created : 10/8/20
import unittest
# def zero_matrix(mat):
#     rows = set()
#     cols = set()
#
#     for i in range(len(mat)):
#         for j in range(len(mat[0])):
#             if mat[i][j] == 0:
#                 rows.add(i)
#                 cols.add(j)
#
#     for row in rows:
#         mat[row] = [0]*len(mat[0])
#
#     for row in mat:
#         for col in cols:
#             row[col] = 0
#
#     return mat

def zero_matrix(mat):
    row_has_zero = False
    column_has_zero = False

    for j in range(len(mat[0])):
        if mat[0][j] == 0:
            row_has_zero = True
            break
    for i in range(len(mat)):
        if mat[i][0] == 0:
            column_has_zero = True
            break

    for i in range(1,len(mat)):
        for j in range(1,len(mat[0])):
            if mat[i][j] == 0:
                mat[0][j] = 0
                mat[i][0] = 0

    #check which column to be set to 0 in first row
    for j in range(1, len(mat[0])):
        if mat[0][j] == 0:
            for i in range(1,len(mat)):
                mat[i][j] = 0

    for i in range(1, len(mat)):
        if mat[i][0] == 0:
            mat[i] = [0]*len(mat[0])

    if row_has_zero:
        mat[0] = [0]*len(mat[0])

    if column_has_zero:
        for i in range(len(mat)):
            mat[i][0] = 0

    return mat



class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()