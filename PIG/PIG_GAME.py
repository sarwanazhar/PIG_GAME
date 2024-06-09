import random


def roll():
    min_number = 1
    max_number = 6
    random_number = random.randint(min_number, max_number)
    return random_number


while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("players must be between (2-4)")
    else:
        print("Invalid. try again")

print(f"number of players are {players}")

max_score = 50
player_score = [0 for _ in range(players)]

while max(player_score) < max_score:
    
    for player_index in range(players):
        print(f"\nPlayer {player_index +1} turn has just started !!\n")

        current_score = 0

        while True:
            should_roll = input("Would you like to roll(y-n): ")
            if should_roll.lower() == "n":
                break
            elif should_roll.lower() == "y":
                value = roll()
                if value == 1:
                    print('You rolled 1 turn done!')
                    current_score = 0
                    break
                else:
                    current_score += value
                    print(f"You rolled a {value} !!")
                print(f"Your current score is {current_score}")
            else:
                print("Enter (Y-N) only")
        
        player_score[player_index] += current_score

        print(f'Your total score is {player_score[player_index]} !!')

        if player_score[player_index] >= max_score:
            print(f"\nPlayer {player_index +1} WON !!!\n")
            break