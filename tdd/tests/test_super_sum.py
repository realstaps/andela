
from math.super_summation import super_summation as ss

import unittest

class SuperSumTest(unittest.TestCase):

	def test_two_numbers(self):
		result = ss(20,20)
		self.assertEqual(result,40)

	def test_four_numbers(self):
		result = ss(20,15,12,3)
		self.assertEqual(result,50)

	def test_two_lists(self):
		a = [10,20,30,40]
		b = [100,20]
		result = ss(a,b)
		self.assertEqual(result,200)

	def test_lists_and_number(self):
		a = [10,30,50]
		result = ss(a,50)
		self.assertEqual(result,140)

	def test_four_numbers(self):
		a,b,c,d = [1,2] , [2,3] , [3] , [4,10]
		result = ss(a,b,c,d)
		self.assertEqual(result,25)

	def test_large_input(self):
		pass

	
		
