# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

class TestTriangles(unittest.TestCase):
    # Existing test cases
    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    # Enhanced test cases
    # Test Invalid Inputs
    def testInvalidInputNegative(self):
        self.assertEqual(classifyTriangle(-1,2,3), 'InvalidInput', '-1,2,3 cannot form a triangle')

    def testInvalidInputZero(self):
        self.assertEqual(classifyTriangle(0,0,0), 'InvalidInput', '0,0,0 cannot form a triangle')

    def testInvalidInputTooLarge(self):
        self.assertEqual(classifyTriangle(201,201,201), 'InvalidInput', '201,201,201 is too large for valid input')

    # Test Not a Triangle
    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(1,2,3), 'NotATriangle', '1,2,3 does not form a triangle')

    # Test Isoceles Triangles
    def testIsocelesTriangle(self):
        self.assertEqual(classifyTriangle(2,2,3), 'Isoceles', '2,2,3 should be isoceles')

    # Test Scalene Triangles
    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(4,5,6), 'Scalene', '4,5,6 should be scalene')

    # Additional Right Triangle Tests
    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(8,15,17), 'Right', '8,15,17 is a Right triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
