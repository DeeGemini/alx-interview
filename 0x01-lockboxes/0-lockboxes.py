#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
    - boxes: A list of lists representing the boxes and their keys.

    Returns:
    - True if all boxes can be opened, else False.
    """
    if not boxes or len(boxes) == 0:
        return False

    n = len(boxes)
    keys = [0] # Start with the key to the first box
    visited = set()

    while keys:
        key = keys.pop()
        visited.add(key)
        box = boxes[key]
        for new_key in box:
            if 0 <= new_key < n and new_key not in visited:
                keys.append(new_key)

    return len(visited) == n

if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))

