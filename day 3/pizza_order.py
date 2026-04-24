print("welcome to python pizza deliveries")
size= input("what size pizza do u want? S, M, OR L: ")
pepperoni= input("do you want pepperoni on your pizza? Y or N: ")
extra_cheese= input("do you want extra cheese? Y or N: ")
price=0
if size == "S":
    price += 15
elif size == "M":
    price += 20
elif size == "L":
    price += 25
else:
    print("please enter correct input size")

if   pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3

if extra_cheese =="Y":
    price += 1

print(f"fianal bill: ${price}") 
