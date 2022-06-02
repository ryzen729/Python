
from pickle import TRUE
import random


HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

print("Let's play Hangman")
print(HANGMANPICS[0])
lives = 6
index_hangman = 0
#Generate random word from list
word_list = ["elephant","apple","mango","cocacola","fanta","notebook"]
random_word = word_list[random.randint(0,len(word_list)-1)]

#Generate blank spaces for the word
print(f"Chosen word is {random_word}")
blank_space = list()
for x in random_word:
    blank_space.append("_")
print(blank_space)
print()

bool_val = TRUE
#Input letter from user
while bool_val:
    guess = input("Guess a letter: ")
    print()

    #Replace blank space with correct word
    count = 0
    for letter in random_word:
        if letter == guess:
            count = count + 1

    #substitutue value in "_"
    index = 0
    # keep count of "_"
    blank_count = 0

    #right answer
    if count >= 1:
        
        for replace_letter in random_word:
            if replace_letter == guess:
                blank_space[index] = guess
            index = index + 1
        print(blank_space)
        for check in blank_space:
            if check == "_":
                blank_count += 1
        
        if blank_count == 0:
            bool_val = False




        

    #Check if player has won
    new_word = ""
    for letters in blank_space:
        new_word += letters

    if new_word == random_word:
        print("Player has won")

    
    # wrong answer
    
    if count == 0:
        print(HANGMANPICS[index_hangman + 1])
        lives -= 1
        index_hangman += 1

    if lives <= 0:
        print("Game Over")
        bool_val = False