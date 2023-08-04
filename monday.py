#this is class for the function.
#we will do the small project using python fuction for dice...

#dice ma total six part hunxa ...
#import random le reandom module import garxa which is buile in python module. it is used to generate randon number


import random

def roll_dice():
    return random.randint(1,6)



def dice_rolling_simulator():
    while True:
        input("please enter to the roll the dice...")
        result=roll_dice()
        print(f"you rolled a {result} ")


        again=input("do you want to roll again ?(y/n)")
        if again.lower()!='y':
            break



if __name__=="__main__":
    dice_rolling_simulator()
    