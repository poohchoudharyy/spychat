def start_chat(spy_name,spy_sal,spy_age,spy_rating):
    welcome = '\n authentication complete.welcome' + 'name:' + spy_sal + spy_name + 'age:' + spy_age + '\n rating:' + spy_rating + 'Proud to have you on board'
    print('welcome')
show_menu=True
while show_menu:
    menu_choices = "what do you want to do:\n"
    "1.add status\n"
    "2.add friend\n"
    "3.send msg\n"
    "4.read msg\n"
    "5.read chats\n"
    "6.close\n\n"
    result=input(menu_choices)
    if(result == 1):
        current_status= add_status (current_status)
    elif(result == 2):
        no_of_friends=add_friend()
        print("you have %d friends"%(no_of_friends))
    elif(result == 3):
        send_msg()
    elif(result == 4):
        read_msg()
    elif(result == 5):
        read_chat()
    elif(result == 6):
        #closing app
        show_menu=False
    else:
        print("wrong choice,try again!")
        exit()















