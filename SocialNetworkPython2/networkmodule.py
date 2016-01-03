'''
Created on May 24, 2013
module exports Network class 
@author: Vanessa
'''

from personmodule import Person


class Network:
    """
    creates a Network object where people can add friends, remove friends, remove all friends,
    get a list of their friends and get a list of their friends which are the same age 
    """
    
    #creates a set where person objects (friends) will be stored
    setOfFriends = set()

    def intitialize(self):
        """constructor - initializes a network object"""
        pass
    
    def user_choice(self):
        """asks for the user's choice and returns the user's input"""
        print()
        print ("Would you like to add friends, remove friends, remove all friends, get friends, get friends of same age or sign out?")        
        userInput = input("Please choose by typing your preference exactly as it is written above: ")
        return userInput 

    def user_info(self):
        """prompts the user for his information and returns a user Person"""
        userName = input("What is your name: ")
        userAge = input ("What is your age: ") 
        #create user Person
        user = Person()
        #set that Person's name and age 
        user.set_name(userName)
        user.set_age(userAge)
        return user
    
    def friend_info(self):
        """interacts with the user asking for his friend's information and returns a friend Person"""
        friendName = input("Please enter your friend's name: ")
        friendAge = input ("Please enter their age: ") 
        #create friend Person
        friend = Person()
        #set that Perosn's name and age 
        friend.set_name(friendName)
        friend.set_age(friendAge)
        return friend
        
    def add_friend(self,friend):
        """takes a Person friend and adds it to the set of the user's friends"""
        self.setOfFriends.add(friend)
    
    def friend_to_remove(self, friendName, friendAge):
        """takes friendName and friendAge as parameters, then 
        iterates through the set of friends and returns f, the friend with the given name and age"""
        for f in self.setOfFriends:
            if(f.get_name() == friendName and f.get_age()== friendAge):
                return f
               
    def remove_friend(self,friendToRemove):
        """takes a Person friendToRemove and removes it from the set of the user's friends"""
        #remove friend from set
        self.setOfFriends.remove(friendToRemove)
        
    def remove_all_friends(self):
        """ removes all of the user's friends""" 
        self.setOfFriends.clear()
        
    def get_friends(self):
        """returns set of the names of all of the user's friends"""
        friendsNames = set()
        for friend in self.setOfFriends:
            name = friend.get_name()
            friendsNames.add(name)
        return friendsNames
    
    def get_friends_same_age(self,user):
        """returns list of user's friends of the same age"""
        friendsSameAge = set()
        for friend in self.setOfFriends:
            if friend.get_age() == user.get_age():
                name=friend.get_name()
                friendsSameAge.add(name)
        return friendsSameAge
    
    def changeString(self, word):
        """
        Takes a word and returns the word without white space before/after the word and in lower case 
        and without an 's' at the end of the word since this is a letter that can accidentally be typed or missed in the end of several of these words
        - this is done in order to remove space and caps sensitivity on user input in the main method
        """
        return word.lower().strip().rstrip('s')
        
def main():
    """main method - interacts with the user and calls the other methods"""
    #creates a network object   
    socialNetwork = Network()
 
    print("Welcome to the Social Network, would you like to login?")
    
    #reads user input - stores user input under variable userInput
    #uses if/else statements to determine if user would like to log in
    login = input("Please type 'yes' or 'no' ")
    if(login.lower().strip() == "yes"):
        
        #prompts user for his info - will save the Person object that is return by the method under the variable user
        user = socialNetwork.user_info()
        #asks user what he would like to do      
        userOption = socialNetwork.user_choice()
        #as long as user doesn't want to sign out will execute if/else statements and call userChoice() again
        #in the following while and if/else statements string.lower() removes caps sensitivity and string.strip() removes space sensitivity
        while (socialNetwork.changeString(userOption)!="sign out"):
            #uses if/else statements to determine which method to call 
            if(socialNetwork.changeString(userOption) == "add friend" or socialNetwork.changeString(userOption) == "addfriend"):
                #stores the person returned by the friend_info() function  under the variable friend
                friend = socialNetwork.friend_info()
                #calls the add_friend() function passing the friend as parameters
                socialNetwork.add_friend(friend)
        
            elif(socialNetwork.changeString(userOption) == "remove friend" or socialNetwork.changeString(userOption) == "removefriend"):
                #prompts the user for his friend's information
                friendName = input("Please enter your friend's name: ")
                friendAge = input ("Please enter their age: ") 
                #stores the person returned by the friend_to_remove() function under the variable friendToRemove         
                friendToRemove = socialNetwork.friend_to_remove(friendName,friendAge)
                #if friendToRemove doesn't exit
                if(not friendToRemove):
                    print("This friend doesn't exist in your set of friends")
                else:
                #calls the remove_friend() function passing the friendToRemove as parameters
                    socialNetwork.remove_friend(friendToRemove)
                    print (friendToRemove.get_name() + " was removed")

            elif(socialNetwork.changeString(userOption) == "remove all friend" or socialNetwork.changeString(userOption) =="removeallfriend"):
                socialNetwork.remove_all_friends()
                print("All of your friends have been removed. You currently have no friends.")
                            
            elif(socialNetwork.changeString(userOption) == "get friend" or socialNetwork.changeString(userOption) =="getfriend"):
                #if the set of friends is empty
                if (not socialNetwork.get_friends()):
                    print ("You have no friends")
                else:
                    #print the set of names converted to a string    
                    print ("These are your friends: " + socialNetwork.get_friends().__str__())
    
            elif(socialNetwork.changeString(userOption) == "get friends of same age" or socialNetwork.changeString(userOption) =="getfriendsofsameage"):
                #store the set returned by get_friends_of_same_age under sameAge
                sameAge = socialNetwork.get_friends_same_age(user)
                
                #if the set of friends of same age is empty
                if (not sameAge):
                    print ("You have no friends that are your same age")
                else:
                    #print the set of names converted to a string    
                    print ("These are your friends of your same age: " + sameAge.__str__())

            
            #if the user enters a string that is not one of the above options
            else:
                print()
                print("What you entered is not an option, please try again!")
       
            #will call userChoice() again
            userOption = socialNetwork.user_choice()
   
        #if user types "sign out"
        print()
        print("Signing out. Thank you for visiting the social network, come again to acquire more friends!")
        #will exit the program
        return
    
    #if the user enters no (when asked at the beginning about signing in)
    else:
        print()
        print ("exiting....come again!")
        #will exit the program 
        return
    

#in order to call the main method
if __name__ == "__main__":
    main() 