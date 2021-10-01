from django.test import TestCase
from app.calc import *

class TestCalc(TestCase):
    def test_addition(self):
        self.assertEqual(add(1,1),2)
    
    def test_subtraction(self):
        self.assertEqual(Subtraction(1,1),0)
    
    def test_multiplication(self):
        self.assertEqual(Multiplication(1,1),1)
    
    def test_division(self):
        self.assertEqual(Division(1,1),1)
