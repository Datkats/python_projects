print("let's fix your WIFI connection")#introduction
print("___"*20)# divider line
print("Reboot the computer and try to connect.")# first action
user_respond=input("Did that fix the problem?: ").strip().lower()
if user_respond=="yes":# if user fixed problem Congrats to them
    print("Congrats!! You fixed your WIFI connection")
elif user_respond=="no":# if not teach them what to do next
    print("Reboot the router and try to connect.")
    user_respond=input("Did that fix the problem?: ").strip().lower()# ask again if they fixed issue
    if user_respond=="yes":# if user fixed problem Congrats to them
        print("Congrats!! You fixed your WIFI connection")
    elif user_respond=="no":# if not teach them what to do next
        print("Make sure the cables between the router and modem are plugged in firmly.")
        user_respond=input("Did that fix the problem?: ").strip().lower()# ask again if they fixed issue
        if user_respond=="yes":# if user fixed problem Congrats to them
            print("Congrats!! You fixed your WIFI connection")
        elif user_respond=="no":# if not teach them what to do next
            print("Move the router to a new location.")
            user_respond=input("Did that fix the problem?: ").strip().lower()# ask again if they fixed issue
            if user_respond=="yes":# if user fixed problem Congrats to them
                print("Congrats!! You fixed your WIFI connection")
            elif user_respond=="no":# if not stop asking
                print("Get a new router")
