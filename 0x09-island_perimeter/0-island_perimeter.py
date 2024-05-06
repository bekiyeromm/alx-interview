#!/usr/bin/python3
"""
module island_perimeter
"""


def island_perimeter(grid):
    """
     returns the perimeter of the island described in grid
    """
    if not grid:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    num_of_islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                """add 4 because each cell has 4 sides """
                num_of_islands += 4
                if r > 0 and grid[r - 1][c] == 1:
                    """
                    checks the above cell and if it is 1 -2 because
                    currunt cell shares a side with the cell to its top
                    """
                    num_of_islands -= 2
                if c > 0 and grid[r][c - 1] == 1:
                    """
                    checks the left cell and if it is 1 -2 because
                    currunt cell shares a side with the cell to its left
                    """
                    num_of_islands -= 2

    return (num_of_islands)
