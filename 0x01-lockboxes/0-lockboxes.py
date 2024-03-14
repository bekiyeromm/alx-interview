#!/usr/bin/python3
"""
a method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """Initialize a set to keep track of visited boxes
        boxes: is a list of lists
        """
    visited = set()
    """Define a function to perform depth-first search"""

    def dfs(box):
        """Mark the current box as visited"""
        visited.add(box)

        """Traverse through the keys in the current box"""
        for key in boxes[box]:
            """If key correspond to box hasn't ben visited,recursiv call dfs"""
            if key not in visited and key < len(boxes):
                dfs(key)

    """Start DFS from the first box (boxes[0])"""
    dfs(0)
    """Check if all boxes have been visited"""
    return len(visited) == len(boxes)
