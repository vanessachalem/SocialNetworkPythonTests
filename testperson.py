'''
Created on May 28, 2013
module exports the TestPerson class
@author: Vanessa
'''

from personmodule import Person
import unittest

class TestPerson(unittest.TestCase):
    """
    test class that will contain functions which test each of the functions in the Person class to make 
    sure they work as they should
    """ 
    
    def setUp(self):
        personV = Person()
    
    def test_set_get_age(self):
        """
        tests the set_age() and get_age() functions
        accepts age1 and sets the user's age
        returns True if the function returns the user's correct age
        """
        personV = Person()
        personV.set_age(18)
        self.assertEqual(personV.get_age(), 18)
        
    def test_set_get_name(self):
        """
        tests the set_name() and get_name() functions
        accepts name1 and sets the user's name
        returns True if the function returns the user's correct name
        """
        personV = Person()
        personV.set_name("Vanessa")
        self.assertEqual(personV.get_name(), "Vanessa")

if __name__ == "__main__":
    unittest.main()           