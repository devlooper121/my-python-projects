from random import randint
from art import logo

import os
from time import sleep

print(logo)
print("Welcome! To the Number Gharduessing Game")
print("I'm thinking a number between 1 to 100")
rand_int = randint(1,100)

game_over = False

while not game_over:

    mood = input("Choose difficulty. Type 'easy' or 'hard': ").lower()
    if mood == 'easy':
        life = 10
    elif mood == 'hard':
        life = 5
    else:
        print("super mode")
        life = 1
    original_life = life
    print(f"You Got Only {life} guesses.")
    while life > 0 and not game_over:
        
        num = int(input("Guess a number? "))
        if num == rand_int:
            print("Your Guess is Correct! you win.")
            game_over = True
            if life > original_life//2:
                print("You are Good!")
        elif num < rand_int:
            print("Too low Guess again.")
            life -= 1
            if life != 0:
                print(f"You have only {life} guess left")
        else:
            print("Too high Guess again.")
            life -= 1
            if life != 0:
                print(f"You have only {life} guess left")
     
    if life ==0:
        game_over = True
        print("Unluckly You've run out of guesses, you lose.")



# The screen clear function
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
# wait for 5 seconds to clear screen
sleep(5)
# now call function we defined above

screen_clear()