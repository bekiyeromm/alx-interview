#!/usr/bin/env python3
"""
a module to rotate n x n 2D matrix by 90 clockwise direction
"""


def rotate_2d_matrix(matrix):
    """
    rotate n x n 2D matrix 90 degrees clockwise
    Args:
        matrix (list): 2d square matrix
    Return:
        None
    """
    n = len(matrix)
    """
    first transpose matrix
    """
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    """
    then reverse ech row
    """
    for row in matrix:
        row.reverse()
