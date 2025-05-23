
print("Welcome to Toothpick Game!!")
player_1=input("Name of Player one?: ")
player_2=input("Name of Player two?: ")

count_pick=13
print(f"| "*count_pick)

while True:
    
    player_1_move=int(input(f"{player_1} How Many Stick you will Pick?: "))
    if player_1_move>=4:
        while player_1_move >=4:
            player_1_move=int(input("Only Valid input 1,2 or 3 : "))
            if player_1_move<4:
                count_pick -=player_1_move
    else:
        count_pick -=player_1_move
    print(f"| "*count_pick)
    if count_pick <1:
        print(f"{player_1} Wins!!!!")
        break
    
    player_2_move=int(input(f"{player_2} How Many Stick you will Pick?: "))
    if player_2_move>=4:
        while player_2_move >=4:
            player_2_move=int(input("Only Valid input 1,2 or 3 : "))
            if player_2_move<4:
                count_pick -=player_2_move
    else:
        count_pick -=player_2_move
    print(f"| "*count_pick)
    if count_pick <1:
        print(f"{player_2} Wins!!!!")
        break
    
    
