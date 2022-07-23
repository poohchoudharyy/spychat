# importing friend, steganography library, and datetime
from select_friend import select_friend
from LSBSteg import *
from spy_details import friends
from send_message_help import send_message_help
from spy_details import ChatMessage
from LSBSteg import *
# importing termcolor and colorama for colorful output.
from termcolor import colored
from colorama import init

# initializing colorama
init()

# function for read message
def read_message():
    # choose friend from the list to communicate
    sender = select_friend()

    # encrypted_image = input("Provide encrypted image : ")
    # pattern_e = '^[a-zA-Z]+\.jpg$'

# error handling if secret message is present or not
    try:
        im = cv2.imread("Hidden_Image.png")
        steg = LSBSteg(im)
        secret_message = steg.decode_text()
        print ("The secret message is ")
        print (colored(secret_message, 'red'))
        words = secret_message.split()

        # converting text into upper case
        new = (secret_message.upper()).split()

        # controlling the words spoken by spy in every message received.
        friends[sender].count += len(words)

        # if Emergency words present\
        if "SOS" in new or "SAVE" in new or "HELP" in new or "ACCIDENT" in new or "ALERT" in new:

            # Emergency alert
            # Termcolor and Colorama both libraries happily used.
            print (colored("!", 'grey', 'on_yellow')),
            print (colored("!", 'grey', 'on_yellow')),
            print (colored("!", 'grey', 'on_yellow'))

            # help friend by sending a helping message
            print (colored("The friend who sent this message need your help.", 'cyan'))
            print (colored("You can help your friend by sending helping message.", 'cyan'))
            print (colored("Select the friend to send helping message", 'red'))

        # calling the send message help function
        send_message_help()

        # the message has been sent successfully
        print (colored("You just sent a message to help your friend.", 'magenta'))

        # add the chat to sender
        new_chat = ChatMessage(secret_message, False)
        friends[sender].chats.append(new_chat)
        print (colored("Your secret message has been saved.", 'cyan'))

        # average words spoken by your friend
        print ("Average words said by : ")
        print (colored(friends[sender].name, 'red')),
        print (" is ")
        print (colored(friends[sender].count, 'blue'))

        # delete a spy if he speaks too much
        if(len(words)>100):
            print (colored(friends[sender].name, 'red')),
            print (colored(" removed from friends list. He was out of his mind, huh!.", 'yellow'))
        # remove that chatterbox friend.
            friends.remove(friends[sender])

    except TypeError:
        print(colored("This image has no secret message. No decoding. Aah!"))

        # users input validations
        if (re.match(pattern_e, encrypted_image) != None):
            print (colored('All perfect', 'red'))
        else:
            print (colored('Sorry! Invalid entry. We can\'t validate your input and output\n ', 'blue'))
            print (colored('The convention to follow is: \n ', 'blue'))
            print (colored('1. Encrypted should ends with (.jpg) format.\n ', 'blue'))
            print (colored('Keep in mind and Try Again\n\n ', 'blue'))