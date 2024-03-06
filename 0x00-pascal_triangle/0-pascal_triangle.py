#!/usr/bin/python3
"""
 0. Pascal's Triangle
"""


def pascal_triangle(n):
    """prints pascal triangle using n """
    if n <= 0:
        return []

    roww = [[1]]

    for i in range(1, n):
        prev_row = roww[-1]
        new_row = [1]

        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)
        roww.append(new_row)

    return roww
