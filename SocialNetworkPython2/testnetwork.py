'''
Created on May 28, 2013
module exports the TestNetwork class
***this is the old version
@author: Vanessa
'''

from networkmodule import Network
from personmodule import Person


class TestNetwork ():
    """test class that will contain methods which test that all of the methods in the Network class work as they should""" 

    def test_add_friend(self, friendToAdd):
        """
        Tests that the add_friend() function adds the specified person to the set
        Takes a Person, friendToAdd and returns True if the specified friend was added to the set or False if it wasn't
        """
        Network.add_friend(self, friendToAdd)
        #check that the friend was added to the set
        if (Network.setOfFriends.__contains__(friendToAdd)):
            return True
        else:
            return False
    
    
    def test_get_friends(self):
        """
        tests that get_friends() returns the set of names of the friends
        returns true if the get_friends() method returns the correct set of names of the friends which are in the set
        """
        Network.get_friends(self)
        #check that it returns the correct names of friends that are within the set
        return Network.get_friends(self)
        if(Network.get_friends(self)._contains_("Vanessa") and Network.get_friends(self)._contains_("Andrea")):
            return True
        else:
            return False
        
    
    
    def test_get_friends_same_age(self,user):
        """
        tests that get_friends_same_age() returns a set of the names of the friends of the same age
        returns true if the get_friends_same_age() method returns the correct set of names of the friends of the same age which are in the set
        """
        Network.get_friends_same_age(self,user)
        if(Network.get_friends_same_age(self,user).__contains__("Vanessa")):
           return True
        else:
            return False
    
    def test_friend_to_remove(self):
        """
        tests that the friend_to_remove() functions returns the friend with the given name and age that the user wants to remove
        returns true if the friend_to_remove function works as it should
        """
        friendToRemove = Network.friend_to_remove(self, "Vanessa", 18)
        #checks that the Person returned by the friend_to_remove() function contains that name and age
        if(friendToRemove.get_name() == "Vanessa" and friendToRemove.get_age() == 18 ):
            return True
        else:
            return False
    
    def test_remove_friend(self, friendToRemove):
        """
        Tests that the remove_friend() function removes the specified person to the set
        Takes a Person, friendToRemove and returns True if the specified friend was removed from the set or False if it wasn't
        """
        Network.remove_friend(self, friendToRemove)
        #check that the friend was removed from the set
        if (Network.setOfFriends.__contains__(friendToRemove)):
            return False
        else:
            return True
    
        
        return
    
    def test_remove_all_friends(self):
        """
        tests that remove_all_friends() removes all of the friends from the set
        returns True if all of the friends were removed from the set and false if they weren't
        """
        Network.remove_all_friends(self)
        #if the set is empty
        if(not Network.setOfFriends):
            return True
        else:
            return False
    
def main():  
    """
    calls the test functions and will print whether or not the functions in the Network class work 
    depending if the test functions return True or False    
    """
    #create a network object
    socialN = Network()
    
    #creates a user person object
    userM = Person()
    userM.set_name("Marilyn")
    userM.set_age(18)
    
    #creates a friend Person object and sets their name and age
    friendV = Person()
    friendV.set_name("Vanessa")
    friendV.set_age(18)
    
    #call test_add_friend() passing the friend as parameters
    #if the method returns True then the add_friend() function works 
    if (TestNetwork.test_add_friend(socialN,friendV) == True):
        print ("add_friend() function works")
    else:
        print ("add_friend() function doesn't work")
    
    #creates another friend object and adds her to the set
    friendA = Person()
    friendA.set_name("Andrea")
    friendA.set_age(15)
    Network.add_friend(socialN, friendA)
    
    #call the test_get_friend() passing socialN as parameters
    #if the method returns True then the get_friend() function works
    if(TestNetwork.test_get_friends(socialN)==True):
        print("get_friends() function works")
    else:
        print("get_friends() function doesn't work")
    
    
    #call the test_get_friends_same_age() passing socialN as parameters
    #if the method returns True then the get_friend_same_age() function works
    if(TestNetwork.test_get_friends_same_age(socialN, userM)==True):
        print("get_friends_same_age() function works")
    else:
        print("get_friends_same_age() function doesn't work")
    
    
    #call the test_friend_to_remove() function
    #if the function returns True then the friend_to_remove() function works
    if(TestNetwork.test_friend_to_remove(socialN) == True):
        print("friend_to_remove() function works")
    else:
        print("friend_to_remove() function doesn't work")
    
    
    #call test_remove_friend() passing the friend as parameters
    #if the method returns True then the remove_friend() function works 
    if (TestNetwork.test_remove_friend(socialN, friendV) == True):
        print ("remove_friend() function works")
    else:
        print ("remove_friend() function doesn't work")
        
    #call test_remove_all_friends() 
    #if the method returns True then the remove_all_friends() function works 
    if (TestNetwork.test_remove_all_friends(socialN) == True):
        print ("remove_all_friends() function works")
    else:
        print ("remove_all_friends() function doesn't work")    
    
    

#calls main method
if __name__ == "__main__":
    main()      