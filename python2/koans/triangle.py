#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    # DELETE 'PASS' AND WRITE THIS CODE
    edge = [a, b, c]
    a, b, c = sorted(edge)
    if a + b <= c:
        raise TriangleError(None)
    elif a <= 0 or b <= 0 or c <= 0:
        raise TriangleError(None)
    else:
        edgeset = set(edge);
        if a == b and b == c:
            return 'equilateral'
        elif a == b or b == c:
            return 'isosceles'
        else:
            return 'scalene'
    #pass


# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    def __init__(self,error):
        self.error = error
        StandardError.__init__(self,'False')

    #pass


