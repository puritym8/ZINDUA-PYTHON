import random

# Define the snakes and ladders positions
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

# Function to get the current position considering snakes and ladders
def get_position(player, current_pos):
    if current_pos in snakes:
        print(f"Player {player} landed on a snake! Sliding down from {current_pos} to {snakes[current_pos]}")
        return snakes[current_pos]
    elif current_pos in ladders:
        print(f"Player {player} landed on a ladder! Climbing up from {current_pos} to {ladders[current_pos]}")
        return ladders[current_pos]
    else:
        return current_pos

# Function to roll the dice and update position
def dice_roll(player, current_pos):
    dice = random.randint(1, 6)
    print(f"Player {player} rolled a {dice}.")
    new_pos = current_pos + dice
    new_pos = get_position(player, new_pos) # Check for snakes and ladders
    return new_pos

# Function to play the game
def play():
    print("Welcome to Snake and Ladder Game.")
    print("Version: 1.0.0")
    print("Rules:")
    print("1. Initially all the players are at starting position i.e. 0.")
    print("   Take it in turns to roll the dice.")
    print("2. If you land at the bottom of a ladder, you can move up to the top of the ladder.")
    print("3. If you land on the head of a snake, you must slide down to the bottom of the snake.")
    print("4. The first player to get to the FINAL position is the winner.")
    print("5. Hit enter to roll the dice.")
    print("6. Sign up the number of players and names to begin")

    num_players = int(input("Enter the number of players (1-4): "))
    if not 1 <= num_players <= 4:
        print("Invalid number of players. Please enter a number between 1 and 4.")
        return

    player_names = [input(f"Enter name for Player {i+1}: ") for i in range(num_players)]

    positions = [0] * num_players

    

play()
