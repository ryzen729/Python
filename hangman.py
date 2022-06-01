
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
    print(count)

    index = 0
    if count >= 1:
        
        for replace_letter in random_word:
            if replace_letter == guess:
                blank_space[index] = guess
            index = index + 1
        print(blank_space)
        for check in blank_space:
            if check != "_":
                bool_val = False

    print(blank_space)


        

    #Check if player has won
    new_word = ""
    for letters in blank_space:
        new_word += letters
    print(new_word)

    if new_word == random_word:
        print("Player has won")