# importing spy and existing friends
from spy_details import Spy, friends
# importing regular expressions for proper validation
import re

# importing termcolor for colorful output
from termcolor import colored

# function to add new friends.
def add_friend():
    # using class spy
    new_friend = Spy(" ", " ", 0, 0.0)

    # ask user for name and salutation of friend
    new_friend.name = input("Please add your friend's name: ")
    pattern_n = '^[a-zA-Z\s]+$'
    # user validation.
    if(len(new_friend.name) > 0 and re.match(pattern_n,new_friend.name)!=None):
        if(len(new_friend.name)>20):
            print (colored("Your name is too big.","red."))
    else:
        print (colored("Name should be alphabetic", "red"))
        return add_friend()

    new_friend.salutation= input("What to call Mr. or Ms.?: ")
    pattern_s = '^[a-zA-Z\s]+$'
    # user validation
    if(len(new_friend.salutation) >0 and re.match(pattern_s,new_friend.salutation) != None):
        if(len(new_friend.salutation)>5):
            print (colored("Your salutation is too big.", "red"))
    else:
        print (colored("Salutation should be alphabetic", "red"))
        return add_friend()


    # concatination for full name
    new_friend.name = new_friend.salutation + " " + new_friend.name

    # ask for age of friend
    new_friend.age = int((input("Age? ")))
    # pattern_a = '^[0-9]+$'
    # user validation
    # if(re.match(pattern_a,new_friend.age)!=None):
    if(12 < new_friend.age < 50):
        True
    else:
        print (colored("Age should be in beetween 12 to 50", 'red'))
    # else:
    #     print (colored("Age should be Numeric.", "red"))
    # return add_friend()

    #ask for rating of friend, float represents type casting in float
    new_friend.rating = float(input("Spy rating? "))
    # user validation.
    # pattern_r = '^[0-9]+\.[0-9]+$'
    # if(re.match(pattern_r,new_friend.rating)!= None):
    if (new_friend.rating>0.0):
        True
    else:
        print ("Ratting should be more than 0.0")
    # else:
    #     print (colored("Ratting should be Numeric or Decimal.", "red"))
    # return add_friend()


    # add friend if conditions satisfies
    friends.append(new_friend)
    print (colored('Friend Added!', 'magenta'))

    # returning total no of friends.
    return len(friends)