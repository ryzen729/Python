# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

complete_name = name1 + name2
first_count = "true"
second_count = "love"
first_number = 0
second_number = 0
for x in first_count:
    count_number = complete_name.lower().count(x)
    first_number = first_number + count_number
 
for y in first_count:
    count_second_number = complete_name.lower().count(y)
    second_number = second_number + count_second_number

total_number = str(first_number) + str(second_number)
print(total_number)

in_total_number = int(total_number)

if in_total_number <10 and in_total_number >90:
    print(f"Your score is {in_total_number}, you go together like coke and mentos.")

if in_total_number >= 40 and in_total_number <= 50:
    print(f"Your score is {in_total_number}, you are alright together")

else:
    print(f"Your score is {in_total_number}.")