def get_valid_move(player_name):
    """
    Prompt the given player for a move until a valid input (1, 2, or 3) is provided.
    """
    while True:
        try:
            move = int(input(f"{player_name} - How many sticks will you pick? (1, 2, or 3): "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if move in (1, 2, 3):
            return move
        else:
            print("Only valid input is 1, 2, or 3.")

def display_sticks(count):
    """
    Display the remaining sticks as vertical bars.
    """
    print("| " * count)

def toothpick_game():
    print("Welcome to Toothpick Game!!")
    player_1 = input("Name of Player one?: ")
    player_2 = input("Name of Player two?: ")

    count_pick = 13  # total number of sticks
    display_sticks(count_pick)

    players = [player_1, player_2]
    current_player = 0

    while count_pick > 0:
        # Get a valid move from the current player
        move = get_valid_move(players[current_player])
        count_pick -= move
        display_sticks(count_pick)

        # Check if the current move ends the game
        if count_pick < 1:
            print(f"{players[current_player]} wins!!!!")
            break

        # Toggle to the next player
        current_player = (current_player + 1) % 2

if __name__ == "__main__":
    toothpick_game()
