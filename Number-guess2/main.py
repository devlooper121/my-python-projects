# generate a random number
from random import randint
import random


# Global variable
HARD_LEVEL = 5
LOW_LEVEL = 10
SUPER = 1

# compare function
def compare(guess_num, random_num, life):
    
    if guess_num > random_num:
        print("\nSorry...\nToo high.")
        return life - 1
    elif guess_num < random_num:
        print("\nSorry...\nToo low.")
        return life - 1
    else:
        print("You guess the correct number.\nExcelent!")
        return life    
    
       

# level selector
def level():
    print("\nWhich way you wanna go Easy Or Hard?")
    mood = input("Type 'easy' or 'hard'. : ").lower()
    if mood == 'easy':
        life = LOW_LEVEL
    elif mood == 'hard':
        life = HARD_LEVEL
    else:
        print("Surprise...\nGod Mood!")
        life = SUPER
    return life
from art import logo
print(logo)
def game():
    rand_num = randint(1,100)
    life = level()
    guess_num = 0

    # main code
    while guess_num != rand_num:
        print(f"\nYou have only {life} guesses")
        guess_num = int(input("\nGuess That Number: "))


        life = compare(guess_num,rand_num,life)

        if life == 0:
            
            print(f"\nYou'v lost.\n Number was {rand_num}")
            next_game = input("Do you wanna try again? ")
            if next_game == 'y':
                game()
            else:
                print("Thank you!")
            return
        
if __name__=='__main__':      
    print("i am thinking number between 1 and 100.")
    play_or = input("Do you wanna guss that number? 'y' or 'n': ").lower()
    if play_or == 'y':
        game()
    else:
        print("goodbye!")
