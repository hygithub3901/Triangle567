# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
@author: hyz
"""

import unittest

from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def testInvalidInputA(self):
        self.assertEqual(classify_triangle(300, 300, 300), 'InvalidInput', '(300, 300, 300) is InvalidInput')

    def testInvalidInputB(self):
        self.assertEqual(classify_triangle(-1, 0, 0), 'InvalidInput', '(-1, 0, 0) is InvalidInput')

    def testInvalidInputC(self):
        self.assertEqual(classify_triangle("a", "b", "c"), 'InvalidInput', '("a", "b", "c") is InvalidInput')

    def testNotATriangleA(self):
        self.assertEqual(classify_triangle(1, 1, 10), 'NotATriangle', '(1, 1, 10) is InvalidInput')

    def testRightTriangleA(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classify_triangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def testRightTriangleC(self):
        self.assertEqual(classify_triangle(5, 4, 3), 'Right', '5,4,3 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testIsocelesTrianglesA(self):
        self.assertEqual(classify_triangle(2, 2, 1), 'Isoceles', '2,2,1 should be Isoceles')

    def testIsocelesTrianglesB(self):
        self.assertEqual(classify_triangle(1, 2, 2), 'Isoceles', '1,2,2 should be Isoceles')

    def testIsocelesTrianglesC(self):
        self.assertEqual(classify_triangle(2, 1, 2), 'Isoceles', '1,2,2 should be Isoceles')

    def testScaleneTriangles(self):
        self.assertEqual(classify_triangle(2, 3, 4), 'Scalene', '2,3,4 should be Scalene')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
