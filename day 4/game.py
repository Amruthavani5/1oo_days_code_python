import random
game_images=["rock","paper","scissors"]
user_choice=int(input("what do you choose? type 0 for rock, 1 for paper or 2 for scissors"))
#rock beats scissors(0>2), scissors beat paper (2>1), paper beat rock (1>0)
if user_choice  >= 0 and user_choice <=2:
    print(game_images[user_choice])
computer_choice=random.randint(0,2)
print(game_images[computer_choice])

if user_choice == 0 and computer_choice == 2:
    print("you  wins!")
elif user_choice >=3  or user_choice < 0 :
    print("you typed invalid number, you lose!") 
elif computer_choice== 0 and   user_choice == 2 :
    print("you lose!")
elif computer_choice <  user_choice:
    print("you win!")
elif computer_choice >  user_choice:
    print("you lose!")
elif computer_choice ==  user_choice:
    print("its draw!")
  
