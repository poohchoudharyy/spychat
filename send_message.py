# importing existing friend, steganography library, and datetime.
from select_friend import select_friend
from LSBSteg import *
from datetime import datetime
from spy_details import friends, ChatMessage

#importing regular expression for proper validation
# import re

# importing termcolor for colorful output.
from termcolor import colored

# function to send a secret message.
def send_message():

    # choose a friend from the list to communicate
    friend_choice = select_friend()

    # select an image in which you want to hide a secret message.
    original_image = input("Provide the name of the image to hide the message : ")

    # write the secret message
    text = input("Enter your message here : \n")

    # Encrypt the message using Steganography library
    steg = LSBSteg(cv2.imread(original_image))
    img_encoded = steg.encode_text(text)
    cv2.imwrite("Hidden_Image.png", img_encoded)
    # the message will be stored in chat message class
    new_chat = ChatMessage(text, True)

    # along the name of friend with whom we add message
    friends[friend_choice].chats.append(new_chat)

    # Successful message after encoding
    print (colored("Your message encrypted successfully.", 'red'))

    # name of the friend along which we add message.
    friends[friend_choice].chats.append(new_chat)
    print (colored("your secret message is ready.",'yellow'))