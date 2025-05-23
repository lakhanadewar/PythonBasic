print("Welcome to Pizza App")
size=   input("What size of Pizza you want? S, M or L :")
pepperoni=  input("Do you want pepperoni on your Pizza? Y for Yes and N for No: ")
extra_cheeze=   input("DO you want Extra Cheeze on your Pizza? Y for Yes and N for No: ")

pizza_price=0

if size=='S':
    pizza_price=15
elif size=='M':
    pizza_price=20
elif size=='L':
    pizza_price=25
else:
    print("Enter a Valid Pizza Size S, M or L Only!")

if pepperoni=='Y': 
    if size=='S':
        pizza_price+=2
    else:
        pizza_price+=3

if extra_cheeze=='Y':
    pizza_price+=1

print(f"Your final Bill is ${pizza_price}")