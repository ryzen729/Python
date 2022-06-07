import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty_type = input("Choose a difficulty. Type 'easy' or 'hard': ")

def easy_hard(counter):
    guess_number = random.randint(2,99)
    while counter > 0:
        chance = int(input("Make a guess: "))
        counter -= 1
        if guess_number == chance:
            print("YOur guess is correct")
            break
        else:
            if chance > guess_number:
                print("Too high")
                print(f"YOu have {counter} attempts remaining to guess the number.")
            else:
                print("Too Low")
                print(f"YOu have {counter} attempts remaining to guess the number.")
        

if difficulty_type == 'easy':
    easy_hard(10)
else:
    easy_hard(5)