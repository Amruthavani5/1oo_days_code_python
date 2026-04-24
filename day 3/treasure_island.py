print("Welcome to treasure island. \nyour mission is to find the treasure. \n")
direction=input('you\'re at the cross road. where do yo want to go? type "left" or "right": \n').lower()
if direction=="left":
    choice1=input('you have come to a lake there is a island inthe middle of the lake. type "wait" for a boat. type "swim" to swim across. \n').lower()
    if choice1=="wait":
        choice2= input('select the door colour? "red" "blue" or "yellow": \n').lower()
        if choice2=="yellow":
            print("you win!")
        else:
            print("game over")
    else:
        print("game over")


elif direction=="right":
    print("game over")
else:
    print("select correct direction")