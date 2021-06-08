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
##################################
import random
choice = input("What do you choose? 'rock','paper' or 'scissors' ")
# computer choice random.choice()
choice_box = ["r","p","s"]
computer_choice = random.choice(choice_box)
# checking player input i.e input controll if it is right then only code is going to continue if it is wrong then player loose 
if choice[0].lower() not in choice_box:
  print("you loose because you choose a wrong option")
else:
  print("You selected.")
  # player choice printing
  if choice[0].lower() == "r":
    print(rock)
  elif choice[0].lower() == "p":
    print(paper)
  else:
    print(scissors)
  # computer choice printing
  print("computer selects.")
  if computer_choice == "r":
    print(rock)
  elif computer_choice == "p":
    print(paper)
  else:
    print(scissors)
  # game logic
  result = 0

  if choice[0].lower() == computer_choice:
    result += 1
  else:
    if choice[0].lower()=="r" and computer_choice == "s":
      result += 2 #win for result = 2
    elif choice[0].lower()=="r" and computer_choice == "p":
      result += 3 # loss
    else:
      if choice[0].lower()=="p" and computer_choice == "r":
        result += 2 #win for result = 2
      elif choice[0].lower()=="p" and computer_choice == "s":
        result += 3 # loss
      else:
        if choice[0].lower()=="s" and computer_choice == "p":
          result += 2 #win for result = 2
        else:
          
          result += 3
    
  # result printing
  if result == 1:
    print("It's draw!")
  elif result == 2:
    print("You have won the game!")
  else:
    print("you loose!")