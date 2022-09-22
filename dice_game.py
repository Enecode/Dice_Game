import random

def roll_dice():

    roll = input("Roll dice? (yes/no)")

    while roll.lower() == "Yes".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print(f"dice rolled: {dice1} and {dice2}")

        roll = input("Role again? (Yes/No): ")

roll_dice()
