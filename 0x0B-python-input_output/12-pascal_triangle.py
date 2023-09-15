#!/usr/bin/python3
"""Define Pascal Triangle function"""


def pascal_triangle(n):
    """Function that returns a list of lists of integers"""
    t_row = [1]
    temp_l = [0]
    pTri = []

    if n <= 0:
        return (pTri)

    for i in range(n):
        pTri.append(t_row)
        t_row = [l+r for l, r in zip(t_row + temp_l, temp_l + t_row)]
    return (pTri)
