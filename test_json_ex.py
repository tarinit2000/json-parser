import unittest 
# python unit test library (standard so no need for pip install)
from json_ex import check_char_count 
# import the function I wrote 
from json_ex import check_char_type
from json_ex import check_char_match

#checks if the functions behave as I want them to 
class TestJsonEx(unittest.TestCase): 
# creating a class in json
# subclassing: TestCase class has unittest stuff
    def test_check_char_count(self):
        self.assertEqual(check_char_count('AA'), 'AA count passes')
        self.assertEqual(check_char_count('AAA'), 'AAA count FAILS')
        #self.assertRaises(TypeError, check_char_count, 1)
        #self.assertRaises(TypeError, check_char_count, True)
        #self.assertRaises(TypeError, check_char_count, ['AA', 'BB'])
        self.assertRaises(AssertionError, check_char_count, 1)
        self.assertRaises(AssertionError, check_char_count, True)
        self.assertRaises(AssertionError, check_char_count, ['AA', 'BB'])

    def test_check_char_type(self):
         self.assertEqual(check_char_type('AA'), 'AA type passes')
         self.assertEqual(check_char_type('Aa'), 'Aa type FAILS')
         self.assertEqual(check_char_type('aa'), 'aa type FAILS')
         self.assertEqual(check_char_type('A1'), 'A1 type FAILS')
         self.assertEqual(check_char_type('a1'), 'a1 type FAILS')
         self.assertRaises(AttributeError, check_char_type, 1)
         self.assertRaises(AttributeError, check_char_type, True)
         self.assertRaises(AttributeError, check_char_type, ['AA', 'BB'])

         # attribute error comes if you try using a string function on a float 
    def test_check_char_match(self):
        self.assertRaises(TypeError, check_char_match, 1, 1)
        self.assertRaises(IndexError, check_char_match, 'AA', '')
        self.assertEquals(check_char_match('AZ', 'Arizona'), 'AZ Arizona passes')
        self.assertEquals(check_char_match('AZ', 'Brizona'), 'AZ Arizona FAILS')
        self.assertEquals(check_char_match('AZ', 'Arizona'), 'AZ Arizona passes')    
        self.assertRaises(TypeError, check_char_match, ['AA', 'BB'], ['AA', 'BB'])
        
if __name__ == '__main__':
    unittest.main()
