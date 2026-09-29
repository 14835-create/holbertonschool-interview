#!/usr/bin/python3
"""Pascals triangle module"""


def pascal_triangle(n):
    """Returns list of lists rep Pascal's triangle"""
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev = triangle[-1]
        row = [1]
        for j in range(len(prev) - 1):
            row.append(prev[j] + prev[j + 1])
        row.append(1)
        triangle.append(row)

    return triangle
