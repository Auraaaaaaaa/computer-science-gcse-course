from random import randint
matching = False
while matching == False:
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    if dice1 != dice2:
        print("Dice do not match! Rolling again...")
        continue
    elif dice1 == dice2:
        print(f"You won! the dices match at {dice1}")
        exit()