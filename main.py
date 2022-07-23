from spy_detail import spy, Spy, ChatMessage, friends
# from steganography.steganography import Steganography
# from colors import color
from datetime import datetime
import sys
from termcolor import colored, cprint

#importing colors from colors.py for output/messages.
from colors import prCyan, prRed, prYellow, prGreen, prLightPurple, prPurple , R , B , Black

#Status Message lists
STATUS_MESSAGES = ["'My name is Bond, James Bond'", "'Shaken, not stirred.'", "'Keeping the British end up, Sir'"]

question = "Do you want to continue as " + spy.spy_salutation + " " + spy.name + " (Y/N)? "
existing = input(question)
if existing != 'Y' or existing != 'N':
    prRed('Wrong Input! Try Again')
    existing = input(question)


# from start_chat import start_chat
# from spy_detail import spy_name,spy_sal,spy_rating,spy_age
# question=input("continue as" +" " +spy_sal +"  " +spy_name + "yes/no?")
# if(question=='yes'):
#     start_chat(spy_name,spy_sal,spy_age,spy_rating)
#

def start_chat(spy):
    spy.spy_name = spy.spy_sal + " " + spy.spy_name
    if spy_age > 12 and spy_age < 50:
        print("authentication complete.welcome" + spy.spy_name + "age:" + str(spy.spy_age) + "and rating of:" + str(spy.spy_rating) + " Proud to have you on board")
        welcome = '\n authentication complete.welcome' + 'name:' + spy_sal + spy_name + 'age:' + spy_age + '\n rating:' + spy_rating + 'Proud to have you on board'
        print('welcome')


    show_menu = True
    while show_menu:
        menu_choices = "what do you want to do:\n 1.add status\n 2.add friend\n 3.send msg\n 4.read msg\n 5.read chats\n 6.close\n\n"
        result = input(menu_choices)
        if(result == 1):
            current_status_message = add_status(current_status_message)
        elif(result == 2):
            no_of_friends = add_friend()
            print("you have %d friends" % (no_of_friends))
        elif(result == 3):
            send_msg()
        elif(result == 4):
            read_msg()
        elif(result == 5):
            read_chat()
        elif(result == 6):
            # closing app
            show_menu = False
        else:
            print("wrong choice,try again!")
            exit()
            STATUS_MESSAGES=["My name is Bond","Shaken:not stirred"]

def add_status():
    updated_status_message = None

    if spy.current_status_message != None:
        print("your current status message is %s \n" % (spy.current_status_message))
    else:
        print("you don't have any status message currently \n")
        default = input("do you want to select from older statuses(Y/N)?")
        if default.upper() == "N":
            new_status_msg = input("what status msg do you want to set?")

            if len(new_status_msg) > 0:
                STATUS_MESSAGES.append(new_status_msg)
                #append = inserting the new value in the array
                updated_status_message = new_status_msg
        elif default.upper() == 'Y':
            item_position = 1
            for message in STATUS_MESSAGES:
                print('%d. %s' % (item_position, message))
                item_position = item_position + 1
            message_selection = int(input("\n choose from the above messages"))

            if len(STATUS_MESSAGES) >= message_selection:
                updated_status_message = STATUS_MESSAGES[message_selection - 1]
        else:
            print('The option you choose is not valid! Press either y or n.')
        if updated_status_message:
            print('your updated status message is: %s' % (updated_status_message))
        else:
            print("you current don't have a status update")
        return updated_status_message
    #end function to add status

    #start function to add friend
