
import random
# Rock Paper Scissors ASCII Art

# Rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

user_select = int(input(("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")))
random_select = random.randint(0,2)

if user_select == 0:
    print(rock)
    if random_select == 1:
        print(paper)
        print("You lost")
    elif random_select == 0:
        print(rock)
        print("Its a draw")
    elif random_select == 2:
        print(scissors)
        print("You have won")

if user_select == 1:
    print(paper)
    if random_select == 1:
        print(paper)
        print("Its a draw")
    elif random_select == 0:
        print(rock)
        print("You win")
    elif random_select == 2:
        print(scissors)
        print("You loose")


if user_select == 2:
    print(scissors)
    if random_select == 1:
        print(paper)
        print("You win")
    elif random_select == 0:
        print(rock)
        print("You loose")
    elif random_select == 2:
        print(scissors)
        print("Its a draw")