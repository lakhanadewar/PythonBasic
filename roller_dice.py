from random import randint

num_dice=int(input("Number of Dice to Roll?: "))
num_faces=int(input("Number of faces for a Dice?: "))

while True:
    for x in range(num_dice):
        rand = randint(1,num_faces)
        print(f"{rand}\t")
    reply=input("Roll again? (q for Quit): ")
    if reply=="q":
        break