# number gussing game:

import random

def number_guessing_game():
    secret_number=random.randint(1,100)
    attempts=0

    while True:
        guess=int(input("guess the number from 1 to 100:"))
        attempts+=1

        if guess==secret_number:
            print("congrants you won it")


        elif guess<secret_number:
            print("too low,try again")
        else:
            print("too high. try again.")


if __name__=="__main__":
    number_guessing_game()


    #wrong  