'''
Created on June 4, 2013
module exports the TestNetworkFixed class
***this is the fixed version of the unittest for the Network class
@author: Vanessa
'''

from networkmodule import Network
from personmodule import Person
import unittest

class TestNetworkFixed (unittest.TestCase):
    """test class that will contain methods which test that all of the methods in the Network class work as they should""" 
    
    def setUp(self):
        socialN = Network()
    
    def test_add_friend(self):
        """
        Tests that the add_friend() function adds the specified person to the set
        Takes a Person, friendToAdd and returns True if the specified friend was added to the set or False if it wasn't
        """
        #creates a friend Person object and sets their name and age
        friendV = Person()
        friendV.set_name("Vanessa")
        friendV.set_age(18)

        Network.add_friend(self, friendV)
        #check that the friend was added to the set
        self.assertTrue(friendV in Network.setOfFriends)
    
    
    def test_get_friends(self):
        """
        tests that get_friends() returns the set of names of the friends
        returns true if the get_friends() method returns the correct set of names of the friends which are in the set
        """
        Network.get_friends(self)
        #check that it returns the correct names of friends that are within the set
        self.assertTrue("Vanessa" in Network.get_friends(self))
        
    
    def test_get_friends_same_age(self):
        """
        tests that get_friends_same_age() returns a set of the names of the friends of the same age
        returns true if the get_friends_same_age() method returns the correct set of names of the friends of the same age which are in the set
        """
         #creates a user person object
        userM = Person()
        userM.set_name("Marilyn")
        userM.set_age(18)
    
        Network.get_friends_same_age(self,userM)
        self.assertTrue("Vanessa" in Network.get_friends_same_age)
        
    def test_friend_to_remove(self):
        """
        tests that the friend_to_remove() functions returns the friend with the given name and age that the user wants to remove
        returns true if the friend_to_remove function works as it should
        """
        friendToRemove = Network.friend_to_remove(self, "Vanessa", 18)
        #checks that the Person returned by the friend_to_remove() function contains that name and age
        self.assertEqual(friendToRemove.get_name(), "Vanessa")
        
    def test_remove_friend(self):
        """
        Tests that the remove_friend() function removes the specified person to the set
        Takes a Person, friendToRemove and returns True if the specified friend was removed from the set or False if it wasn't
        """
        friendToRemove = Network.friend_to_remove(self, "Vanessa", 18)
        
        Network.remove_friend(self, friendToRemove)
        #check that the friend was removed from the set
        self.assertTrue(friendToRemove is not Network.setOfFriends)
        
    def test_remove_all_friends(self):
        """
        tests that remove_all_friends() removes all of the friends from the set
        returns True if all of the friends were removed from the set and false if they weren't
        """
        Network.remove_all_friends(self)
        #if the set is empty
        self.assertTrue(not Network.setOfFriends)
        
#calls unittest
if __name__ == "__main__":
    unittest()      