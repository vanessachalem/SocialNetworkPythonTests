'''
Created on May 26, 2013
module exports Person class
@author: Vanessa
'''


class Person:
    """creates a Person object with a name and age""" 
   
    #initializes the variables 
    age = 0
    name = " "
    
    def initialize(self):    
        """constructor - initializes Person object""" 
        pass
     
    def set_age (self, PersonAge):
        """takes an integer PersonAge and sets the person's age""" 
        self.age =  PersonAge 
    
    def get_age(self):
        """returns the person's age"""
        return self.age
        
    def set_name(self, PersonName):
        """takes a string PersonName and sets the person's name"""
        self.name = PersonName
            
    def get_name(self):
        """returns the person's name""" 
        return self.name


