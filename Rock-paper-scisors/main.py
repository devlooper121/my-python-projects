import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
ascii_char = [" ",rock,paper,scissors]

##################################


def welcome() -> None:
    print("Welcomme to Rock paper Scissors World class Console game.")

def user_choice() -> int:
    choice = int(input("What do you choose? 1='rock',2='paper' or 3='scissors' "))
    if choice not in (1,2,3):
        choice = int(input("Make a vaid choice:1='rock',2='paper' or 3='scissors': "))
    else:
        return choice


computer_choice = random.choice((1,2,3))

def game_mind(user, computer) -> int:
    if user==computer:
        return 0
    elif user == 3 and computer == 1:
        return -1
    elif user > computer:
        return 1
    elif user == 1 and computer ==3:
        return 1
    else:
        return -1


def cui(user, computer)->None:
    
    print(f"You Choose: {ascii_char[user]}  Computer Choose: {ascii_char[computer]} ")
    if game_mind(user, computer) == 0:
        print("Its a draw!")
    elif game_mind(user, computer) == 1:
        print("you won!")
    else:
        print("You loose")

def main() -> None:
    welcome()
    user_coose = user_choice()
    cui(user=user_coose, computer=computer_choice)

if __name__=='__main__':
    main()