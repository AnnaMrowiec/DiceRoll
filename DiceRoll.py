import random

def main():
    player1 = 0
    player2 = 0
    rounds = 1

    while rounds != 4:
        print('Round ' + str(rounds))
        player1 = diceRoll()
        player2 = diceRoll()
        print(player1)
        print(player2)

        rounds = rounds + 1

        if player1 > player2:
            print('Player1 won!')
        elif player2 > player1:
            print('Player2 won!')
        else:
            print('It is a draw!')

def diceRoll():
    roll = random.randint(1, 6)
    return roll

print(main())
