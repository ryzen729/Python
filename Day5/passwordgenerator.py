import random


letters = ["a","b","c","d","e","f","g","h","i","j","k","l",
            "m","n","o","p","q","r","s","t",
            "u","v","w","x","y","z","A","B","C","D",
            "E","F","G","H","I","J","K","L",
            "M","N","O","P","Q","R","S","T",
            "U","V","W","X","Y","Z"]

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','@','#','$','%','^','&','*']


print("Welcome to PyPassword Generator")
nr_letters = int(input("How many letter you want?"))
nr_numbers = int(input("How many numbers you want?"))
nr_symbols = int(input("How many symbols you want?"))

letter_random = []
for i in range(0,nr_letters):
    letter_random.append(letters[random.randint(0,len(letters)-1)])
print(letter_random)

number_random = []
for j in range(0,nr_numbers):
   number_random.append(numbers[random.randint(0,len(numbers)-1)])
print(number_random)


symbols_random = []
for k in range(0,nr_symbols):
    symbols_random.append(symbols[random.randint(0,len(symbols)-1)])
print(symbols_random)

letter_random.extend(symbols_random)
letter_random.extend(number_random)
print(letter_random)
random.shuffle(letter_random)
print(letter_random)
for x in letter_random:
    print(x,end="")
print()