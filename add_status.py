# importing spy details and default or/and older status
from spy_details import spy
from globals import STATUS_MESSAGES, current_status_message

# importing termcolor colorful output
from termcolor import colored

# function to add status
def add_status(current_status_message):

    # status in beginning
    updated_status_message = None

    # check if current status is set or not
    if current_status_message != None:
        print ('Your current status message is %s \n' % (current_status_message))
    else:
        print ('You don\'t have any status message currently \n')

    # Ask user for choose default status or an old status.
    default = input(colored("Do you want to select from the older status (y/n)? ",'cyan'))

    # when spy wants to add another status rather than existing one
    # .upper() converts everything to uppercase
    if default.upper() == "N":
        new_status_message = input(colored("What status message do you want to set?: ",'cyan'))

        # validating users input.
        if len(new_status_message) > 0:
            # adding new status to default status or older status list.
            STATUS_MESSAGES.append(new_status_message)
            #updated status
            updated_status_message = new_status_message
            print ('Your updated status message is: %s' % (updated_status_message))
        else:
            print ("You did not provided any status message. Try again.")

    # spy wants to choose from existing status.
    elif default.upper() == 'Y':

        # counter for serial number of messages.
        item_position = 1

        # printing all older status messages so spy can choose
        for message in STATUS_MESSAGES:
            print ('%d. %s' % (item_position, message))
            item_position = item_position + 1

        # asking users choice which index of list he wants to choose
        message_selection = int(input(colored("\nChoose from the Index of status: ",'cyan')))

        # validating users input and set status of choice if exist.
        if len(STATUS_MESSAGES) >= message_selection:
            #updating
            updated_status_message = STATUS_MESSAGES[message_selection - 1]
            print ('Your updated status message is: %s' % (updated_status_message))
        # when user has wrong choice or choice that does not exist.
        else:
            print ("Invalid choice. Try again.")
    # when user has diffrent choice than yes and no
    else:
        print ('The option you chose is not valid! Press either y or n.')
    # updated message will be read
    return updated_status_message