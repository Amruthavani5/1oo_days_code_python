#comparison operator (> , < , >= , <= , == , !=)
print("welcome to the ride")
height=int(input("what is your height in cm? "))
bill=0
if height >= 120:
    print("you can ride")
    age= int(input("what is your age? "))
    if age <= 12:
        bill=5
        print("child tickets are  $5")
    elif age <= 18:
        bill=7
        print("youth tickets are $7")
    elif age >= 45 and age <= 55:
        print("everything is ok. have a free ride on us! ")
        
    else:
        bill=12
        print("adult tickets are $12") 

    wants_photo=input("do u want to have photo take? type y for yes n for no. ")
    if wants_photo == "y":
        bill +=3
    
    print(f"your final bill is {bill}")

else:
    print("sorry, you can't ride")

