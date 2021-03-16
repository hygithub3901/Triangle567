# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Mar 16, 2021

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
@author: hyz
"""


def classify_triangle(line_a, line_b, line_c):
    '''
    classify if three numbers can be a triangle
    '''
    result: str = ''
    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(line_a, int) and isinstance(line_b, int) and isinstance(line_c, int)):
        return 'InvalidInput'
    # require that the input values be >= 0 and <= 200
    if (line_a > 200 or line_b > 200 or line_c > 200):
        return 'InvalidInput'
    if (line_a <= 0 or line_b <= 0 or line_c <= 0):
        return 'InvalidInput'
    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (line_a >= (line_b + line_c)) or (line_b >= (line_a + line_c)) or (line_c >=
    (line_a + line_b)):
        return 'NotATriangle'
    # now we know that we have a valid triangle
    if line_a == line_b and line_b == line_c:
        result = 'Equilateral'
    elif ((line_a ** 2) + (line_b ** 2)) == (line_c ** 2) or ((line_a ** 2) + (line_c
    ** 2)) == (line_b ** 2) or ((line_b ** 2) + (line_c ** 2)) == (line_a ** 2):
        result = 'Right'
    elif (line_a != line_b) and (line_b != line_c) and (line_a != line_c):
        result = 'Scalene'
    else:
        result = 'Isoceles'
    return result
