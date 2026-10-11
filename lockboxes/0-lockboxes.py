#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = {0}
    stack = [0]

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if 0 <= key < n and key not in unlocked:
                unlocked.add(key)
                stack.append(key)

    return len(unlocked) == n