def add_friend():
    new_friend = Spy('','',0,0.0)
    while True:
        new_friend.name = input("please add your friend's name:")
        if new_friend.name.replace(" ", "").isalpha():
            break
        print("ERROR !!! Invalid Friend Name")
    while True:
        new_friend.salutation = input("Are they Mr. or Ms.?:")
        if new_friend.salutation.replace(".", "").isalpha():
            break
        print("ERROR !!! Invalid Friend Name")
    new_friend.name = new_friend.salutation + " " + new_friend.name
    while True:
        new_friend.age = input("Age?")
        if new_friend.age.replace("", "").isdigit():
            new_friend.age = int(new_friend.age)
            break
        print("ERROR!!! Age should be in NUMBERS")
    while True:
        new_friend.rating = input("Spy rating?")
        if new_friend.rating.replace("", "").isdigit():
            new_friend.rating = float(new_friend.rating)
            break
        print("ERROR!!! rating should be in numbers and precise")
    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print('Friend Added!')
    else:
        print("Sorry! Invalid entry. we can't add spy with the details you provided")
    return len(friends)


def select_a_friend():
    item_number = 0
    for friend in friends:
        print('%d. %s %s aged %d,with rating of %.2f is online.'% (item_number +1, friend.salutation, friend.name, friend.age, friend.rating))
        item_number = item_number + 1
    friend_choice = input("choose from your friends")
    friend_choice_position = int(friend_choice) - 1
    return friend_choice_position

def send_msg():
    friend_choice = select_a_friend()
#     original_image = input("What is the name of the image?")
#     output_path = "C:\Users\Nasir Shariff\PycharmProjects\SpyChat_Python-master\Secret\output.jpg"
#     #Validation for not entering mess
    while True:
        text = input("What do you want to say? ")
        words = text.split()
        length = sum(len(word) for word in words)
#         if text !=("") and length <=100:
#             Steganography.encode(original_image, output_path, text)
#             break
#         prRed("ERROR !!! Either empty or 100 words exceeded")
        new_chat = ChatMessage(text,True)
        friends[friend_choice].chats.append(new_chat)
        print("Your secret message image is ready!")

def read_msg():
        sender = select_a_friend()
        #     output_path = input("What is the name of the file?")
        #     secret_text = Steganography.decode(output_path)
        new_chat = ChatMessage(secret_text, False)
        friends[sender].chats.append(new_chat)
        print(secret_text)
    # END Function to read message in SpyChat


def read_chat_history():
    read_for = select_a_friend()
    print('\n')
    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print('[%s] %s: %s' %(B+ chat.time.strftime("%d %B %Y"), R+ 'You said:', Black+ chat.message))
        else:
            print('[%s] %s said: %s' % (B+ chat.time.strftime("%d %B %Y"), R+ friends[read_for]. name, Black+ chat.message))





































    #fetch

    else:
        spy_name = "BOND"
        spy_sal = "MR."
        print(spy_sal + spy_name)
        spy_name=input('welcome to spychat please enter your name')
        if len(spy_name)>0:
            print('welcome'+spy_name)
            spy_sal=input('Should i call you mister / miss')
        # elif len(spy_sal)>0:
        #     print('glad to meet you'+spy_sal+spy_name)
        #     print(spy_sal)
        #     print('glad to have you back'+spy_sal + spy_name)
            spy_by = input('what is your birth year?')
            spy_age = 2022-int(spy_by)
            print(spy_age)
            #nested if
            if spy_age>18 and spy_age<50:
                print('the age is verified')
                spy_rating = 0.0
                spy_rating=input('enter the spy rating')
                spy_rating=float(spy_rating)
                print(spy_rating)
                if spy_rating > 4.5:
                    print('great!')
                elif spy_rating > 3.5 and spy_rating <= 4.5:
                    print('good')
                elif spy_rating > 2.5 and spy_rating <= 3.5:
                    print('Average')
                else:
                    print('Your fired')

                print('fail')
                spy_online='TRUE'
                # print("Authentication complete welcome" + spy_sal + spy_name + "age:" + str(spy_age) + " & spy_rating of:" + str(spy_rating) + "proud to have you onboard")
                print('Authentication complete welcome, %s %s, age %d and spy_rating of %f, proud to have you on board' %(spy_sal,spy_name,spy_age,spy_rating))
            # else:
            #     print('the age is not verified')
            else:
                print('sorry you are not eligible')
        else:
            print('A spy needs to have valid name')